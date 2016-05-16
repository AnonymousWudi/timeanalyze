# coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class indexView(View):
    def get(self, request):
        return HttpResponse('ok')
