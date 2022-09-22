from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Task
from .serializers import TaskSerializer
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls ={
        "create":"create-task",
        "view":"/detail-task/",
        "List":"/list-task/",
        "update":"update-task",
        "delete":"delete-task",
    }
    return Response(api_urls)

@api_view(['GET'])
def TaskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Details(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(["POST"])
def createTask(request):
    serializer = TaskSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def updateTask(request,pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance = task ,data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request,pk):
    task =Task.objects.get(id = pk)
    task.delete()
    return Response("Task has been deleted.")