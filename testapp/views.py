from django.shortcuts import render
import json
import requests
from django.views.generic import TemplateView





# Create your views here.
def index(request):
	context = {}
	news_data = requests.get(' http://hlx.li/tmp/lpb/payload.json?api_key=developer_key')
	# print(news_data.json())
	data = news_data.json()
	list1=[]
	for each in data:
		print(each)
		each_data={ x.replace(' ',''):v
		
		for x,v in each.items()}
		list1.append(each_data)

	context["data"] = list1
	# print(type(context))
	return render(request,'templates/hello.html',context)


