from .models import Points
from .serializers import PointsSerialzer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def closest(points, K):
    points.sort(key=lambda K: K[0] ** 2 + K[1] ** 2)

    return points[:K]


# Create your views here.
class PointsList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        points = Points.objects.all()
        serializer = PointsSerialzer(points, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user_input = request.data
        list_csp = [user_input]
        res = [eval(str(ele)) for ele in list_csp]
        empty_list = []
        for item in res:
            for it in item:
                empty_list.append(it)

        output = closest(empty_list, 1)
        data = {"input": user_input, "output": str(output)}
        serializer = PointsSerialzer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PointsDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Points.objects.get(pk=pk)
        except Points.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        point = self.get_object(pk)
        serializer = PointsSerialzer(point)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        point = self.get_object(pk)
        serializer = PointsSerialzer(point, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        point = self.get_object(pk)
        point.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
