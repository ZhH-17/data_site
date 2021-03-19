from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from .models import Record
import os
from .settings import DATA_BASEPATH


def index(request):
    return HttpResponse("You're looking at question ")


# Create your views here.
class IndexView(generic.ListView):
    model = Record
    template_name = 'data_record/index.html'
    context_object_name = 'latest_question_list'
    paginate_by = 1


class DetailView(generic.DetailView):
    model = Record
    template_name = 'data_record/detail.html'
    context_object_name = 'record'


def record_result(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    return HttpResponse("You're looking on record %s." % record_id)
    # return render(request, 'polls/results.html', {'question': question})


