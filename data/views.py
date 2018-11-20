# Blanca Martin and Luis Carabe pair number 10

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from find import views

def base(request):
	# If the method used is POST, we are searching for a workflow
	if request.method == 'POST':
		return views.workflow_search(request)
	# If it's GET, we are requesting the template
	return render(request, 'data/base.html')
