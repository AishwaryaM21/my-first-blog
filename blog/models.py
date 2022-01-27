from django.conf import settings
from django.db import models
from django.utils import timezone
# Importing essentials to create our blog

class Post(models.Model): 
#Defines our model.Post is the name of our model. models.Model means Post is a Django modelso it is saved in the database
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #ForeignKey is a link to another model
    title = models.CharField(max_length=200)
    #CharField defines text with limited numbers
    text = models.TextField()
    #TextField defines text without limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date =  models.DateTimeField(blank=True , null=True)
    #models.DateTimeFielsd gives the date and time

    def publish(self):
    #def is a function. publish is the name of the method.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        #method often returns something. Here, We will get a text(string) with the Post title