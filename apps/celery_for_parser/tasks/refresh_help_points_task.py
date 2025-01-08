import logging
from celery import shared_task
from apps.project_functionality.models import HelpPoint, Section
from apps.project_functionality.services_prodject.get_content_from_page import get_some_content_from_page_main

# from django.db import models


import re

MAX_URL_LENGTH = 200


def extract_address(text):
    # Простая логика: ищем строки, начинающиеся с "Адрес"
    match = re.search(r"(?:Адрес|Address):?\s*(.+)", text, re.IGNORECASE)
    return match.group(1) if match else None


def extract_phone(text):
    # Регулярное выражение для поиска телефонных номеров
    phone_pattern = r"\+?\d{1,4}\s?\(?\d{2,4}\)?[\s\-]?\d{2,4}[\s\-]?\d{2,4}"

    # Найти все совпадения
    match = re.findall(phone_pattern, text)

    # Удалить "номера", которые являются частью ссылок или не соответствуют длине
    valid_numbers = [
        num
        for num in match
        if len(re.sub(r"\D", "", num)) >= 10  # Номер должен содержать >= 10 цифр
        and not re.search(r"https?://", text)  # Исключить строки, содержащие URL
    ]

    # Возвращаем объединенные номера или None, если ничего не найдено
    return "; ".join(valid_numbers) if valid_numbers else None


def extract_link(text):
    # Ищем URL-адреса
    match = re.search(r"https?://[^\s]+", text)
    return match.group(0) if match else None


@shared_task
def refresh_help_points_task():
    logger = logging.getLogger("django")
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
            name = item[0]
            information_list = item[1:]  # Это список, каждый элемент нужно проверить

            # дописывали дубликаты, когда была ошибка дублирования
            #             duplicates = (
            #                 HelpPoint.objects.values('name')
            #                 .annotate(count=models.Count('id'))
            #                 .filter(count__gt=1)
            #             )
            #
            #             for duplicate in duplicates:
            #                 objs = HelpPoint.objects.filter(name=duplicate['name'])
            #                 for i, obj in enumerate(objs):
            #                     obj.name = f"{obj.name}_{i}"
            #                     obj.save()
            #     else:
            #         # Логирование, если объект пропущен
            #         logger.info(f"Skipped object: {name} (No address, phone, or link found)")

            # Переменные для хранения найденных данных
            addresses, phones, links = [], [], []

            # Перебираем элементы списка и собираем данные
            for info in information_list:
                address = extract_address(info)
                phone = extract_phone(info)
                link = extract_link(info)

                if address and address not in addresses:
                    addresses.append(address)
                if phone and phone not in phones:
                    phones.append(phone)
                if link and link not in links:
                    links.append(link)

            # Объединяем данные в строки (или сохраняем как списки, если требуется)
            combined_address = "; ".join(addresses)
            combined_phone = "; ".join(phones)
            combined_link = "; ".join(links)

            # Убедитесь, что объект содержит хотя бы одно значение в адресе, телефоне или ссылке
            if combined_address or combined_phone or combined_link:
                # Проверяем, что name отличается от извлеченных данных
                if name != combined_address and name != combined_phone and name != combined_link:
                    # Сохраняем объект в базе данных
                    HelpPoint.objects.update_or_create(
                        name=name,
                        sect=section_obj,
                        defaults={
                            "address": combined_address,
                            "phone": combined_phone,
                            "link": combined_link,
                        },
                    )
            else:
                # Логирование, если объект пропущен
                logger.info(f"Skipped object: {name} (No address, phone, or link found)")
