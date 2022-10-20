from django.shortcuts import render

from .models import Topic 
# Create your views here.
def index(request):
    """Home page of Chess Base"""
    return render(request, 'chess_bases/index.html')

# create a topics function
def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'chess_bases/topics.html', context)