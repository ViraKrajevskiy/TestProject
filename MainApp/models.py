from django.db import models
from django.urls import reverse, NoReverseMatch

class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название пункта')
    named_url = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Named URL',
        help_text='Имя named URL из urls.py (например: "home", "about")'
    )
    explicit_url = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Явный URL',
        help_text='Явный URL (например: "/about/", "/contact/")'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительский пункт'
    )
    menu_name = models.CharField(
        max_length=50,
        verbose_name='Название меню',
        help_text='Уникальное название меню для template tag (например: "main_menu", "footer_menu")'
    )
    order = models.IntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['menu_name', 'order', 'name']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return f"{self.menu_name} - {self.name}"

    def get_url(self):
        """Возвращает URL для пункта меню"""
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return f"/{self.named_url}/"
        elif self.explicit_url:
            if not self.explicit_url.startswith('/'):
                return f'/{self.explicit_url}'
            return self.explicit_url
        return '#'

    def get_absolute_url(self):
        return self.get_url()