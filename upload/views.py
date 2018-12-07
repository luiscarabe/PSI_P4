# Blanca Martin and Luis Carabe pair number 10

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from upload.forms import WorkflowForm

from django.shortcuts import render

def add_workflow(request):
	# If the method is post
	if request.method == 'POST':

		# We check if the form with the provided information is valid
		form = WorkflowForm(request.POST, request.FILES)
		
		if form.is_valid():
			# The json file is read and decoded
			workflowFile = form.cleaned_data['json']
			try:
				file_data = workflowFile.read().decode('utf-8')
			except UnicodeDecodeError:
				# If the file could not be decoded, an error message is shown
				return render(request, "upload/upload.html", {'form' : form, 'error' : True })
			
			# We fill the json field of the form with the data read
			form.instance.json = file_data

			# The creation of the workflow
			workflow = form.save(commit=True)
			_dict = {}
			_dict['result'] = True
			_dict['workflow'] = workflow
			# We show a message that informs that the workflow has been successfully created
			_dict['error'] = 'Workflow ' + workflow.name + ' successfully uploaded'
			return render(request, 'find/detail.html', _dict)
		
		else:
			# If the form was not valid, we print the errors in the form
			print form.errors

	form = WorkflowForm()
	return render(request, "upload/upload.html", {'form' : form, 'error' : False })