from django import forms
from data.models import Workflow, Category

class WorkflowForm (forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the name of the workflow.")
	category = forms.ModelMultipleChoiceField(Category.objects.all().order_by('name'), help_text="Please select at least one category.")
	versionInit = forms.CharField(max_length=128, help_text="Please enter the version of the workflow.")
	description = forms.CharField(max_length=512, help_text="Please enter the description of the workflow.")
	keywords = forms.CharField(max_length=256, help_text="Please enter the keywords of the workflow.")
	json = forms.FileField(label="Workflow json file")
	
	class Meta:
	# Provide an association between the ModelForm and a mod
		model=Workflow
		fields = ('name', 'category', 'versionInit', 'description', 'keywords',)


