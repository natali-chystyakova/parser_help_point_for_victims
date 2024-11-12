import logging
from celery import shared_task
from django.template.defaultfilters import linebreaksbr
from apps.project_functionality.models import HelpPoint
from apps.project_functionality.services_prodject.get_content_from_page import get_some_content_from_page_main


@shared_task
def refresh_help_points_task():
    logger = logging.getLogger("django")
    queryset = HelpPoint.objects.all()
    logger.info(f"Current amount of contacts before: {queryset.count()}")

    for data in get_some_content_from_page_main():
        # HelpPoint.objects.update_or_create(information=linebreaksbr("\n".join(data)), name=data[0])
        HelpPoint.objects.update_or_create(
            name=data[0],  # Поле поиска (name)
            defaults={"information": linebreaksbr("\n".join(data))},  # Поле для обновления или создания (information)
        )
    logger.info(f"Current amount of contacts after: {HelpPoint.objects.count()}")


# import uuid
# from celery import shared_task
# from django.core.cache import cache  # Используем Django-кеш для хранения ID
# import logging
# from apps.project_functionality.models import HelpPoint
# from django.template.defaultfilters import linebreaksbr
# from django.db.utils import IntegrityError
# #from django.utils.html import linebreaksbr
# from apps.project_functionality.services_prodject.get_content_from_page import get_some_content_from_page_main
#
#
# @shared_task
# def refresh_help_points_task():
#     logger = logging.getLogger("django")
#
#     # Создаем уникальный ID для этого запуска задачи
#     id_ = str(uuid.uuid4())
#     task_key = f"refresh_help_points_task_{id_}"
#
#     # Проверяем, выполняется ли уже такая задача
#     if cache.get(task_key):
#         logger.info(f"Task with id {id_} is already running. Skipping.")
#         return  # Прерываем задачу, если она уже активна
#
#     # Устанавливаем флаг, что задача запущена
#     cache.set(task_key, True, timeout=300)  # Устанавливаем тайм-аут, например, 5 минут
#
#     try:
#         # Логируем количество записей до обновления
#         queryset = HelpPoint.objects.all()
#         logger.info(f"Current amount of contacts before: {queryset.count()}")
#
#         # Обновляем или создаем записи
#         # for data in get_some_content_from_page_main():
#         #     HelpPoint.objects.update_or_create(
#         #         information=linebreaksbr("\n".join(data)),
#         #         name=data[0]
#         #     )
#
#         for data in get_some_content_from_page_main():
#             try:
#                 HelpPoint.objects.update_or_create(
#                     name=data[0],
#                     defaults={"information": linebreaksbr("\n".join(data))}
#                 )
#             except IntegrityError:
#                 logger.warning(f"Skipped duplicate entry for {data[0]}")
#
#
#         # Логируем количество записей после обновления
#         logger.info(f"Current amount of contacts after: {HelpPoint.objects.count()}")
#
#     finally:
#         # Убираем флаг после завершения задачи
#         cache.delete(task_key)
