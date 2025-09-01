from django.contrib import admin
from .models import Odam

@admin.register(Odam)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "username", "birthday")   # admin jadvalda ko‘rinadigan ustunlar
    search_fields = ("name", "username", "phone")              # qidirish uchun fieldlar
    list_filter = ("birthday",)                                # filter uchun
