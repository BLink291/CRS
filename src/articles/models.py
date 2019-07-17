from django.conf import settings
from django.contrib.auth.models import User

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext as _
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255 )
    slug = models.SlugField(max_length= 255, unique_for_date = 'created')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    lat = models.DecimalField(_('Latitude'), max_digits=22, decimal_places=16, blank=True, null=True)
    lng = models.DecimalField(_('Longitude'), max_digits=22, decimal_places=16, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article_detail', 
                    args=[ self.created.year,
                            self.created.month,
                            self.created.day, 
                            self.slug])