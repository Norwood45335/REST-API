from django.db import models

# Create your models here.
#ORM, object relational mapping. It maps a python object to a database instance

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

