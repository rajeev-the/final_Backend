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
    locations_link = models.URLField(null=True, blank=True)
    map_link = models.TextField(max_length=2000, default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d42157498.47345266!2d60.94156072887267!3d19.69240573692257!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30635ff5d23cbb0f%3A0xe1b092d74e10e9c5!2sIndia!5e0!3m2!1sen!2sin!4v1744037809273!5m2!1sen!2sin")
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

