from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Система контроля качества<br><a href='/bugs/'>Список всех багов</a><br><a href='/features/'>Запросы на улучшение</a>")

def bug_list(request):
    return HttpResponse("Cписок отчетов об ошибках")

def feature_list(request):
    return HttpResponse("Список запросов на улучшение")

def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")
