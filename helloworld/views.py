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

	
def events(request):
	url='https://www.eventbriteapi.com/v3/categories/?token=BKKRDKVUVRC5WG4HAVLT'
	response=urllib.request.urlopen(url)
	str_response=response.readall().decode('utf-8')
	data=json.loads(str_response)
	categories=data['categories']
	categorylist={}
	
	for item in categories:
		#comment
		#categorylist.update({'a':1})
		id=item['id']
		catname=item['name']
		categorylist.update({id:catname})
		tuple_cat = tuple(categorylist)
		list=categorylist.items()
	paginator = Paginator(categories, 5) # Show 25 contacts per page
	page=request.GET.get('page')

    # Make sure page request is an int. If not, deliver first page.
	
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
       
			contacts = paginator.page(1)
	except EmptyPage:
       
			contacts = paginator.page(paginator.num_pages)



	return render(request,'helloworld/events.html', {'cat': contacts})
	