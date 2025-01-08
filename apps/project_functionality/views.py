from django.core.paginator import Paginator
from django.db.models import Count
from django.views.generic import ListView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from apps.project_functionality.forms import ContactForm
from apps.project_functionality.models import HelpPoint, Section
from apps.project_functionality.tools import paginate_by_condition

from django.shortcuts import redirect


class HelpPointListView(ListView):
    model = HelpPoint
    paginate_by = 5
    template_name = "project_functionality/helppoint_list.html"

    queryset = HelpPoint.objects.all().order_by("created_at").select_related("sect")

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
        context["cat_selected"] = 0
        context["sections"] = Section.objects.all()

        return context


class HelpPointUpdateView(UpdateView):
    model = HelpPoint
    fields = (
        "name",
        "address",
        "phone",
        "link",
    )
    success_url = reverse_lazy("project_functionality:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sections"] = Section.objects.all()
        context["cat_selected"] = self.kwargs.get("sect_id", 0)

        return context


class HelpPointDeleteView(DeleteView):
    model = HelpPoint

    success_url = reverse_lazy("project_functionality:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sections"] = Section.objects.all()
        context["cat_selected"] = self.kwargs.get("sect_id", 0)

        return context


class SectionListView(ListView):
    model = Section
    template_name = "project_functionality/section_list.html"

    queryset = Section.objects.all().order_by("created_at")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data["title"] = "Section"

        return context_data


class ShowSectionListView(ListView):
    model = HelpPoint

    template_name = "project_functionality/list.html"
    allow_empty = False  # появление ошибки 404, что страника не найдена
    # context_object_name = 'points_filter'

    def get_queryset(self):
        sect_id = self.kwargs.get("sect_id")  # Получаем ID категории из URL
        return HelpPoint.objects.filter(sect_id=sect_id).order_by("created_at").select_related("sect")

    def get_context_data(self, object_list=None, **kwargs):
        # Получаем базовый контекст
        context = super().get_context_data(**kwargs)

        # Добавляем данные секции в контекст
        context["sections"] = Section.objects.all()

        context["cat_selected"] = self.kwargs.get("sect_id", 0)
        context["title"] = "Категория"

        return context


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "project_functionality/contact.html"
    success_url = reverse_lazy("project_functionality:list")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Зворотнiй зв'язок"
        context["sections"] = Section.objects.all()
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect("project_functionality:list")
