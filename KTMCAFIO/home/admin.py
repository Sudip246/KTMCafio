from django.contrib import admin
from .models import *

admin.site.site_header = "KTM_CAFIO | Admin"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", 'email', 'message')
    list_filter = ("name", "subject",)
    search_fields = ("email", "name")


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('address', "email")
    list_filter = ("phone", "email",)
    search_fields = ("email", "address")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "description")
    list_filter = ("title", "icon")
    search_fields = ("name",)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title","image", "description")
    list_filter = ("title","description")
    search_fields = ("title",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "image")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "image","profession", "description", "star_rating")
    list_filter = ("name", "profession", "star_rating")
    search_fields = ("name","profession")


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(MenuItemImage)
class MenuItemImageAdmin(admin.ModelAdmin):
    list_display = ("slug", "image", "category")
    list_filter = ("slug", "category")
    search_fields = ("category", "slug")


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "description")
    list_filter = ("name", "slug", "category")
    search_fields = ("name", "slug")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("username", "slug", "quantity", "total", "checkout")
    list_filter = ("checkout", "date")
    search_fields = ("username", "slug")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "fname", 'lname', "email", "phone", "address","status" )
    list_filter = ("email", "phone", "city")
    search_fields =("email", "phone", "city")

