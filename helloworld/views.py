import urllib.request
import json
from django.http import HttpResponse
from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def index(request):
	url='https://www.eventbriteapi.com/v3/categories/?token=BKKRDKVUVRC5WG4HAVLT'
	response=urllib.request.urlopen(url)
	str_response=response.readall().decode('utf-8')
	data=json.loads(str_response)
	categories=data['categories']
	categorylist={}
	name=[]
	

	for item in categories:
		name.append(item['name'])
		#categorylist.update({'a':1})
		id=item['id']
		catname=item['name']
		categorylist.update({id:catname})
	
	print (categorylist)
	return render(request, 'helloworld/index.html',{'cat': categorylist})


def event1(request):
	list=request.get_full_path() 
	split =list.split('?')
	print (split[1])
	base_url='https://www.eventbriteapi.com/v3/events/search/?'+split[1]+'&token=BKKRDKVUVRC5WG4HAVLT'
	response=urllib.request.urlopen(base_url)
	str_response=response.readall().decode('utf-8')
	data=json.loads(str_response)
	event_list=data['events']
	pagination_obj=data['pagination']
	page_count=pagination_obj['page_count']
	page_size=pagination_obj['page_size']
	for i in range(0,page_count):
		print (i)
		page_url='https://www.eventbriteapi.com/v3/events/search/?'+split[1]+'&token=BKKRDKVUVRC5WG4HAVLT'+'&page='+str(i)
		response=urllib.request.urlopen(page_url)
		data=json.loads(str_response)
		event_list.append(data['events'])
		print(page_url)
	return event_list
	
	
	
def page_count(request)


return





	
def events(request):
	list=request.get_full_path() 
	if 'categories' in list:
		list=event1(request)
			

	return render(request,'helloworld/events.html', { 'hello' :list })
	

	
	
