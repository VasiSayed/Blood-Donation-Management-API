from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CreateUser,CreateDonation,CreatPateint,ListUser,listDonation,ListPateinds,UpdateUser,DelUser,CompletedPatients,UpdatePaitent

router=DefaultRouter()
router.register(r'View-user',ListUser,basename='View-user'),
router.register(r'View-donation',listDonation,basename='View-donors'),
router.register(r'View-patients',ListPateinds,basename='View-patients'),
router.register(r'View-completed-patient',CompletedPatients,basename='Completed-Paitent'),
router.register(r'Create-user',CreateUser),
router.register(r'Create-donation',CreateDonation,basename='Create-donation'),
router.register(r'Create-patient',CreatPateint,basename='Create-Paitent'),
router.register(r'update-user',UpdateUser,basename='update-User'),
router.register(r'update-patient', UpdatePaitent, basename='update-patient'),
router.register(r'delete-user',DelUser,basename='Delete-User'),

urlpatterns = [
    path('',include(router.urls)),
]