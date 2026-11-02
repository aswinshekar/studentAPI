from os import name

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views import View
from app.models import Student
from app import serializers

#API VIEW FOR READINFG ALL RECORD
#using django
# class StudentList(View):
#     def get(self, request):
#         # students = [
#         #     {
#         #         "id": 1,
#         #         "name": "Aswin",
#         #         "age": 21,
#         #         "course": "B.Tech CSE"
#         #     },
#         #     {
#         #         "id": 2,
#         #         "name": "Rahul",
#         #         "age": 22,
#         #         "course": "B.Tech CSE"
#         #     },
#         #     {
#         #         "id": 3,
#         #         "name": "Anu",
#         #         "age": 21,
#         #         "course": "B.Tech IT"
#         #     }
#         # ]
#         s=list(Student.objects.all().values())
#         print(s)
#         print(type(s))
#         # return JsonResponse
#         return JsonResponse(s, safe=False)
#USING DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import StudentSerializer
class StudentList(APIView):
    def get(selfself, request):
        # reads all employee records
        qs = Student.objects.all()  # DJANGO FORMAT QS
        # CONVERTS QUERYSET INTO PYTHON NATIVE USING SERIALIZER
        serializer_instance =StudentSerializer(qs,many=True)
        # RETURNS RESPONSE AS JSON USING RESPONSE FUNTION
        # print(serializer_instance.data)
        return Response(serializer_instance.data)

#API VIEW FOR READING A SPECIFIC RECORD
# class StudentDetails(View):
#     def get(self, request,i):
#         # student = { "id": 1,"name": "Aswin", "age": 21,"course": "B.Tech CSE"}
#         print(i)
#         #reads data from students table matching with id i
#         s=Student.objects.filter(id=i)
#
#         #converts the data into python native type
#         data=list(s.values())
#
#         #return response
#
#         return JsonResponse(data,safe=False)


#API VIEW FOR CREATING A NEW RECORD
#USEING DJANGO
# from json import loads
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# @method_decorator(csrf_exempt,name="dispatch")
#
# class StudentCreate(View):
#     def post(self,request):
#         #fetches the data from client side
#         form_data=request.body
#         #converts json data into python native type
#         data=loads(form_data)
#         print(data)
#         n=data['Name']
#         a=data['Age']
#         m=data['Marks']
#         c=data['Course']
#         #creates a new record inside db table
#         s=Student.objects.create(Name=n,Age=a,Marks=m,Course=c)
#         s.save()
#         #returns response
#         return JsonResponse({'messgae':"created"})

#USING DRF
class StudentCreate(APIView):
     def post(self,request):
            data=request.data#PYTHON NATIVE TYPE
            # VALIDATION+CONVERSION(NATIVE TO MODEL OBJECT)
            serializer_instance = StudentSerializer(data=request.data)
            print(request.data)
            # CHECKS WHERETHER THE DATA COMING FROM CLIENT IS VALID,IF VALID
            # SAVES THE DATA INTO MODEL
            #
            if serializer_instance.is_valid():
                serializer_instance.save()#SAVES THE DATA  INTO MODEL
                return Response(serializer_instance.data)# SENDS CREATED OBJECT AS RESPONSE
           # IF DATA IS NOT VALID IT WILL SHOW VALIDATION ERRORS
            else:
                return Response(serializer_instance.errors)

# #API VIEW FOR DELETING RECORD
# @method_decorator(csrf_exempt,name="dispatch")
# class StudentDelete(View):
#     def delete(self,request,i):
#         #fetch the data from students table matching id i
#         s=Student.objects.get(id=i)
#         #DELETE THE RECORD
#         s.delete()
#         #RETURNS RESPONSE BACK TO CLIENT
#         return JsonResponse({"message":"deleted"})
#
# #API TO UPDATE A EXISTING RECORD
# from json import loads
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# @method_decorator(csrf_exempt,name="dispatch")
# class StudentUpdate(View):
#     def put(self,request,i):
#         # FETCH THE DATA FROM CLIENT SIDE
#         form_data = request.body
#         #CONVERTS THE DATA INTO NATIVE
#         data = loads(form_data)
#         print(data)
#         # READS THE RECORD MATCHING WITH ID FROM DB TABLE
#         s = Student.objects.get(id=i)
#         # UPDATE THE RECORD
#         s.Name=data['Name']
#         s.Age=data['Age']
#         s.Course=data['Course']
#         s.Marks=data['Marks']
#         #SAVES THE RECORD
#         s.save()
#         # RETURNS RESPONSE BACK TO CLIENT
#         return JsonResponse({'message':'UPDATED'})
#
# #API TO UPDATE DATA PARTIALY (patch)
# from json import loads
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# @method_decorator(csrf_exempt,name="dispatch")
# class StudentPartialUpdate(View):
#     def patch(self,request,i):
#         # FETCH THE DATA FROM CLIENT SIDE
#         form_data = request.body
#         # CONVERTS THE DATA INTO NATIVE
#         data = loads(form_data)
#         print(data)
#         # READS THE RECORD MATCHING WITH ID FROM DB TABLE
#         s = Student.objects.get(id=i)
#         # UPDATE THE RECORD
#         if 'Name' in data:
#             s.Name = data['Name']
#         if 'Age' in data:
#             s.Age = data['Age']
#         if 'Course' in data:
#             s.Course = data['Course']
#         if 'Marks' in data:
#             s.Marks = data['Marks']
#         # SAVES THE RECORD
#         s.save()
#         # RETURNS RESPONSE BACK TO CLIENT
#         return JsonResponse({'message': 'UPDATED'})