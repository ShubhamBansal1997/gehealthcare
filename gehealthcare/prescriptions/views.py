from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Prescription



@login_required(login_url='/login/')
def eprescription(request, template_name='pages/eprescription.html'):
	ctx = {}
	hadm_id = request.user.hadm_id
	prescription = Prescription.objects.filter(hadm_id=hadm_id).order_by('startdate')
	ctx['prescription'] = prescription
	return render(request, template_name, ctx)

