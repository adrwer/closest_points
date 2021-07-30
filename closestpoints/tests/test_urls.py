from django.test import SimpleTestCase
from django.urls import reverse, resolve
from closestpoints.views import PointsList, PointsDetail


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse("list")
        self.assertEquals(resolve(url).func.view_class, PointsList)

    def test_detail_url_resolves(self):
        url = reverse("detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, PointsDetail)