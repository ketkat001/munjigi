from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .serializers import HeritageSerializer, HeritageDetailSerializer
from .models import Heritage
from backend.pagination import CustomPagination
from django.db.models import Count
from accounts.models import User


class HeritageListAPI(GenericAPIView):
    serializer_class = HeritageSerializer
    queryset = Heritage.objects.all()
    pagination_class = CustomPagination
    def get(self, request):
        sort = request.GET.get('sort','')
        if sort == 'likes':
            queryset = Heritage.objects.annotate(like_count=Count('like_users')).order_by('-like_count')
        else:
            queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializer.data)
            data = result.data # pagination data
        else:
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
        payload = {
            'return_code': '0000',
            'return_message': 'Success',
            'data': data
        }
        return Response(data)


class HeritageDetailAPI(generics.GenericAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageDetailSerializer

    def get(self ,request, pk):

        heritage = get_object_or_404(Heritage, pk=pk)
        if request.session.get("h_hit", False) == False:
            request.session["h_hit"] = []
        hit_l = request.session["h_hit"]
        if pk not in hit_l:
            hit_l.append(pk)
            request.session["h_hit"] = hit_l
            heritage.hit += 1
        
        h_data = HeritageDetailSerializer(heritage).data
        serializer = HeritageDetailSerializer(heritage, data = h_data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.data)



class HeritageLikeAPI(generics.GenericAPIView):
    queryset = Heritage.objects.all()
    serializer_class = HeritageDetailSerializer
    permissions_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        heritage = get_object_or_404(Heritage, pk=pk)
        user = User.objects.get(id=request.data['userDataId'])
        if user in heritage.like_users.all():
            heritage.like_users.remove(user)
        else:
            heritage.like_users.add(user)
        serializer = HeritageDetailSerializer(heritage)
        return Response(serializer.data)