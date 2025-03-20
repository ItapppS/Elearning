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

from django.db import models
from django.utils.text import slugify
import json

class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='project_images/')
    subdomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    # 🔹 Additional fields
    introduction = models.TextField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    video_description = models.TextField(blank=True, null=True)
    guide_description = models.TextField(blank=True, null=True)
    guide_link = models.URLField(blank=True, null=True)
    report_description = models.TextField(blank=True, null=True)
    report_link = models.URLField(blank=True, null=True)
    interface_diagram = models.ImageField(upload_to='interface_diagrams/', blank=True, null=True)

    # 🔹 JSON Field to store multiple components with specifications and price
    components = models.JSONField(default=dict, blank=True, null=True)  

    # 🔹 Project-level total price (Auto Calculated)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        """ 
        🔹 Auto-calculate total price from component prices & quantities before saving 
        """
        if self.components and isinstance(self.components, dict):
            total_cost = 0
            updated_components = {}

            for key, item in self.components.items():
                name = item.get("name", "").strip()
                quantity = max(int(item.get("quantity", 1)), 1)  # ✅ Quantity must be at least 1
                price = float(item.get("price", 0))
                specification = item.get("specification", "No specification available").strip()

                # 🔥 Auto-calculate total cost
                total_cost += price * quantity

                # ✅ Ensure cleaned and structured data is stored
                updated_components[key] = {
                    "name": name,
                    "quantity": quantity,
                    "price": price,
                    "specification": specification
                }

            self.components = updated_components
            self.price = total_cost  # ✅ Store total price
        
        # 🔹 Slug generation
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Component(models.Model):
    name = models.CharField(max_length=100)
    recommended = models.CharField(max_length=100)
    customizable_options = models.JSONField(default=list)  # Store selectable options
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name