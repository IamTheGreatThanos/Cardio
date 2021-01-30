import socket
import select
import requests
import binascii

SERVER_ADDRESS = ('82.200.167.29', 9881)
# SERVER_ADDRESS = ('localhost', 9879)

dd = ""
# Говорит о том, сколько дескрипторов единовременно могут быть открыты
MAX_CONNECTIONS = 30

# Откуда и куда записывать информацию
INPUTS = list()
OUTPUTS = list()

def get_non_blocking_server_socket():

    # Создаем сокет, который работает без блокирования основного потока
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)

    # Биндим сервер на нужный адрес и порт
    server.bind(SERVER_ADDRESS)

    # Установка максимального количество подключений
    server.listen(MAX_CONNECTIONS)

    return server


def handle_readables(readables, server):
    """
    Обработка появления событий на входах
    """
    global dd
    for resource in readables:
        # Если событие исходит от серверного сокета, то мы получаем новое подключение
        if resource is server:
            connection, client_address = resource.accept()
            connection.setblocking(0)
            INPUTS.append(connection)
            print("new connection from {address}".format(address=client_address))

        # Если событие исходит не от серверного сокета, но сработало прерывание на наполнение входного буффера
        else:
            data = ""
            try:
                data = resource.recv(1024)
            # Если сокет был закрыт на другой стороне
            except ConnectionResetError:
                pass

            if data:
                data = binascii.hexlify(data).decode()
                # Вывод полученных данных на консоль
                # print("getting data: {data}".format(data=str(data)))
                # if data != dd:
                # if len(data) % 6 == 0:
                    # dd += data
                # if len(dd) == 600:
                if len(data) > 18:
                    response = requests.post('https://back.cardioservice.com.kz/api/setByte/', data={'byte':str(data)})
                    # dd = ""
                # print(response)
                # Говорим о том, что мы будем еще и писать в данный сокет
                if resource not in OUTPUTS:
                    OUTPUTS.append(resource)

            # Если данных нет, но событие сработало, то ОС нам отправляет флаг о полном прочтении ресурса и его закрытии
            else:
                # Очищаем данные о ресурсе и закрываем дескриптор
                clear_resource(resource)


def clear_resource(resource):
    """
    Метод очистки ресурсов использования сокета
    """
    if resource in OUTPUTS:
        OUTPUTS.remove(resource)
    if resource in INPUTS:
        INPUTS.remove(resource)
    resource.close()

    print('closing connection ' + str(resource))


def handle_writables(writables):
    # global dd
    print(writables)
    # Данное событие возникает когда в буффере на запись освобождается место
    for resource in writables:
        try:
            resource.send(b'\x80\x00\x00')
        except OSError:
            clear_resource(resource)


if __name__ == '__main__':
    # Создаем серверный сокет без блокирования основного потока в ожидании подключения
    server_socket = get_non_blocking_server_socket()
    INPUTS.append(server_socket)

    print("server is running, please, press ctrl+c to stop")
    try:
        while INPUTS:
            readables, writables, exceptional = select.select(INPUTS, OUTPUTS, INPUTS)
            handle_readables(readables, server_socket)
            # handle_writables(writables)
    except KeyboardInterrupt:
        clear_resource(server_socket)
        print("Server stopped! Thank you for using!")