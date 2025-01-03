import logging
from celery import shared_task

from apps.project_functionality.models import HelpPoint, Section
from apps.project_functionality.services_prodject.get_content_from_page import get_some_content_from_page_main


@shared_task
def refresh_help_points_task():
    # logger = logging.getLogger("django")
    # queryset = HelpPoint.objects.all()
    # logger.info(f"Current amount of contacts before: {queryset.count()}")
    #
    # for data in get_some_content_from_page_main():
    #     # HelpPoint.objects.update_or_create(information=linebreaksbr("\n".join(data)), name=data[0])
    #     HelpPoint.objects.update_or_create(
    #         name=data[0],  # Поле поиска (name)
    #         defaults={"information": linebreaksbr("\n".join(data))},  # Поле для обновления или создания (information)
    #     )
    # logger.info(f"Current amount of contacts after: {HelpPoint.objects.count()}")

    # вариант 5

    logger = logging.getLogger("django")
    queryset = HelpPoint.objects.all()
    logger.info(f"Current amount of contacts before: {queryset.count()}")

    parsed_data = get_some_content_from_page_main()

    for section_data in parsed_data:
        category_name = section_data["category"]  # Название секции
        items = section_data["items"]  # Список пунктов помощи в секции

        # Сохранить или обновить секцию
        section_obj, created = Section.objects.get_or_create(
            name_section=category_name,
            defaults={"description": f"Описание для категории {category_name}"},
            # Можно добавить описание, если нужно
        )

        for item in items:
            HelpPoint.objects.update_or_create(
                information=item,
                name=item[0],  # Поле поиска (name)
                section=section_obj,
            )
    logger.info(f"Current amount of contacts after: {HelpPoint.objects.count()}")

    # full_information = "\n".join(items).strip()  # Объединяем все параграфы,
    #
    # if full_information:  # Проверяем, что есть информация для записи
    #         HelpPoint.objects.update_or_create(
    #             information=full_information,
    #             defaults={
    #                 "name": category_name,  # Привязка категории как имя
    #                 "section": section_obj,  # Секция, к которой привязан пункт
    #             },
    #         )

    # logger.info(f"Current amount of contacts after: {HelpPoint.objects.count()}")
