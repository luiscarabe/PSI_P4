# Blanca Martin and Luis Carabe pair number 10

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.template.defaultfilters import slugify


class Category(models.Model):
	# Name of the category
	name = models.CharField(max_length=128, unique=True, blank=False)
	# Slug of the category
	slug = models.SlugField(unique=True)
	# Date of creation
	created = models.DateTimeField(auto_now_add = True, editable=True)
	# Description
	tooltip = models.CharField(max_length=128)

	def save(self, *args, **kwargs):
		# Before saving we create the slug based on the name
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		# For linguistic reasons
		verbose_name_plural='Categories'

	def __str__(self):# For Python 2, use __unicode__ too
		return self.name


class Workflow(models.Model):
	# Name of the workflow
	name = models.CharField(max_length=128, unique=True, blank=False)
	# Slug of the workflow
	slug = models.SlugField(unique=True)
	# Description
	description = models.CharField(max_length=512, default="")
	# Number of views
	views = models.IntegerField(default=0)
	# Number of downloads
	downloads = models.IntegerField(default=0)
	# Version of the workflow
	versionInit = models.CharField(max_length=128)
	# Categories the workflow is associated with
	category = models.ManyToManyField(Category)
	# The ip of the client
	client_ip = models.GenericIPAddressField(default="127.0.0.1")
	# Some key words
	keywords = models.CharField(max_length=256, default="")
	# A json
	json = models.TextField()
	# Date of creation
	created = models.DateTimeField(auto_now_add = True)

	def save(self, *args, **kwargs):
		# Before saving we create the slug based on the name
		self.slug = slugify(self.name)
		super(Workflow, self).save(*args, **kwargs)


	def __str__(self):# For Python 2, use __unicode__ too
		return self.name
