from django.contrib import admin

from bot.models import CartItem, Category, Item, ShoppingCart, TelegramUser
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'first_name',
        'last_name',
        'username',
        'created_at'
    )
    search_fields = (
        'user_id',
        'first_name',
        'last_name',
        'username',
    )
    readonly_fields = (
        'user_id',
        'first_name',
        'last_name',
        'username',
        'created_at'
    )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'color',
        'category',
        'subcategory',
        'image_tag',
        'description',
        'price_view'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'count'
    )

    @admin.display(description='Количество товаров')
    def count(self, category):
        return category.items.count()

    class CategoryItemsInline(admin.TabularInline):
        model = Item
        extra = 0

    inlines = [CategoryItemsInline]


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'items_count',
        'total_count',
        'total_price',
    )
    readonly_fields = (
        'total_price',
    )

    @admin.display(description='Общее число товаров')
    def total_count(self, shopping_cart: ShoppingCart):
        return sum(item.quantity for item in shopping_cart.cart_items.all())

    @admin.display(description='Количество позиций')
    def items_count(self, shopping_cart: ShoppingCart):
        return shopping_cart.items.count()

    class CartItemInline(admin.TabularInline):
        model = CartItem
        extra = 0

    inlines = [CartItemInline]
