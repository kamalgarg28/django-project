from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
import datetime,  json
import mysql.connector as sql
from .models import Students
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication

# Create your views here.
class Create(APIView):
    
    def post(self, request):
        m = sql.connect(host='localhost', user='root', password="Kamalgarg@28", database='school')
        cursor = m.cursor()
        name = request.data['name']
        email = request.data['email']
        address = request.data['address']
        city = request.data['city']
        grade = request.data['grade']
        section = request.data['section']
        c = "insert into students_students(name,email,address,city,grade,section) Values('{}','{}','{}','{}','{}','{}')".format(name,email,address,city,grade,section)
        print(c)
        cursor.execute(c)
        m.commit()
        response = Response()
        response.data = {
            'message': 'Student successfully added!'
        }
        return response


class Read(APIView):
    permission_classes = [IsAuthenticated]
    #authentication_classes = [SessionAuthentication]
    def get(self, request):

        try:
            m = sql.connect(host='localhost', user='root', password="Kamalgarg@28", database='school')
        except:
            print("Connection error in MySQL")
        cursor = m.cursor()
        c = "select * from students_students"
        cursor.execute(c)
        t = cursor.fetchall()
        m.commit()
        pagination = request.data['pagination']
        response = Response()
        response.data = t[:pagination]
        return response


class Update(APIView):

    def post(self, request):
        m = sql.connect(host='localhost', user='root', password="Kamalgarg@28", database='school')
        cursor = m.cursor()
        name = request.data['name']
        email = request.data['email']
        address = request.data['address']
        city = request.data['city']
        grade = request.data['grade']
        section = request.data['section']
        c = "delete from students_students where email='{}'".format(email)
        cursor.execute(c)
        c = "insert into students_students(name,email,address,city,grade,section) Values('{}','{}','{}','{}','{}','{}')".format(name,email,address,city,grade,section)
        cursor.execute(c)
        m.commit()
        response = Response()
        response.data = {
            'message': 'Student successfully Updated!'
        }
        return response


class Delete(APIView):
    
    def post(self, request):
        m = sql.connect(host='localhost', user='root', password="Kamalgarg@28", database='school')
        cursor = m.cursor()
        email = request.data['email']
        c = "delete from students_students where email='{}'".format(email)
        cursor.execute(c)
        m.commit()
        response = Response()
        response.data = {
            'message': 'Student successfully Deleted!'
        }
        return response