from django.contrib import admin
from .models import TechnologyDomain, Project  # Project import kiya

@admin.register(TechnologyDomain)
class TechnologyDomainAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'domain')  # Projects ke title aur domain dikhayenge
    list_filter = ('domain',)  # Filter projects by domain
