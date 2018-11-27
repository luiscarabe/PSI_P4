# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from upload.forms import WorkflowForm

from django.shortcuts import render

def add_workflow(request):
	if request.method == 'POST':
		form = WorkflowForm(request.POST, request.FILES)
		
		if form.is_valid():
			
			workflowFile = form.cleaned_data['json']
			try:
				file_data = workflowFile.read().decode('utf-8')
			except UnicodeDecodeError:
				return render(request, "upload/upload.html", {'form' : form, 'error' : True })
			
			form.instance.json = file_data

			workflow = form.save(commit=True)
			_dict = {}
			_dict['result'] = True
			_dict['workflow'] = workflow
			_dict['error'] = 'Workflow ' + workflow.name + ' successfully uploaded'
			return render(request, 'find/detail.html', _dict)
		
		else:
			print form.errors

	form = WorkflowForm()
	return render(request, "upload/upload.html", {'form' : form, 'error' : False })