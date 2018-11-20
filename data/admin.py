# Blanca Martin and Luis Carabe pair number 10
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from data.models import Category, Workflow

class CategoryAdmin(admin.ModelAdmin):
		# We display only the field listed below in the admin interface
    list_display = ('name', 'slug')
		# We mark the field created as a readonly field
    readonly_fields = ('created',)
    # We prepopulate the slug field based on the name
    prepopulated_fields = {'slug' : ('name',)}

class WorkflowAdmin(admin.ModelAdmin):
		# We display only the field listed below in the admin interface
    list_display = ('name', 'slug', 'views', 'downloads', 'client_ip', 'created')
		# We mark the field created as a readonly field
    readonly_fields = ('created',)
    # We prepopulate the slug field based on the name
    prepopulated_fields = {'slug' : ('name',)}

# Registration of the models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Workflow, WorkflowAdmin)
