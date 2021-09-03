from rest_framework import generics, permissions, views, response
from .models import Follower
from azsite.az.src.profiles.models import UserNet
from .serializer import  ListFollowerSerializer

class ListFollowerView(generics.ListAPIView):


    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ListFollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class AddFollowerView(views.APIView):


    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):

        user = UserNet.objects.filter(id=pk)
        if user.exists():
            Follower.objects.create(subscriber=request.user, user=user)
            return response.Response(status=201)
        return response.Response(status=404)
