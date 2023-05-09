from django.core.paginator import Paginator
from django.db.models import Count
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.project_functionality.models import HelpPoint
from apps.project_functionality.tools import paginate_by_condition


class HelpPointListView(ListView):
    model = HelpPoint
    paginate_by = 5
    template_name = "project_functionality/helppoint_list.html"

    queryset = HelpPoint.objects.all().order_by("created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queries_annotate_all = HelpPoint.objects.all().annotate(count=Count("id"))
        count_all_logs = HelpPoint.objects.count()

        objects_per_page = self.paginate_by
        queryset = queries_annotate_all.order_by("created_at")
        paginator = Paginator(queryset, objects_per_page)
        page = self.request.GET.get("page")

        paginated_queryset = paginate_by_condition(paginator, page)

        context["title"] = "Helppoint List"
        context["count_all_logs"] = count_all_logs
        context["queries_annotate_all"] = queries_annotate_all
        context["paginated_queryset"] = paginated_queryset
        context["page_obj"] = paginated_queryset

        return context


class HelpPointUpdateView(UpdateView):
    model = HelpPoint
    fields = (
        "name",
        "information",
    )
    success_url = reverse_lazy("project_functionality:list")


class HelpPointDeleteView(DeleteView):
    model = HelpPoint

    success_url = reverse_lazy("project_functionality:list")
