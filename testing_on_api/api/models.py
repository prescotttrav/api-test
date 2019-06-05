from django.db import models

class API(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_position(self):
        return self.name + ' works as ' + self.position + '.'

    def __repr__(self):
        return self.name + ' is added.'   
