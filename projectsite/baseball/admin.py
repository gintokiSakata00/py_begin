from django.contrib import admin
from django.contrib.admin import display
from .models import Position, Person, Club, Play

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("description",)
    search_fields = ("description",)

@admin.register(Person)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","height","weight")
    search_fields = ("firstname","lastname","height","weight")


@admin.register(Club)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name","coach","dorm_latitude","dorm_longhitude")
    search_fields = ("name","coach","dorm_latitude","dorm_longhitude")

@admin.register(Play)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("player","team","string_no","pos")
    list_display = ("player","team","string_no","pos")
