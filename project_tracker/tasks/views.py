from django.http import HttpResponse
from django.urls import reverse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
from django.views import View


class IndexView(View):
    ...