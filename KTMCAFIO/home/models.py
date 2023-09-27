from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 300)
    email = models.EmailField(max_length= 300)
    subject = models.TextField()
    message = models.TextField()


    def __str__(self):
        return self.name


class Information(models.Model):
    address= models.CharField(max_length = 400)
    phone = models.CharField(max_length= 50)
    email = models.EmailField(max_length = 500)

    def __str__(self):
        return self.address


class About(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=300)
    icon = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Team (models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    designation = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Review (models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    profession = models.CharField(max_length=300)
    description = models.TextField()
    star_rating = models.IntegerField()

    def __str__(self):
        return self.name


class MenuCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


LABELS = (('special', 'special'),)


class MenuItemImage(models.Model):
    slug = models.CharField(max_length=500, unique=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    labels = models.CharField(choices=LABELS, max_length=50, blank=True)

    # def __str__(self):
    #     return self.image


class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    slug = models.CharField(max_length=500, unique=True)
    labels = models.CharField(choices=LABELS, max_length=50, blank = True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    username = models.CharField(max_length = 300)
    slug = models.CharField(max_length= 300)
    quantity = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add= True)
    checkout = models.BooleanField(default = False)
    items = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    items_img = models.ForeignKey(MenuItemImage, on_delete = models.CASCADE)

    def __str__(self):
        return self.username



orderstatuses = (('Pending', 'Pending'), ('Out for Shipping','Out for Shipping'), ('Completed','Completed'))

class Order(models.Model):
    username = models.CharField(max_length = 300, null= False)
    fname = models.CharField(max_length = 300, null= False)
    lname = models.CharField(max_length = 300, null= False)
    email = models.EmailField(max_length = 300, null= False)
    phone = models.CharField(max_length = 300, null= False)
    address = models.TextField(null= False)
    city = models.CharField(max_length = 300, null= False)
    total_price  = models.FloatField(null = False)
    payment_mode = models.CharField(max_length = 300, null= False)
    payment_id = models.CharField(max_length = 300, null= True)
    status = models.CharField(max_length = 300, null= False, choices=orderstatuses, default= 'Pending')
    message = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True, auto_now_add=False)

    def __str__(self):
        return '{} - {}'.format(self.id, self.username)

    def update_status(self, new_status):
        valid_statuses = dict(orderstatuses)
        if new_status not in valid_statuses:
            raise ValueError("Invalid status choice")
        self.status = new_status
        self.save()