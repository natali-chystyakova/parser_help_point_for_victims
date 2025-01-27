# from django.shortcuts import render
# from celery.result import AsyncResult
# from django.views.generic import TemplateView


# class CeleryView(TemplateView):
#     template_name = "celery_for_parser/index.html"
#
#     def get_context_data(self, **kwargs):
#         context_data = super().get_context_data(**kwargs)
#
#         result: AsyncResult = example_1.delay("Hello, world!")
#
#         context_data["result_id"] = result.id
#
#         return context_data


from celery.result import AsyncResult
from django.views.generic import TemplateView
from apps.celery_for_parser.tasks.refresh_help_points_task import refresh_help_points_task
from apps.project_functionality.models import Section


class CeleryView(TemplateView):
    template_name = "celery_for_parser/index.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        result: AsyncResult = refresh_help_points_task.delay()
        context_data["result_id"] = result.id
        # Добавляем секции и выбранную категорию
        context_data["sections"] = Section.objects.all()
        context_data["cat_selected"] = None  # Или вычислить выбранную категорию
        return context_data
