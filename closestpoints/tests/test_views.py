from django.test import TestCase, Client
from django.urls import reverse
from closestpoints.models import Points
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.points1 = Points.objects.create(
            input="(2, 3),(12, 30),(40, 50),(5, 1),(12, 10),(3, 4)",
            output="[(2, 3)]"
        )

    def test_points_list_POST(self):
        url = reverse("list")
        response = self.client.post(url, {
            "input": "(2, 4),(12, 20),(30, 50),(3, 1),(11, 10),(3, 4)",
            "output": "[(3, 1)]"
        })

        points2 = Points.objects.get(id=2)
        self.assertEquals(points2.input, "(2, 4),(12, 20),(30, 50),(3, 1),(11, 10),(3, 4)")
        self.assertEquals(points2.output, "[(3, 1)]")