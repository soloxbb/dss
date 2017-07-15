from django.db import models

# Create your models here.
class Consequence(models.Model):
    consequence_text = models.CharField(max_length=20)
    def __str__(self):
        return self.consequence_text


class MissingInfo(models.Model):
    consequence = models.ForeignKey(Consequence, on_delete=models.CASCADE)
    missinginfo_text = models.CharField(max_length=200)
    def __str__(self):
        return self.missinginfo_text

class ManualComments(models.Model):
    consequence = models.ForeignKey(Consequence, on_delete=models.CASCADE)
    missinginfo_id = models.IntegerField(default=0)     
    missinginfo_text = models.CharField(max_length=200) 
    comments_text = models.CharField(max_length=200)
    operator = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    mod_date = models.DateTimeField('date modified')
    def __str__(self):
        return self.comments_text

class ManualAddInfo(models.Model):
    consequence = models.ForeignKey(Consequence, on_delete=models.CASCADE)
    missinginfo_id = models.IntegerField(default=0) 
    missinginfo_text = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    operator = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    mod_date = models.DateTimeField('date modified')
    def __str__(self):
        return self.data


class Likelihood(models.Model):
    consequence = models.ForeignKey(Consequence, on_delete=models.CASCADE)
    likelihood_text = models.CharField(max_length=20)
    def __str__(self):
        return self.likelihood_text


class Severity(models.Model):
    consequence = models.ForeignKey(Consequence, on_delete=models.CASCADE)
    severity_text = models.CharField(max_length=20)
    def __str__(self):
        return self.severity_text
