import urllib.request
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

base_url='https://www.eventbriteapi.com/v3/events/search/?token=BKKRDKVUVRC5WG4HAVLT&'

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
	return render(request, 'helloworld/index.html',{'cat':categorylist})




def getevents(url,set_max_pages):
	
	
	response=urllib.request.urlopen(base_url+url)
	str_response=response.readall().decode('utf-8')
	data=json.loads(str_response)
	event_list=data['events']
	return event_list


	
def get_max_pages(url):
	response=urllib.request.urlopen(base_url+url)
	str_response=response.readall().decode('utf-8')
	data=json.loads(str_response)
	pagination_obj=data['pagination']
	max_pages1=pagination_obj['page_count']
	print (max_pages1)
	return max_pages1
	
def events(request):
	
	set_max_page_count='false'
	current_page_uri=request.get_full_path()
	query_string=current_page_uri.split('?')
	get_page_no = request.GET.get('page')
	valid_query='true'
	max_pages=get_max_pages(query_string[1])
	try:
		current_page_no = int(get_page_no)
	except TypeError:
		current_page_no = 1
		set_max_page_count='true'
	
	if current_page_no is 1:
		next_page=current_page_uri+'&page=2'
		previous_page=0
	elif current_page_no is max_pages:
		print (current_page_no)
		print (max_pages)
		next_page=0
		pageless_uri=current_page_uri.split('page')
		previous_page_no=int(current_page_no)-1
		previous_page=pageless_uri[0]+'page='+str(previous_page_no)
	elif current_page_no > max_pages:
		previous_page=0
		next_page=0
		valid_query='false'
	else:
		next_page_no=int(current_page_no)+1
		previous_page_no=int(current_page_no)-1
		pageless_uri=current_page_uri.split('page')
		next_page=pageless_uri[0]+'page='+str(next_page_no)
		previous_page=pageless_uri[0]+'page='+str(previous_page_no)
	
	if  valid_query is 'true':
		events=getevents(query_string[1],set_max_page_count)
	else:
		raise Http404("Page Not Found")
	
			

	return render(request,'helloworld/events.html', { 'events' :events,'previous_page':previous_page,'next_page' : next_page,'current_page_no':current_page_no,'max_pages':max_pages})
	

	
	
