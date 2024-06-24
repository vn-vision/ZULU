from django.shortcuts import render
from django.http import JsonResponse


# index view, improve on it
def api_index(request):
    return JsonResponse({"Greeting" :"Hello, world. You're at the zulu index."})
