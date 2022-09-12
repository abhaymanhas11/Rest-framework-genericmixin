from django.shortcuts import render
from .models import student
from .serializer import s_serializer
from rest_framework.generics import GenericAPIView
from  rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class studentlistcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = student.objects.all()
    serializer_class = s_serializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class studentretrieveupdatedestroy(GenericAPIView, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = student.objects.all()
    serializer_class = s_serializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




