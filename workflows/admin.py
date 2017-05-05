from django.contrib import admin

from .models import Workflow


# Register your models here.


class WorkflowsAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name','galaxy_server')
    list_filter = ['galaxy_server']

admin.site.register(Workflow,WorkflowsAdmin)