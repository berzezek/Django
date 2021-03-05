from django.db import models
from django.contrib.auth.models import User # Нужно импортировать табличку User
# Create your models here.

class Profile(models.Model):
    # Назвать класс как угодно
    user = models.OneToOneField(User, on_delete=models.CASCADE) # перед User можно добавить название "Пользователь"
    # Класс OneToOneField с ссылкой на запись из другой таблице и наоборот ("on_... при удалении - удалить")
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')
    # поле через которое будет загружать, класс ImageField, (def... картинка по умолчанию, upl... папка для загрузки)
    def __str__(self):
        return f'Профайл пользователя: {self.user.username}'
    # Чтобы отображалось нормально (через user можно связаться с другой табличкой... они уже связанны)
    # Устровить pip install pillow (для работы с изображениями)
    # делаем миграции и переходим в admin.py (1.1)
    class Meta: # Поменять название в панели администратора
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
