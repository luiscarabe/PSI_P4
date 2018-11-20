# Blanca Martin and Luis Carabe pair number 10

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

import django, os
from data.models import Category, Workflow
from populate import Command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workflowrepository.settings')
django.setup()
# Populate is class command
populate = Command()

# Function to filter workflows contained in some category
def workflow_given_category(categoryname):
	try:
		ret = []
		# Get category with that name
		c = Category.objects.get(name = "category 1")
		# Filter workflows
		q = Workflow.objects.filter(category = c)
		# Returns those workflows names
		for w in q:
			ret.append(w.name)
		return w
	# If the category does not exist, we inform the user
	except ObjectDoesNotExist:
		return "Category named '" + categoryname + "' does not exist"


# Function to give all categories of a specific workflow
def category_given_workflow(workflowslug):
	try:
		ret = []
		# Filter workflow by slug
		q = Workflow.objects.get(slug = workflowslug)
		# Return categories asocciated with that workflow
		query = q.category.all()
		for q in query:
			ret.append(q.slug)
		return ret
	# If the workflow does not exist, we inform the user
	except ObjectDoesNotExist:
		return "Workflow with slug '"+ workflowslug +"'  does not exist"

# Get or create categories category 1 and category 2
for i in range(1, 3):
	print "Creating category " + str(i) + "..."
	try:
		# Try to find the category
		c = Category.objects.get(name = "category " + str(i))
	except ObjectDoesNotExist:
		# If it does not exist, we create it
		c = Category(name = "category " + str(i))
		c.save()

# Get or create workflows with names workflow xy, x in {1,2} and y in {1,2,3} and relate them to category x
for i in range(1, 4):
	for j in range(1, 3):
		print "Creating workflow " + str(j) + str(i) + "..."
		try:
			# Try to find the workflow
			w = Workflow.objects.get(name = "workflow " + str(j) + str(i))
			# Relate with category j
			w.category.add(Category.objects.get(name = "category " + str(j)))
		except ObjectDoesNotExist:
			# If the workflow does not exist, we create it
			w = Workflow(name = "workflow " + str(j) + str(i), json = Command.getJson(populate))
			w.save()
			w.category.add(Category.objects.get(name = "category " + str(j)))



print "--------------------------------------------"

# Print query that returns a list containinf the workflows related with category 1
print "Searching workflow associated to category 1..."
print workflow_given_category("category 1")

# Print slug of all categories found in a query that searchs for cats in workflow-11
print "Searching category of workflow-11..."
print category_given_workflow("workflow-11")

# Print slug of category found in a query that searchs for cats in workflow-10 (must show workflow not found)
print "Searching category of workflow-10..."
print category_given_workflow("workflow-10")

