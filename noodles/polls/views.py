# Create your views here.
from django.shortcuts import render_to_response
from polls.models import Poll
from django.http import Http404

def index(request):
    latest_poll_list1 = Poll.objects.all().order_by('-pub_data')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list1})

def detail(request, poll_id):
    try:
        p = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return renter_to_response('polls/detaul.html', {'poll': p})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)



