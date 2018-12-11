from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Diagnoses
# Create your views here.


@login_required(login_url='/login/')
def diagnoses(request, template_name='pages/diagnoses.html'):
	ctx = {}
	hadm_id = request.user.hadm_id
	diagnoses = Diagnoses.objects.filter(hadm_id=hadm_id).order_by('seq_num')
	ctx['diagnoses'] = diagnoses
	return render(request, template_name, ctx)
