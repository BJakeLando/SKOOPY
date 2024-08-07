from django.db import models


class Tenant(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('User Email')


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Property(models.Model):
    landlord = models.CharField('Landlord Name', max_length=120)
    address =  models.CharField('Address', max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    date = models.DateField('Date lived')
    description =  models.TextField('Description', max_length=1000)
    tenants = models.ManyToManyField(Tenant, blank=True)


    def __str__(self):
        return self.address
    
