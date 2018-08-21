from django.db import models


# Create your models here.
class Policy(models.Model):
    firstname = models.CharField(max_length=30, db_column='name')
    lastname = models.CharField(max_length=30)
    policyno = models.IntegerField()
    date = models.CharField(max_length=25)

    def __str__(self):
        return self.firstname
