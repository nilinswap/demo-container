from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import asyncio
import time
import uuid
import pdfkit

from django.template import loader
from asgiref.sync import sync_to_async
# Create your views here.

async def index(_request):
	for i in range(10):
		print("hello", i)
		await do_something(i)
		print("world", i)
	return JsonResponse("hello world", safe=False)


async def test_html(_request):
	context, template_name = {"is_true": True}, "index"
	template_path = f"{template_name}.html"
	template = await sync_to_async(loader.get_template)(template_path)
	doc = await sync_to_async(template.render)(context)
	return HttpResponse(doc)


async def test_htmltopdf(_request):
	context, template_name = {"is_true": True}, "index"
	template_path = f"{template_name}.html"
	template = await sync_to_async(loader.get_template)(template_path)
	doc = template.render(context)
	print("doc", type(doc))
	filename = uuid.uuid4().hex + ".pdf"
	
	temp_file_path = "/tmp/" + filename
	pdfkit.from_string(doc, temp_file_path)
	print("temp_file_path", temp_file_path)
	return HttpResponse(doc)


async def do_something(j):
	for i in range(3):
		print("something",j, i)