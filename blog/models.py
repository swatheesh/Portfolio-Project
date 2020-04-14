from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    summary = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summ(self):
        return self.summary[0:100]

    def date(self):
        return self.pub_date.strftime('%b %e %Y')
