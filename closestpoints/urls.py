from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("points/", views.PointsList.as_view(), name="list"),
    path("points/<int:pk>/", views.PointsDetail.as_view(), name="detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)