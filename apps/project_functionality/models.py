from django.db import models
from django.urls import reverse

# class Url(models.Model):
#     url = models.CharField(max_length=100)
#     address = models.CharField(max_length=100, default=None, null=True, blank=True)
#     phone = models.CharField(max_length=100, default=None, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)


class Section(models.Model):
    name_section = models.CharField(max_length=255)  # Название секции (например, "Одежда")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_section

    def get_absolute_url(self):
        return reverse("project_functionality:section", kwargs={"sect_id": self.pk})

    class Meta:
        ordering = ["pk"]
        verbose_name = "section for points"
        verbose_name_plural = "sections for points"


class HelpPoint(models.Model):
    name = models.TextField(default=None, null=True, blank=True)
    information = models.TextField(default=None, null=True, blank=True, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sect = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name="helppoints",
        default=None,
        null=True,
        blank=True,
    )  # Связь с секцией

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.name}"

    __repr__ = __str__

    # def get_absolute_url(self):
    #     return reverse('project_functionality:list', kwargs={'sect': self.sect})
