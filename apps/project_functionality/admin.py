from django.contrib import admin
from . import models


# admin.site.register(models.Contact)


@admin.register(models.HelpPoint)
class HelpPointAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "address",
        "phone",
        "link",
        # "information",
        "sect",
        "created_at",
    )
    list_display_links = (
        "id",
        "name",
    )
    search_fields = (
        "name",
        "address",
        "phone",
    )
    list_filter = ("created_at",)


class ContactInline(admin.TabularInline):
    model = models.HelpPoint


@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name_section",
        "created_at",
    )
    list_display_links = (
        "pk",
        "name_section",
    )
    search_fields = ("name_section",)
    # list_filter = ("name",)
    inlines = (ContactInline,)
