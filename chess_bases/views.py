from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
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

# new topic function
def new_topic(request):
    if request.method != 'POST':
        # no data submitted; create blank form
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('chess_bases:topics')
    # display a blank or invalid form
    context = {'form': form}
    return render(request, 'chess_bases/new_topic.html', context)

# new entry function
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()
    else:
        # POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic 
            new_entry.save()
            return redirect('chess_bases:topic', topic_id=topic_id)
    # display a blak or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'chess_bases/new_entry.html', context)

# edit function
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic 

    if request.method != 'POST':
        # initial request; pre-fill form with current entry
        form = EntryForm(instance=entry)
    else:
        # post data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('chess_bases:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'chess_bases/edit_entry.html', context)