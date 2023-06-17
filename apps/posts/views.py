from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer

class PostAPIViewSet(GenericViewSet, 
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer