from django.shortcuts import render
from .models import Bank
# Create your views here.
def index(request):
	obj = Bank.objects.all()
	context = {
		'movie_list': obj
	}
	return render(request, 'index.html', context)