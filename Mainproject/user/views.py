from rest_framework.viewsets import ReadOnlyModelViewSet,mixins
from .models import Donation,Patient,User
from .serializer import UserSerializer,PatientSerializer,DonatioSerializer
from rest_framework import mixins, viewsets,permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.


class CreateUser(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[permissions.IsAuthenticated]


class CreatPateint(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes=[permissions.IsAuthenticated]


class CreateDonation(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonatioSerializer
    permission_classes=[permissions.IsAuthenticated]


class ListUser(ReadOnlyModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class ListPateinds(ReadOnlyModelViewSet):
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer


class listDonation(ReadOnlyModelViewSet):
    queryset=Donation.objects.all()
    serializer_class=DonatioSerializer
    filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields=['patient','donor']
    search_fields = ['message']
    ordering_fields = ['date', 'amount']


class UpdateUser(mixins.ListModelMixin  ,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]


class UpdatePaitent(mixins.ListModelMixin,mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = PatientSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        return Patient.objects.filter(is_completed=False)
    

class CompletedPatients(ReadOnlyModelViewSet):
    serializer_class=PatientSerializer
    def get_queryset(self):
        return Patient.objects.filter(is_completed=True)
    
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_fields=['name']
    search_fields = ['name']



    
    
class DelUser(mixins.ListModelMixin,mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]