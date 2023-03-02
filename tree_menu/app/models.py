from django.db import models


class Menu(models.Model):
    """Модель основного меню."""

    class Meta:
        """Метакласс для модели основного меню."""

        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name='Наименование меню',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание меню',
    )
    slug = models.SlugField(
        max_length=20,
        verbose_name='Слаг меню',
    )

    def __str__(self) -> str:
        """Метод возвращает строковое представление основного меню."""
        return self.name


class Item(models.Model):
    """Модель пункта меню."""

    class Meta:
        """Метакласс для модели пункта меню."""

        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    name = models.CharField(
        max_length=128,
        verbose_name='Наименование пункта меню',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание пункта меню',
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.PROTECT,
        related_name='items',
        verbose_name='Меню',
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='childs',
        verbose_name='Родительский пункт',
    )
    slug = models.SlugField(
        max_length=20,
        verbose_name='Слаг пункта меню',
    )

    def __str__(self) -> str:
        """Метод возвращает строковое представление пункта меню."""
        return self.name
