from django.contrib import admin
from .models import Project,Phase,Iteration,Time_Record,Code,Defect

admin.site.register(Project)
admin.site.register(Phase)
admin.site.register(Iteration)
admin.site.register(Time_Record)
admin.site.register(Code)
admin.site.register(Defect)