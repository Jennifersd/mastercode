from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaulttfilters import slugify

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    active = models.BooleanField(default=False)
    
    def save(self, *args, **Kwargs):
        self.slug = slugify(self.name)
        super(Language, self).save(*args, **Kwargs)
        
    def get_absolute_url(self):
        return reverse('tutorials:language', args=[self.slug] )

    def __str__(self):
        return self.name
    
class StudentExperience(models.Model):
    EXPERIENCE_LEVEL_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )
    
    experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES, default='Beginner')
    
    def __str__(self):
        return self.experience_level
    
class TutorialSeries(models.Model):
    language = models.ForeignKey(Language)
    studentExperience = models.ForeignKey(StudentExperience)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    archived = models.BooleanField(default=False)
    slug = models.SlugField(max_length=250, unique=True)
    
    def save(self, *args, **Kwargs):
        self.slug = slugify(self.name)
        super(TutorialSeries, self).save(*args, **Kwargs)
        
    def get_absolute_url(self):
        return reverse('tutorials:tutorial_series_details', args=[self.slug] )

    def __str__(self):
        return self.name
    
class Lesson(models.Model):