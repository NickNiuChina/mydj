from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request):
	# now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	# html = "It is now %s." % now
	# return HttpResponse(html)
	
	# now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	# html = "<html><body>It is now %s</body></html>" % now
	# return HttpResponse(html)

	# now = datetime.datetime.now()
	# t = get_template('current_datetime.html')
	# html = t.render({'current_date': now})
	# return HttpResponse(html)
	now = datetime.datetime.now()
	return render(request, 'current_datetime.html', {'current_date': now})



def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render(request, 'future_time.html', {'hour_offset':offset, 'next_time':dt})