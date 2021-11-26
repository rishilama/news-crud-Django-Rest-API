from rest_framework import viewsets, response, status
from . import serializers, models as NewsModels
from rest_framework.generics import get_object_or_404

class NewsViewSets(viewsets.ViewSet):

    serializer_class = serializers.NewsViewSet
    queryset = NewsModels.News.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return response.Response(serializer.data)

    def create (self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        latestNews = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(latestNews)
        return response.Response (serializer.data)

    def update(self, request, pk=None):
        latestNews = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(latestNews, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def partial_update(self, request, pk=None):
        latestNews = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializers_class(latestNews, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    def destroy(self, request, pk=None):
        latestNews = get_object_or_404(self.queryset, pk=pk)
        latestNews.delete()
        return response.Response(status=status.HTTP_200_OK)