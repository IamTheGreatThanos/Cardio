from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from datetime import datetime


def user_photos_dir(instanse, filename):
    usrnme = f'{instanse.username}'
    folder_name = f"{usrnme}/{datetime.today().strftime('%d_%m_%Y')}/{filename}"
    return folder_name


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to=user_photos_dir, blank=True, null=True, default="default/default.png")
    location = models.TextField(blank=True, null=True)
    device_id = models.CharField(max_length=500, blank=True, null=True)

    CHOICES = ((0, 'Нет'), (1, 'Да'))
    GENDER_FEMALE = 0
    GENDER_MALE = 1
    GENDER_CHOICES = ((GENDER_FEMALE, 'Женский'), (GENDER_MALE, 'Мужской'))
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    diabet = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    asthma = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    # Гипертония
    hypertension = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    # Бывают ли боли в груди
    breast = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    # Были ли у вас когда-либо проблемы с сердцем
    heart = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    # Принимаете ли вы лекарства на постоянной основе
    medicines = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    # Есть ли у вас аллергии на лекарства или продукты?
    allergies = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    # Были ли у вас операции?
    operations = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    # психотропные препараты
    psychotropic_drugs = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    # Сердечно-сосудистые заболевания заболевания в семье
    diseases = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    #  наследственный Диабет
    hereditary_diabetes = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    # Курите ли вы?
    SMOKE_CHOICES = ((0, 'Нет'), (1, 'Да'), (2, 'Бросил(а)'))
    smoke = models.SmallIntegerField(choices=SMOKE_CHOICES, null=True, blank=True)
    # Были ли у вас депрессии или тревожные расстройства?
    depression = models.SmallIntegerField(choices=CHOICES, null=True, blank=True)
    # Употребляете ли алкоголь?
    ALCOHOL_CHOICES = ((0, 'Никогда'), (1, 'Редко'), (2, 'Регулярно'), (3, 'Часто'))
    alcohol = models.SmallIntegerField(choices=ALCOHOL_CHOICES, null=True, blank=True)
    # Как часто вы занимаетесь спортом?
    SPORT_CHOICES = ((0, 'Никогда'), (1, 'Редко'), (2, 'Несколько раз в неделю'), (3, 'Каждый день'))
    sport = models.SmallIntegerField(choices=SPORT_CHOICES, null=True, blank=True)
    # Какой тип питания вы придерживаетесь?
    NUTRITION_CHOICES = ((0, 'Другое'), (1, 'Обычное'), (2, 'Вегетарианское'))
    nutrition = models.SmallIntegerField(choices=NUTRITION_CHOICES, null=True, blank=True)
    # Как часто вы едите?
    EAT_CHOICES = ((0, 'Другое'), (1, '1 раз в день'), (2, '2 раза в день'), (3, '3 раза в день'))
    eat = models.SmallIntegerField(choices=EAT_CHOICES, null=True, blank=True)
    # Как вы оцениваете свое психоэмоциональное состояние?
    STATE_CHOICES = ((0, 'Плохое'), (1, 'Удовлетворительное'), (2, 'Хорошее'), (3, 'Отличное'))
    emotional_state = models.SmallIntegerField(choices=STATE_CHOICES, null=True, blank=True)

    STATUS_CHOICES = ((1, 'врач'), (2, 'пациент'), (3, 'ученый'))
    status = models.SmallIntegerField(choices=STATUS_CHOICES, null=True, blank=True) 