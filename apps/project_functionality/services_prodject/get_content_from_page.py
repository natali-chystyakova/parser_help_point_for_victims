import asyncio

import bs4

from apps.project_functionality.services_prodject.make_request import make_request
from apps.project_functionality.services_prodject.typings import T_TEXT


# https://kustdnipro.com/ru/gyd-dlya-pereselentsev-bolee-polnogo-v-gorode-net/


# <article class="cust-article city-article ">


def parse_page__site__kust(soup: bs4.BeautifulSoup):
    """
    Парсит страницу и возвращает список категорий с вложенными пунктами помощи.
    """
    # Найти главную статью
    article = soup.find("article", class_="cust-article city-article")
    if not article:
        return []  # Если статья не найдена, вернуть пустой список

    # Найти все заголовки секций <h4 class="wp-block-heading">
    section_headers = article.find_all("h4", class_="wp-block-heading")
    sections = []

    for header in section_headers:
        # Создать новую секцию с её заголовком
        section_data = {"category": header.get_text(strip=True), "items": []}

        # Собрать все элементы до следующего заголовка
        current_element = header.find_next_sibling()
        temp_item = []  # Временный список для одного пункта помощи

        while current_element and current_element.name != "h4":
            if current_element.name == "p":
                # Если текущий элемент содержит <strong>, это начало нового пункта помощи
                strong_tag = current_element.find("strong")
                if strong_tag:
                    # Если temp_item не пустой, завершить предыдущий пункт
                    if temp_item:
                        section_data["items"].append(temp_item)
                        temp_item = []

                    # Добавить название нового пункта
                    temp_item.append(strong_tag.get_text(strip=True))

                else:
                    # Если <strong> нет, добавить текст к текущему пункту
                    text = current_element.get_text(strip=True)
                    if text:
                        temp_item.append(text)

                # Проверить наличие ссылок и добавить их
                link = current_element.find("a")
                if link:
                    href = link.get("href")
                    if href:
                        temp_item.append(href)

            current_element = current_element.find_next_sibling()

        # Добавить последний пункт помощи, если он не пустой
        if temp_item:
            section_data["items"].append(temp_item)

        sections.append(section_data)

    return sections


# 2 вариант только для категорий( пункты помощи - по параграфам)
# def parse_page__site__kust(soup: bs4.BeautifulSoup):
#     """
#     Парсит страницу и возвращает список секций (категорий).
#     """
#     # Найти главную статью
#     article = soup.find("article", class_="cust-article city-article")
#     if not article:
#         return []  # Если статья не найдена, вернуть пустой список
#
#     # Найти все заголовки секций <h4 class="wp-block-heading">
#     section_headers = article.find_all("h4", class_="wp-block-heading")
#     sections = []
#
#     for header in section_headers:
#         # Создать новую секцию с её заголовком
#         section_data = {"category": header.get_text(strip=True), "items": []}
#
#         # Собрать все элементы до следующего заголовка
#         current_element = header.find_next_sibling()
#         while current_element and current_element.name != "h4":
#             if current_element.name == "p":
#                 text = current_element.get_text(strip=True)
#                 if text:
#                     section_data["items"].append(text)
#
#                 # Проверить наличие ссылок
#                 link = current_element.find("a")
#                 if link:
#                     href = link.get("href")
#                     if href:
#                         section_data["items"].append(href)
#
#             current_element = current_element.find_next_sibling()
#
#         sections.append(section_data)
#
#     return sections  #тут словарь


# 1 вариант для списка и пунктов помощи
# def parse_page__site__kust(soup: bs4.BeautifulSoup):
#     # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#navigating-the-tree
#     article = soup.find("article", class_="cust-article city-article")
#
#     is_found_section = False
#
#     contact_data_list = []
#
#     is_found_contact_data = False
#     temp_item_lines = []
#     for element in article.children:
#         # If element is H4
#         if element.name == "h4"and element.text == "ІV. Соціальні виплати":
#         #if element.name == "h4" and element.text == "ІІ. Одяг":
#             is_found_section = True
#
#         if is_found_section:
#             if is_found_contact_data:
#                 if element.name == "p":
#                     # Check about e
#                     # and of contact data
#                     if tag_a := element.find("a"):
#                         href = tag_a.get("href")
#
#                         temp_item_lines.append(href)
#                         contact_data_list.append(temp_item_lines)
#                         temp_item_lines = []
#                         is_found_contact_data = False
#                         continue
#
#                 temp_item_lines.append(element.text)
#
#             elif element.name == "p":
#                 if element.find("strong"):
#                     is_found_contact_data = True
#                     temp_item_lines.append(element.text)
#
#     if temp_item_lines:
#         contact_data_list.append(temp_item_lines)
#
#     return contact_data_list


def get_data_from_page(text: T_TEXT):
    soup = bs4.BeautifulSoup(markup=text, features="html.parser")

    return parse_page__site__kust(soup=soup)


async def main():
    # url = "https://kustdnipro.com/ru/gyd-dlya-pereselentsev-bolee-polnogo-v-gorode-net/"
    url = "https://kustdnipro.com/gid-dlya-pereselentsiv-povnishogo-u-misti-nemaye/"

    page__text = await make_request(url=url)

    data_from_page = get_data_from_page(text=page__text)

    # for item in data_from_page:
    #     print(item)
    #
    #     return item
    print(data_from_page)
    return data_from_page


def get_some_content_from_page_main():
    data = asyncio.run(main())
    # for elem in data:
    #     return elem
    return data


# import bs4
# from typing import List, Dict
# from apps.project_functionality.services_prodject.make_request import make_request
#
# def parse_page_sections(soup: bs4.BeautifulSoup) -> List[Dict[str, List]]:
#     sections = []
#     current_section = None
#     for element in soup.find_all(["h4", "p"]):  # Ищем только <h4> и <p>
#         if element.name == "h4" and "wp-block-heading" in element.get("class", []):
#             # Это начало новой секции
#             if current_section:
#                 sections.append(current_section)  # Добавляем предыдущую секцию
#             current_section = {
#                 "category": element.text.strip(),  # Имя секции
#                 "items": []  # Список для элементов
#             }
#         elif current_section and element.name == "p":
#             # Это элемент внутри текущей секции
#             if element.find("strong"):
#                 # Это заголовок элемента
#                 current_section["items"].append({
#                     "name": element.text.strip(),
#                     "information": []
#                 })
#             elif current_section["items"]:
#                 # Это дополнительная информация к последнему элементу
#                 current_section["items"][-1]["information"].append(element.text.strip())
#
#     if current_section:
#         sections.append(current_section)  # Добавляем последнюю секцию
#     return sections
#
#
# async def main():
#     url = "https://kustdnipro.com/ru/gyd-dlya-pereselentsev-bolee-polnogo-v-gorode-net/"
#     page__text = await make_request(url=url)
#     soup = bs4.BeautifulSoup(page__text, features="html.parser")
#
#     sections_data = parse_page_sections(soup)
#     return sections_data
#
#
# def get_some_content_from_page_main():
#     import asyncio
#     data = asyncio.run(main())
#     return data
