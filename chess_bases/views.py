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

# single topic function
def topic(request, topic_id):
    """Show a single topic and all of its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'chess_bases/topic.html', context)