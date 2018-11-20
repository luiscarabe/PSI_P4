# Blanca Martin and Luis Carabe pair number 10

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import django, os

from django.shortcuts import render
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from data.models import Category, Workflow


def workflow_list(request, category_slug = None):
	page = request.GET.get('page', 1)
	workflows = None

	# Search for all categories
	categories = Category.objects.all()
	found = True # Default value of found is true

	# Check if we are searching a specific category
	# In case not...
	if category_slug == None:
		category = None
		# List of all workflows
		workflow_list = Workflow.objects.all()
		if workflow_list.count() == 0:
			found = False
			error = "No Workflows found!"
		else:
			paginator = Paginator(workflow_list, 10)
			error = ""
			try:
				workflows = paginator.page(page)
			except PageNotAnInteger:
				workflows = paginator.page(1)
			except EmptyPage:
				paginator = paginator.page(paginator.num_pages)
	# In other case...
	else:
		try:
			# Find category with that slug and its workflows
			category = Category.objects.get(slug = category_slug)
			workflow_list = Workflow.objects.filter(category = category)
			paginator = Paginator(workflow_list, 10)
		except ObjectDoesNotExist:
			# Category does not exist
			category = None
			found = False
			error = "Category with slug '" + category_slug + "' does not exist"

		# If there is no workflows in some category
		if workflow_list.count()==0 and found == True:
			found = False
			error = "No Workflows in this category!"
		else:
			found = True
			error = ""
			paginator = Paginator(workflow_list, 10)
			error = ""
			try:
				workflows = paginator.page(page)
			except PageNotAnInteger:
				workflows = paginator.page(1)
			except EmptyPage:
				paginator = paginator.page(paginator.num_pages)

	# Create the dictionary
	_dict = {'category' : category,
					 'categories' : categories,
					 'workflows' : workflows,
					 'result' : found,
					 'error' : error}
	return render(request, 'find/list.html', _dict)

def workflow_detail(request, id, slug):

	# Default values
	found = True
	error=""

	# Find workflow with id given
	try:
		workflow = Workflow.objects.get(id = id)
	except ObjectDoesNotExist:
		# Workflow does not exist
		workflow = None
		found = False
		error = "Workflow with slug '" + slug + "' and id '" + str(id) +  "' does not exist"

	# Create the dictionary
	_dict = {}
	_dict['result'] = found
	_dict['workflow'] = workflow
	_dict['error'] = error

	return render(request, 'find/detail.html', _dict)

def workflow_search(request):

	# Default values
	found = True
	error=""

	# Find workflow with name given
	try:
		workflow = Workflow.objects.get(name = request.POST['key'])
	except ObjectDoesNotExist:
		# Workflow does not exist
		workflow = None
		found = False
		error = "Workflow with name '" + request.POST['key'] + "' does not exist"

	# Create the dictionary
	_dict = {}
	_dict['result'] = found
	_dict['workflow'] = workflow
	_dict['error'] = error

	return render(request, 'find/detail.html', _dict)
