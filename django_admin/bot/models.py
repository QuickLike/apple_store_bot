import logging

from asgiref.sync import sync_to_async
from django.contrib.humanize.templatetags.humanize import intcomma
from django.db import models
from django.db.models import Prefetch
from django.utils.safestring import mark_safe


class TelegramUser(models.Model):
    user_id = models.PositiveBigIntegerField(
        verbose_name='ID Пользователя',
        unique=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=256
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=256,
        blank=True
    )
    username = models.CharField(
        verbose_name='Никнейм',
        max_length=256,
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name='Зарегистрирован',
        auto_now_add=True
    )

    def __str__(self):
        return f'ID {self.user_id} - {self.first_name} {self.last_name} ({self.username})'

    @classmethod
    @sync_to_async
    def async_create(cls, **kwargs):
        return cls.objects.get_or_create(**kwargs)

    @classmethod
    @sync_to_async
    def async_get_cart_items(cls, user_id: int):
        user = cls.objects.select_related('shopping_cart').get(user_id=user_id)
        if not hasattr(user, 'shopping_cart'):
            return []
        cart_items = list(
            CartItem.objects.filter(shopping_cart=user.shopping_cart).select_related('item').all())
        return cart_items

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('user_id',)


class Category(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=256
    )

    def __str__(self):
        return self.title[:32]

    class Meta:
        default_related_name = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'


class Item(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=256
    )
    color = models.CharField(
        verbose_name='Цвет',
        max_length=64
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE
    )
    subcategory = models.CharField(
        verbose_name='Подкатегория',
        max_length=256
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='items',
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.DecimalField(
        verbose_name='Стоимость',
        max_digits=10,
        decimal_places=0
    )
    stock = models.PositiveIntegerField(
        verbose_name='В наличии',
        default=10,
    )

    def __str__(self):
        return self.title[:64]

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % self.image)

    def price_view(self):
        return f'{intcomma(self.price)} ₽'

    class Meta:
        default_related_name = 'items'
        verbose_name = 'Товар'
        verbose_name_plural = 'товары'

    image_tag.short_description = 'Изображение'
    price_view.short_description = 'Стоимость'


class ShoppingCart(models.Model):
    user = models.OneToOneField(
        TelegramUser,
        verbose_name='Пользователь',
        on_delete=models.PROTECT,
        related_name='shopping_cart'
    )
    items = models.ManyToManyField(
        Item,
        verbose_name='Товары',
        through='CartItem'
    )

    def __str__(self):
        return f'Корзина покупок #{self.user.user_id}'

    def total_price(self):
        total = sum(item.item.price * item.quantity for item in self.cart_items.all())
        return f'{intcomma(total)} ₽'

    class Meta:
        default_related_name = 'shopping_carts'
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'корзины покупок'

    total_price.short_description = 'Общая стоимость'


class CartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.title}"

    def total_price(self):
        return self.item.price * self.quantity

    class Meta:
        default_related_name = 'cart_items'
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'товары в корзине'
