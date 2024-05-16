from django.db import models


class YourModel2(models.Model):
    hello1 = models.CharField(max_length=100)
    hello2 = models.IntegerField()
    # Add more fields as needed


class YourModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    yourmodel2 = models.ForeignKey(YourModel2, on_delete=models.CASCADE,null=True)
    # Add more fields as needed


class Renewal_Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    no_of_days = models.IntegerField()
    status = models.BooleanField(default=True)
    sort_order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name  # Return the name of the instance for better readability


class Instance(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    date_of_admission = models.DateField(null=True)
    subdomain_prefix = models.CharField(max_length=50, unique=True)
    booking = models.IntegerField(default=0, verbose_name='Number of Bookings')
    is_active = models.BooleanField(default=False)
    status = models.BooleanField(default=0)
    sort_order = models.IntegerField(null=True, blank=True)
    renewal_type = models.ForeignKey(Renewal_Type, on_delete=models.CASCADE, related_name='instances', default=1)
    recent_renew_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name  # Return the name of the instance for better readability