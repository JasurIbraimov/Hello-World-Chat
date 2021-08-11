from django.shortcuts import render

# Create your views here.

def get_homepage_view(request):
	return render(request, 'homepage.html', {})