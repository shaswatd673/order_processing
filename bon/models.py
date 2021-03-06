from django.db import models
from phone_field import PhoneField
from PIL import Image
from datetime import datetime,timedelta

# Create your models here.
class parts(models.Model):

    PartID = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    vendorID = models.ForeignKey('vendor', on_delete=models.CASCADE)
    partType = models.CharField(max_length=10)
    weight = models.FloatField('Weight(in grams)')
    height = models.FloatField('Height(in cm)')
    width = models.FloatField('Width(in cm')
    length = models.FloatField('Length(in cm')
    cost = models.IntegerField('Cost(in rupees')
    image = models.ImageField(upload_to='parts', default='abc.jpg')

    def __str__(self):
        return self.PartID


class vendor(models.Model):

    vendorID = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    poc = models.CharField('Point of contact(name)',max_length=20)
    contact = PhoneField(blank=True, help_text='Contact phone number')
    city = models.CharField(max_length=20)
    Address = models.TextField()
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class modules(models.Model):

    designID = models.CharField(max_length=10, primary_key=True, default='000')
    name = models.CharField(max_length=20, default='aaaa')
    description = models.TextField( default='none')
    Type = models.CharField(max_length=10, default='aaaa')
    made = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='media/modules', default='abc.jpg')
    inventory = models.IntegerField(default=0)
    design_fee = models.IntegerField('design_fee(in rupees)', default=0)
    assembly_fee = models.IntegerField('per_piece_assembly_fee(in rupees', default=0)
    parts = models.IntegerField('Number of parts',default=0)
    Sub_modules = models.IntegerField('Number of modules', default=0)
    Total_cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class part_list(models.Model):

    designID = models.ForeignKey('modules', on_delete=models.CASCADE)
    PartID = models.ForeignKey('parts',on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return "DesignID :{}, PartID :{}".format(self.designID,self.PartID)


    class Meta:
        unique_together = (('designID','PartID'))


class sub_module_list(models.Model):

    designID = models.ForeignKey('modules', on_delete = models.CASCADE, related_name = 'Module')
    subID = models.ForeignKey('modules', on_delete=models.CASCADE, related_name = 'Sub_Module')
    quantity = models.IntegerField()

    def __str__(self):
        return "Product :{}, Sub_module :{}".format(self.designID, self.subID)

    class Meta:
        unique_together = (('designID','subID'))


class customer(models.Model):

    CustomerID = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    City = models.CharField(max_length=15)
    Address = models.TextField()
    pin = models.CharField(max_length=6)
    poc = models.CharField('point of contact(name)', max_length=20)
    contact = PhoneField(help_text = "phone number of the company or poc")

    def __str__(self):
        return self.name+", "+self.City


'''class due_date_helper(models.Model):
    due_date = models.DateTimeField()

    @classmethod
    def create(cls, placed, due):
        due_date = cls(placed=placed)
        due_days = timedelta(days=due)
        due_date += due_days
        return due_date'''


class orders(models.Model):

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Scheduled','Scheduled'),
        ('delayed','delayed'),
        ('Deliveried','Deliveried'),
        ('Shipped','Shipped'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled')
    )

    orderID = models.CharField(max_length=30, primary_key=True)
    placed = models.DateTimeField(auto_now=True)
    customerID = models.ForeignKey('customer', on_delete=models.CASCADE)
    due =  models.IntegerField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='Active')
    status_description = models.TextField(default='None')
    Total_cost = models.IntegerField(default=0)
    product_count = models.IntegerField(default=0)
    
    def _get_due_date(self):
        return self.placed+timedelta(days=self.due)

    due_date = property(_get_due_date)


    def save(self,*args, **kwargs):

        create=False

        try:
            print(self.due_date)

        except TypeError:
            create=True

        if create:
            print("create triggered")
            return super(orders,self).save()

        else:
            kwargs.setdefault('update_fields',['Total_cost','product_count','status','status_description'])
            print("update triggered")
            return super(orders,self).save(**kwargs)

    def __str__(self):
        return self.orderID



class product_list(models.Model):

    productID = models.ForeignKey('modules', on_delete=models.CASCADE)
    orderID = models.ForeignKey('orders', on_delete=models.CASCADE)
    quantity = models.IntegerField()



    
