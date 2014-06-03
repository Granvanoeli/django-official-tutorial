from django.http import HttpResponse
from polls.models import Poll
# from django.http import Http404
from django.shortcuts import render, get_object_or_404




def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5] # Create the list of the latest 5 polls
    context = {'latest_poll_list': latest_poll_list}    # Pass the list just created as context
    return render(request, 'polls/index.html', context) # Render the request and the context with the index.htm template

#def detail(request, poll_id):
#    try:
#        poll = Poll.objects.get(pk=poll_id)
#    except Poll.DoesNotExist:
#        raise Http404
#    return render(request, 'polls/detail.html', {'poll': poll}) # Context contains the ID of the poll

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)