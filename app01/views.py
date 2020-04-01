from django.shortcuts import render

# Create your views here.

from django.views import View
from django.http.response import JsonResponse

from app01 import models
from .forms.book import BookForm

import json

class BookView(View):
	
	def get(self, request):
		queryset = models.Book.objects.values("title")
		return JsonResponse({
			"code": 0,
			"data": list(queryset)
		})

	def post(self, request):
		form = BookForm(json.loads(request.body.decode()))
		if form.is_valid():
			instance = form.save()
			return JsonResponse({
            	"code": 0,
            	"data": instance.pk
       		})
		else:
			return JsonResponse({
            	"code": 1,
            	"data": form.errors
        })

class BookDetailView(View):
	
	def get(self, request, pk):
		pass
		
	def put(self, request, pk):
		instance = models.Book.objects.filter(pk = pk).first()

		if not instance:
			return JsonResponse({
				"code": 1,
				"data": "数据不存在"

			})

		form = BookForm(instance, json.loads(request.body.decode()))
		if form.is_valid():
			instance = form.save()
			return JsonResponse({
				"code":0,
				"data": instance.pk
			})
		else:
			return JsonResponse({
				"code": 1,
				"data": form.errors
			})

	def delete(self, request, pk):
		models.Book.objects.filter(pk = pk).delete()
		return JsonResponse({
			"code": 0,
			"data": []	
		})
