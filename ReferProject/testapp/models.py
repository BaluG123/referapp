from django.db import models
from django.utils import timezone

# Create your models here.
class Apps(models.Model):
    c_choices=(('Trading','trading'),('E-commerce','e-commerce'),('Socialmedia','socialmedia'))
    no=models.IntegerField()
    appname=models.CharField(max_length=128)
    logo=models.FileField(null=True,blank=True,upload_to="media/")
    slug=models.SlugField(max_length=128,unique_for_date='publish')
    category=models.CharField(max_length=11,choices=(c_choices),default='trading')
    description=models.TextField()
    andriod_link=models.CharField(max_length=10000)
    andriod_rate=models.FloatField()
    ios_link=models.CharField(max_length=10000,null=True,blank=True)
    ios_rate=models.FloatField(null=True,blank=True)
    publish=models.DateTimeField(timezone.now)

    class Meta:
        ordering=['-no']

    def __str__(self):
        return self.appname    


