# Blanca Martin and Luis Carabe pair number 10

#populate database
# execute python manage.py  populate

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

import django
from django.shortcuts import get_object_or_404
from random import randint

django.setup()

from data.models import Category, Workflow

#models
CATEGORY = 'category'
USER = 'user'
WORKFLOW = 'workflow'

class Command(BaseCommand):
	#  args = '<-no arguments>'
	# helps and arguments shown when command python manage.py help populate
	# is executed.
	help = 'This scripts populates de workflow database, no arguments needed.' \
				 'Execute it with the command line python manage.py populate'

	def getParragraph(self, init, end):
		# getParragraph returns a parragraph, useful for testing
		if end > 445:
			end = 445
		if init < 0:
			init = 0
		return """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum."""[init:end]

	def handle(self, *args, **options):
		self.cleanDatabase()
		self.addCategory(5) # add 5 categories
		self.addWorkflow(13) # add 13 workflows

	def cleanDatabase(self):
		# Delete all workflows
		for workflow in Workflow.objects.all():
			workflow.delete()

		# Delete all categories
		for category in Category.objects.all():
			for workflow in Workflow.objects.filter(category=category):
				workflow.delete()
			category.delete()


	def addCategory(self, noCategories):
		# Create category with name category x
		# being x a number between 0 and noCategories
		for i in range(0, noCategories):
			c = Category.objects.get_or_create(name="category " + str(i),
				tooltip=self.getParragraph(randint(0,50), randint(55, 100)))[0]
			c.save()


	def addWorkflow(self, noWorkflows):

		# Create workflow, all numbers involved are random ints
		for i in range(0, noWorkflows):
			# r is a randint between 0 and (number of categories -1)
			r = randint(0, Category.objects.count()-1)
			
			j = i
			# We don't create workflow number 10
			if i == 10:
				j = noWorkflows
			
			w =  Workflow.objects.get_or_create(name="workflow " + str(j),
					views=randint(0, 100),
					description=self.getParragraph(randint(50, 80), randint(100, 140)),
					downloads=randint(0, 100),
					versionInit=str(randint(0,3)) + "." + str(randint(0,20)),
					client_ip=str(randint(0,255)) + "." + str(randint(0,255)) + "." + str(randint(0,255)) + "." + str(randint(0,255)),
					keywords=self.getParragraph(randint(0,5), randint(0,20)),
					json = self.getJson())[0]
			
			# Add a random category to the workflow
			w.category.add(get_object_or_404(Category, name="category " + str(r)))
			w.save()


	def getJson(self):
			return """[
	{
			"object.className": "ProtImportMovies",
			"object.id": "2",
			"object.label": "import movies",
			"object.comment": "\\n",
			"runName": null,
			"runMode": 0,
			"importFrom": 0,
			"filesPath": "",
			"filesPattern": "Falcon*.mrcs",
			"copyFiles": false,
			"acquisitionWizard": null,
			"voltage": 300.0,
			"sphericalAberration": 2.0,
			"amplitudeContrast": 0.1,
			"magnification": 39548,
			"samplingRateMode": 0,
			"samplingRate": 3.54,
			"scannedPixelSize": 14.0,
			"gainFile": null
	},
	{
			"object.className": "ProtMovieAlignment",
			"object.id": "40",
			"object.label": "movie alignment",
			"object.comment": "\\n",
			"runName": null,
			"runMode": 0,
			"cleanMovieData": true,
			"alignMethod": 0,
			"alignFrame0": 0,
			"alignFrameN": 0,
			"doGPU": false,
			"GPUCore": 0,
			"winSize": 150,
			"sumFrame0": 0,
			"sumFrameN": 0,
			"cropOffsetX": 0,
			"cropOffsetY": 0,
			"cropDimX": 0,
			"cropDimY": 0,
			"binFactor": 1,
			"extraParams": "",
			"hostName": "localhost",
			"numberOfThreads": 4,
			"numberOfMpi": 1,
			"inputMovies": "2.__attribute__outputMovies"
	},
	{
			"object.className": "ProtCTFFind",
			"object.id": "82",
			"object.label": "ctffind4",
			"object.comment": "\\n",
			"runName": null,
			"runMode": 0,
			"recalculate": false,
			"sqliteFile": null,
			"ctfDownFactor": 1.0,
			"useCftfind4": true,
			"astigmatism": 100.0,
			"findPhaseShift": false,
			"lowRes": 0.05,
			"highRes": 0.35,
			"minDefocus": 0.5,
			"maxDefocus": 4.0,
			"windowSize": 256,
			"hostName": "localhost",
			"numberOfThreads": 4,
			"numberOfMpi": 1,
			"inputMicrographs": "40.__attribute__outputMicrographs"
	},
	{
			"object.className": "EmanProtBoxing",
			"object.id": "369",
			"object.label": "eman2 - boxer",
			"object.comment": "",
			"runName": null,
			"runMode": 0,
			"inputMicrographs": "40.__attribute__outputMicrographs"
	},
	{
			"object.className": "ProtUserSubSet",
			"object.id": "380",
			"object.label": "3mics",
			"object.comment": "",
			"runName": null,
			"runMode": 0,
			"other": null,
			"sqliteFile": "Runs/000082_ProtCTFFind/ctfs_selection.sqlite,",
			"outputClassName": "SetOfMicrographs",
			"inputObject": "82.__attribute__outputCTF"
	},
	{
			"object.className": "XmippProtParticlePicking",
			"object.id": "420",
			"object.label": "xmipp3 - manual picking",
			"object.comment": "",
			"runName": null,
			"runMode": 0,
			"memory": 2.0,
			"inputMicrographs": "40.__attribute__outputMicrographs"
	},
	{
			"object.className": "XmippProtExtractParticles",
			"object.id": "449",
			"object.label": "extract 3 mics",
			"object.comment": "\\n",
			"runName": null,
			"runMode": 0,
			"micsSource": 0,
			"boxSize": 64,
			"doSort": false,
			"rejectionMethod": 0,
			"maxZscore": 3,
			"percentage": 5,
			"doRemoveDust": true,
			"thresholdDust": 3.5,
			"doInvert": true,
			"doFlip": false,
			"doNormalize": true,
			"normType": 2,
			"backRadius": -1,
			"hostName": "localhost",
			"numberOfThreads": 1,
			"numberOfMpi": 1,
			"ctfRelations": "82.__attribute__outputCTF",
			"inputMicrographs": "369.outputMicrographs"
	},
	{
			"object.className": "XmippParticlePickingAutomatic",
			"object.id": "517",
			"object.label": "xmipp3 - auto-picking",
			"object.comment": "",
			"runName": null,
			"runMode": 0,
			"micsToPick": 0,
			"memory": 2.0,
			"hostName": "localhost",
			"numberOfThreads": 1,
			"numberOfMpi": 1,
			"xmippParticlePicking": "420"
	}
]"""

#There's no need to bypass manage.py, since it's a wonderful convenience wrapper around
			# the Django project administration tools. It can be used to create custom
			# management commands - e.g. your own commands parallel to shell, dumpdata,
			# and so on. Not only that creating such commands gives you a very succinct,
			# boilterplate-free way of writing custom management scripts, it also gives
			# you a natural location to house them, per application.
