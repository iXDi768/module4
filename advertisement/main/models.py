from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()
class Advertisement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    title = models.CharField('заголовок', max_length = 128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits= 10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField('изображение', upload_to='advertisements/')


    class Meta:
        db_table = 'a'

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; font-weight: bold;">Сегодня в {}', created_time)

    @admin.display(description='дата обновления')
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html('<span style="color: green; font-weight: bold;">Обновлено сегодня в {}', updated_time)

    @admin.display(description='изображение')
    def image_display(self):
        from django.utils.html import format_html
        if self.image:
            return format_html(
                '<img src="{}" style="width: 45px; height:45px;">', self.image.url
            )
        else:
            return 'No Image'


