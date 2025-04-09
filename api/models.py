from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=100,)
    estate_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, blank=True, null=True, default=None)
    phone_number = models.CharField(max_length=15)
    img = models.ImageField(upload_to='agents/', default="agents/image2_resized.jpg")
    language = models.JSONField()
    verifications = models.BooleanField(default=False)
    rating = models.FloatField()
    STATE_CHOICES = [
    ('Haryana', 'Haryana'),
    ('Delhi', 'Delhi'),
    ('Punjab', 'Punjab'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
     ]
    state = models.CharField(
     max_length=20,
     choices=STATE_CHOICES,
     blank=True,
     null=True,
     default=None
    )


class Property(models.Model):
    STATE_CHOICES = [
    ('Haryana', 'Haryana'),
    ('Delhi', 'Delhi'),
    ('Punjab', 'Punjab'),
    ('Uttar Pradesh','Uttar Pradesh'),
     ]
    state = models.CharField(
     max_length=20,
     choices=STATE_CHOICES,
     blank=True,
     null=True,
     default=None
    )


    address = models.TextField()
    acre_price = models.FloatField()
    acre = models.FloatField()
    available = models.BooleanField(default=True)
    isvaild = models.BooleanField(default=False)
    road_width = models.IntegerField()
    land_category = models.CharField(max_length=100)
    district_name = models.CharField(max_length=100)
    tehsil_name = models.CharField(max_length=100)
    locations_link = models.URLField()
    img = models.ImageField(upload_to='properties/', default="properties/auzC7uegAL4sn1cfSKP1_Cj3YoZB.jpg")
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='properties')
    subagent =  models.TextField(blank=True, null=True, default=None)

    footter = models.FloatField( blank=True, null=True, default=None)

    layout = models.ImageField(upload_to='properties/', default="properties/auzC7uegAL4sn1cfSKP1_Cj3YoZB.jpg")
    village_name = models.CharField(max_length=120, blank=True, null=True, default=None)

    SALE_OR_LEASE_CHOICES = [
        ('sale', 'Sale'),
        ('lease', 'Lease'),
    ]




    sale_or_lease = models.CharField(max_length=10, choices=SALE_OR_LEASE_CHOICES, default='sale')  # Fixed field

    unitofland = [
    ('Acres', 'Acres'),
    ('Square Feet', 'Square Feet'),
    ('Gaj', 'Gaj'),
    ('Square Meters', 'Square Meters'),
    ('Yard', 'Yard'),
    ]

    unit_of_land = models.CharField(max_length=20, choices=unitofland, default='acres')

    money_units = [
    ('Thousand', 'Thousand'),
    ('Lakh', 'Lakh'),
    ('Crore', 'Crore'),
     ]

    money_unit = models.CharField(max_length=10, choices=money_units, default='crore')





    eligible_for_clu = models.BooleanField(default=True)  # Removed blank=True, null=True
    zone = models.CharField(max_length=100, blank=True, null=True, default=None)  # Fixed name
    land_facing = models.TextField(blank=True, null=True, default=None)
    nearest_highways = models.TextField(blank=True, null=True, default=None)
    details = models.TextField(blank=True, null=True, default=None)  # Fixed name
    distance_between_delhi = models.IntegerField(blank=True, null=True, default=None)





class GeneralData(models.Model):
    top_rate = models.ManyToManyField(Property, related_name="top_rated")
    featured = models.ManyToManyField(Property, related_name="featured_properties")
    recommendation = models.ManyToManyField(Property, related_name="recommended_properties")

class UserData(models.Model):
    phone = models.CharField(max_length=15,default="Unknown")
    name = models.CharField(max_length=100 , default="Unknown")

