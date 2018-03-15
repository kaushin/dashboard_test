from django.db import models

# Create your models here.
class TestResult(models.Model):
    date = models.DateField()
    application = models.CharField(max_length=50)
    result = models.BooleanField()

    def __str__(self):
        return '{0} - {1}'.format(self.date,self.application) 