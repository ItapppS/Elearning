from django.contrib import admin
from .models import TechnologyDomain, SubDomain, Project, Component

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'subdomain')  # domain ki jagah subdomain
    list_filter = ('subdomain',)  # domain ki jagah subdomain
    search_fields = ('title', 'subdomain__title')  # Subdomain ka title bhi searchable

@admin.register(TechnologyDomain)
class TechnologyDomainAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    search_fields = ('title',)

@admin.register(SubDomain)
class SubDomainAdmin(admin.ModelAdmin):
    list_display = ('title', 'domain')
    list_filter = ('domain',)
    search_fields = ('title', 'domain__title')


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'recommended', 'price')
    search_fields = ('name',)
