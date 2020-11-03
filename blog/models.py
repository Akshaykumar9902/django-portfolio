from django.db import models

#create a blog models

#Add the Blog app to the settings

#create a migration

#migrate

#add to the admin

class Blog(models.Model):
    #title
    #pub_date 
    #body
    #image

    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    # def __str__(self):
    #     return self.title

    # def summary(self):
    #     return self.body[:100]

    # def pub_date_pretty(self):
    #     return self.pub_date.strftime('%b %e %Y')