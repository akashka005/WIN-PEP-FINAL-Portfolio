from django.db import models

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Languages', 'Languages'),
        ('AI/ML Stack', 'AI/ML Stack'),
        ('Web & Tools', 'Web & Tools'),
    ]
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=80)  # Percentage
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('deployed', 'Deployed'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    details = models.TextField(blank=True, help_text="Detailed description for the modal")
    date = models.CharField(max_length=100)
    tech_stack = models.CharField(max_length=300, help_text="Comma separated tags")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='completed')
    order = models.IntegerField(default=0)

    def __get_tech_list(self):
        return [tag.strip() for tag in self.tech_stack.split(',')]
    
    tech_list = property(__get_tech_list)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, default='fas fa-trophy')
    
    def __str__(self):
        return self.title

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    date_range = models.CharField(max_length=100)
    grade = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"