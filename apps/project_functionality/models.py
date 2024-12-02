from django.db import models


# class Url(models.Model):
#     url = models.CharField(max_length=100)
#     address = models.CharField(max_length=100, default=None, null=True, blank=True)
#     phone = models.CharField(max_length=100, default=None, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)


class Section(models.Model):
    name_section = models.CharField(max_length=255)  # Название секции (например, "Одежда")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_section


class HelpPoint(models.Model):
    name = models.TextField(default=None, null=True, blank=True)
    information = models.TextField(default=None, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="helppoints",
        default=None,
        null=True,
        blank=True,
    )  # Связь с секцией

    def __str__(self) -> str:
        return f"{self.information}"

    __repr__ = __str__
