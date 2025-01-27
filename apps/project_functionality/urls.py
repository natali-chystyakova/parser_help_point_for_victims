from django.urls import path
from . import views

# from django.urls import include
from django.contrib.auth.decorators import login_required


from .views import DistanceToAllPointsAPIView, HelpPointMapView

app_name = "project_functionality"

urlpatterns = [
    path("list/", views.HelpPointListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.HelpPointDetailView.as_view(), name="helppoint_detail"),
    path("update/<int:pk>/", login_required(views.HelpPointUpdateView.as_view()), name="update"),
    path("delete/<int:pk>/", login_required(views.HelpPointDeleteView.as_view()), name="delete"),
    path("contact/", views.ContactFormView.as_view(), name="contact"),
    path("sections/<int:sect_id>/", views.ShowSectionListView.as_view(), name="section"),
    path("sections/", views.SectionListView.as_view(), name="sections_list"),
    # path('sections/<int:sect_id>/', show_section, name='section'),
    path("section/<int:pk>/", views.SectionDetailView.as_view(), name="section_detail"),
    path("list/<int:pk>/map/", HelpPointMapView.as_view(), name="help_point_map"),
    path("list/distances/", DistanceToAllPointsAPIView.as_view(), name="distances"),
    # path("__debug__/", include("debug_toolbar.urls")),
]
