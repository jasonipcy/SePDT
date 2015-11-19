from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	project_id = models.AutoField(primary_key=True)
	project_name = models.CharField(max_length=80)
	project_description = models.TextField(null=True,blank=True)
	project_start_date = models.DateField()
	project_end_date = models.DateField(null=True,blank=True)
	manager_id = models.ForeignKey(User,related_name='User_Project_Manager',limit_choices_to={'groups__name': 'Manager'})
	developer_id = models.ManyToManyField(User,related_name='User_Project_Developer',limit_choices_to={'groups__name': 'Developer'})
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.project_name

class Phase(models.Model):
	phase_id = models.AutoField(primary_key=True)
	project_id = models.ForeignKey(Project)
	PHASE_CHOICES = (
		('inc','Inception'),
		('ela','Elaboration'),
		('con','Construction'),
		('tra','Transition'),
	)
	phase_name = models.CharField(max_length=3,choices=PHASE_CHOICES)
	phase_start_date = models.DateField()
	phase_end_date = models.DateField(null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.project_id) + "_" + self.phase_name

class Iteration(models.Model):
	iteration_id = models.AutoField(primary_key=True)
	phase_id = models.ForeignKey(Phase)
	iteration_version = models.IntegerField()
	iteration_start_date = models.DateField()
	iteration_end_date = models.DateField(null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.phase_id) + "_" + str(self.iteration_version)

class Time_Record(models.Model):
	iteration_id = models.ForeignKey(Iteration)
	developer_id = models.ForeignKey(User,limit_choices_to={'groups__name': 'Developer'})
	ACTIVITY_CHOICES = (
		('dev','Development'),
		('def','Defects_removal'),
	)
	activity = models.CharField(max_length=3,choices=ACTIVITY_CHOICES)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	duration = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.iteration_id) + "_" + str(self.activity) + "_" + str(self.start_time)
	def getDuration(self):
		secs = int(self.duration%60)
		mins = int(self.duration/60)
		hrs = int(self.duration/60/60)
		return str(hrs) + "hr(s) " + str(mins) + "min(s) " + str(secs) + "sec(s)"

class Code(models.Model):
	iteration_id = models.ForeignKey(Iteration)
	manager_id = models.ForeignKey(User,limit_choices_to={'groups__name': 'Manager'})
	code_size = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.iteration_id) + "_" + str(self.created_at)

class Defect(models.Model):
	current_iteration_id = models.ForeignKey(Iteration,related_name='Iteration_Defect_currect')
	defect_iteration_id = models.ForeignKey(Iteration,related_name='Iteration_Defect_defect')
	developer_id = models.ForeignKey(User,limit_choices_to={'groups__name': 'Developer'})
	defect_name = models.CharField(max_length=40)
	DEFECT_CHOICES = (
		('req','Requirement'),
		('des','Design'),
		('imp','Implementation'),
		('bad','Bad_fix'),
	)
	defect_type = models.CharField(max_length=3,choices=DEFECT_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.defect_iteration_id) + "_" + str(self.defect_name)