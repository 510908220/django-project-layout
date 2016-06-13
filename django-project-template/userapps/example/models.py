from __future__ import unicode_literals

from django.db import models


YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
)


class Shop(models.Model):

    class Meta:
        db_table = "shop"

    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=YEAR_IN_SCHOOL_CHOICES, default=YEAR_IN_SCHOOL_CHOICES[0][0])
    console = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
