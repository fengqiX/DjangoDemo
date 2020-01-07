from django.db import models

# Create your models here.

class Subject(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    intro = models.CharField(max_length=511,default='',verbose_name='introduction')
    create_date=models.DateField(null=True)
    is_hot= models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Teacher(models.Model):
    no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    detail=models.CharField(max_length=1023,default='',blank=True)
    photo=models.CharField(max_length=1023,default='')
    good_count=models.IntegerField(default=0)
    bad_count=models.IntegerField(default=0)
    subject = models.ForeignKey(to=Subject,on_delete=models.PROTECT,db_column='sno')