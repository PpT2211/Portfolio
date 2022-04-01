from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body)>25:
            return self.body[:25] + ' ...'
        else:
            return self.body

    def pub_date_noice(self):
        return self.pub_date.strftime('%b %e %Y')
