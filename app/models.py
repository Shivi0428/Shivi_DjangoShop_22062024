from django.db import models
from django.contrib.auth.models import User

# Instance Model
class Instance(models.Model):
    type = models.CharField(max_length=100)
    vcpus = models.IntegerField()
    memory = models.DecimalField(max_digits=5, decimal_places=2)
    storage = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.type

# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Instance, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.product.type} - {self.quantity}'

# State Choices for Customer Model
STATE_CHOICES = (
    ('Avon', 'Avon'),
    # ... (other states)
    ('Worcestershire', 'Worcestershire')
)

# Customer Model
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

# Category Choices for Product Model
CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
)

# Product Model
class Product(models.Model):
    title = models.CharField(max_length=100, default='')
    selling_price = models.FloatField(default=0.0)
    discounted_price = models.FloatField(default=0.0)
    description = models.TextField(default='')
    brand = models.CharField(max_length=100, default='')
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='')
    product_image = models.ImageField(upload_to='productimg', default='productimg/default.jpg')
    code = models.CharField(max_length=10, default='')
    type = models.CharField(max_length=255, default='')
    vcpus = models.IntegerField(default=0)
    memory = models.FloatField(default=0.0)
    storage = models.CharField(max_length=255, default='')
    network = models.CharField(max_length=255, default='')
    price = models.CharField(max_length=255, default='')
    notes = models.TextField()

    def __str__(self):
        return self.title

    @property
    def total_cost(self):
        return self.quantity * self.discounted_price


class Sorder(models.Model):
    AC = models.CharField(max_length=50)
    desc1 = models.CharField(max_length=255)
    SINTONO = models.IntegerField()
    DDATE = models.DateField()

    NOTES = models.CharField(max_length=255, blank=True, null=True)

class Soitem(models.Model):
    PRODUCT = models.CharField(max_length=50)
    UNITPRICE = models.DecimalField(max_digits=19, decimal_places=2)
    desc1 = models.CharField(max_length=255)
    VATRATE = models.DecimalField(max_digits=19, decimal_places=2, default='2.00')
    SINTONO = models.IntegerField()

    QTY = models.IntegerField()
    NOTES = models.CharField(max_length=255, blank=True, null=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

# Order Status Choices
STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)

# OrderPlaced Model
class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Static(models.Model):
    cperiod = models.CharField(max_length=10)
    nsintono = models.IntegerField()
    nsorec = models.IntegerField()
    ninvno = models.IntegerField()

class V_Lorders(models.Model):
    ac = models.CharField(max_length=10)
    date = models.DateField()
    itotal = models.FloatField()
    ono = models.CharField(max_length=10)
    vat = models.FloatField()
    sintono = models.IntegerField()
    invno = models.IntegerField()
    iprinted = models.BooleanField()
    notes = models.TextField()
    type = models.CharField(max_length=1)
    period = models.CharField(max_length=10)

class V_Loitems(models.Model):
    product = models.CharField(max_length=50)
    unitprice = models.FloatField()
    desc1 = models.CharField(max_length=100)
    vatrate = models.FloatField()
    psize = models.CharField(max_length=50)
    lineno = models.IntegerField()
    sorec = models.IntegerField()
    sintono = models.IntegerField()
    ub = models.CharField(max_length=50)
    ddate = models.DateField()
    qtyinpack = models.IntegerField()
    qty = models.IntegerField()
    notes = models.TextField()
