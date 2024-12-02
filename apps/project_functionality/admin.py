from django.contrib import admin
from . import models


# admin.site.register(models.Contact)


@admin.register(models.HelpPoint)
class HelpPointAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "information",
        "section",
        "created_at",
    )


class ContactInline(admin.TabularInline):
    model = models.HelpPoint


@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        "name_section",
        "created_at",
    )
    # list_filter = ("name",)
    inlines = (ContactInline,)
