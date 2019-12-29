from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def current_url_view_good(request):
	return HttpResponse("Welcome to the page at %s" % request.path)
	# request.path 完整的路径,不含域名,但是包含前导斜线 “/hello/”
	# request.get_host() 主机名(即通常所说的“域名”) “127.0.0.1:8000”或“www.exam-ple.com”
	# request.get_full_path() 包含查询字符串(如果有的话)的路径 “/hello/?print=true”
	# request.is_secure() 通过 HTTPS 访问时为 True ,否则为 False True 或 False

def ua_display_good(request):
	ua = request.META.get('HTTP_USER_AGENT', 'unknown')
	return HttpResponse("Your browser is: %s" % ua)

def display_meta(request):
	values = request.META.items()
	# values.sort()
	html = []
	for k, v in values:
		html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
	return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term please.')
		elif len(q) > 20:
			errors.append('Please enter less than 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html', {'books': books, 'query': q})
	return render(request, 'search_form.html', {'errors': errors})