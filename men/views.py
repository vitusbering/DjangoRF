from rest_framework import generics
from django.shortcuts import render
from django.forms import model_to_dict
from .models import Men, Category
from .serializers import MenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework. decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters





# Create your views here.
# class MenAPIView(generics.ListAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer


class MenAPIListPagination(PageNumberPagination): # Base class
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


class MenAPIList(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = MenAPIListPagination
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['cat','title']
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', 'content']
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['title', 'content', 'cat']


class MenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)


class MenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer
    permission_classes = (IsAdminOrReadOnly, )



# class MenViewSet(viewsets.ModelViewSet):
#     # queryset = Men.objects.all()
#     serializer_class = MenSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Men.objects.all()[:5]
#
#         return Men.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cat = Category.objects.get(pk=pk)
#         return Response({'cat':[cat.name]})


# class MenAPIList(generics.ListCreateAPIView):
#     queryset = Men.objects.all()
#     serializer_class = MenSerializer
#
# class MenAPIUpdate(generics.UpdateAPIView):
#     qureyset = Men.objects.all()
#     serializer_class = MenSerializer
#
# class MenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     # lookup_url_kwarg = "pk"
#     # qureyset = Men.objects.all()
#     serializer_class = MenSerializer
#
    # def get_queryset(self):
    #     return(Men.objects.all())



# class MenAPIView(APIView): # class Response transforms dictionary to json
#
#     def get(self, request):
#         m = Men.objects.all()
#         return Response({'posts': MenSerializer(m, many=True).data})
#
#     def post(self, request):
#         serializer = MenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

        # post_new = Men.objects.create(
        #     title=request.data['title'],
        #     content=request.data['content'],
        #     cat_id=request.data['cat_id']
        # )
        # return Response({'post':model_to_dict(post_new)}) #return added information
        # return Response({'post': MenSerializer(post_new).data})
        # return Response({'post': serializer.data})

    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method PUT is not allowed"})
    #
    #     try:
    #         instance = Men.objects.get(pk=pk)
    #     except:
    #         return Response({"error": "Can not add. Object does not exist"})
    #
    #     serializer = MenSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({"post": serializer.data})
    #
    #
    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error": "Method Delete is not allowed"})
    #
    #     else:
    #         try:
    #             instance = Men.objects.get(pk=pk)
    #             instance.delete()
    #         except:
    #             return Response({"error": "Can not delete. Object does not exist"})
    #
    #     return Response({"post": "Post was deleted successfully"})
    #


        # serializer = MenSerializer(data=request.data, instance=instance)
        # serializer.is_valid(raise_exception=True)
        # serializer.delete()
        # return Response({"post": "delete post"})




