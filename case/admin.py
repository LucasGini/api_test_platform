from django.contrib import admin
from .models import ProjectList, ModuleList, TestCase, TestSuite

# Register your models here.
admin.site.register(ProjectList)
admin.site.register(ModuleList)
admin.site.register(TestCase)
admin.site.register(TestSuite)