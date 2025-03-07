from django.db import models
from django.utils.text import slugify

class PhnUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 
    age = models.PositiveIntegerField()
    address = models.TextField(max_length=255)
    mobile_no = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username

class TechnologyDomain(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='domain_images/')
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class SubDomain(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='subdomain_images/', default=True)
    domain = models.ForeignKey(TechnologyDomain, on_delete=models.CASCADE, related_name='subdomains')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='project_images/')
    subdomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE, related_name='projects')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
