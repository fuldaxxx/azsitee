from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer


class UserNetPublicView(ModelViewSet):
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]


class UpdateUserNetView(ModelViewSet):
    ''' Редактирвание пользовтаелья'''

    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)


