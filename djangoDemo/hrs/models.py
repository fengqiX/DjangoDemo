from django.db import models

# Create your models here.
from django.db import models

class Dept(models.Model):
    no=models.IntegerField(primary_key=True,db_column='dno',verbose_name='department NO.')
    name = models.CharField(max_length=20,db_column='dname',verbose_name='department Name')
    location = models.CharField(max_length=30,db_column='dloc',verbose_name='department locations')

    class Meta:
        db_table = 'tb_dept'

class Emp(models.Model):
    no = models.IntegerField(primary_key=True,db_column='eno',verbose_name='employee NO.')
    name = models.CharField(max_length=30,db_column='ename',verbose_name='employee name')
    job=models.CharField(max_length=30,verbose_name='positions')
    mgr = models.ForeignKey('self',on_delete=models.SET_NULL, null=True,blank=True,verbose_name='Manager')
    sal = models.DecimalField(max_digits=7,decimal_places=2,verbose_name='monthly salary')
    comm = models.DecimalField(max_digits=7,decimal_places=2,null=True, blank=True,verbose_name='subsidy')
    dept=models.ForeignKey(Dept,db_column='dno',on_delete=models.PROTECT,verbose_name='department located')

    class Meta:
        db_table= 'tb_emp'