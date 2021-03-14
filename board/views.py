from django.shortcuts import render, redirect
from django.core.serializers import serialize

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


# index
def index(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('account:login')

    return render(request, 'index.html')

"""
{
"title":"hello6",
"content":"hhhh",
"content_at":"20210221",
"use_yn":"Y"
}
"""
class PostView(APIView):

    # GET /board/
    # GET /board/{post_id}
    def get(self, request,  **kwargs):
        # list
        if kwargs.get('post_id') is None:
            post_queryset = Post.objects.all() #모든 Post의 정보를 불러온다.
            post_queryset_serializer = PostSerializer(post_queryset, many=True)
            return Response(post_queryset_serializer.data, status=status.HTTP_200_OK)
        # detail
        else:
            post_id = kwargs.get('post_id')
            post_serializer = PostSerializer(Post.objects.get(id=post_id)) #id에 해당하는 Post의 정보를 불러온다
            return Response(post_serializer.data, status=status.HTTP_200_OK)


    # PUT /post/
    def post(self, request):
        post_serializer = PostSerializer(data=request.data) #Request의 data를 PostSerializer로 변환

        if post_serializer.is_valid():
            post_serializer.save() #PostSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(post_serializer.data, status=status.HTTP_201_CREATED) #client에게 JSON response 전달
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # PUT /post/{post_id}
    def put(self, request, **kwargs):
        if kwargs.get('post_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            post_id = kwargs.get('post_id')
            post_object = Post.objects.get(id=post_id)
 
            update_post_serializer = PostSerializer(post_object, data=request.data)
            if update_post_serializer.is_valid():
                update_post_serializer.save()
                return Response(update_post_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
 

    # DELETE /post/{post_id}
    def delete(self, request, **kwargs):
        if kwargs.get('post_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            post_id = kwargs.get('post_id')
            post_object = Post.objects.get(id=post_id)
            post_object.delete()
            return Response("test ok", status=status.HTTP_200_OK)

"""
# index
def index2(request):

    if request.post.is_authenticated:
        pass
    else:
        return redirect('account:login')

    return render(request, 'index2.html')
"""