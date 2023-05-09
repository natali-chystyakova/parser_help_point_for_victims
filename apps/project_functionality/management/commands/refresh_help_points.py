import logging
from django.core.management.base import BaseCommand
from django.template.defaultfilters import linebreaksbr

from apps.project_functionality.models import HelpPoint
from apps.project_functionality.services_prodject.get_content_from_page import get_some_content_from_page_main


class Command(BaseCommand):
    help = "Refreshes help points by fetching data from a remote source and updating the database."

    def handle(self, *args, **options):
        logger = logging.getLogger("django")
        queryset = HelpPoint.objects.all()
        logger.info(f"Current amount of contacts before: {queryset.count()}")

        for data in get_some_content_from_page_main():
            HelpPoint.objects.update_or_create(information=linebreaksbr("\n".join(data)), name=data[0])

        logger.info(f"Current amount of contacts after: {HelpPoint.objects.count()}")
