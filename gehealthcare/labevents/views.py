from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Labevent


@login_required(login_url='/login/')
def labevents(request, template_name='pages/labreports.html'):
	ctx = {}
	hadm_id = request.user.hadm_id
	labevents = Labevent.objects.filter(hadm_id=hadm_id).order_by('charttime')
	ctx['labevents'] = labevents
	return render(request, template_name, ctx)