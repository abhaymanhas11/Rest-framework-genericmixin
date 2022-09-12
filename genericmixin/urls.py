from django.urls import path
from .import views

urlpatterns=[
    #this url is working one by one list and one pk url can run combine
    path('studentapi/',views.studentlistcreate.as_view()),
    path('studentapi/<int:pk>', views.studentretrieveupdatedestroy.as_view()),

]