from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

User = get_user_model()


def pagination_processing(self, queries_annotate):
    objects_per_page = self.paginate_by
    queryset = queries_annotate.order_by("created_at")
    paginator = Paginator(queryset, objects_per_page)
    page = self.request.GET.get("page")

    return paginator, page


def paginate_by_condition(paginator, page):
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    return paginated_queryset
