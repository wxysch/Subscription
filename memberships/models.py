from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your models here.
MEMBERSHIP_CHOICES = (
    ('Enterprise', 'ent'),
    ('Professional', 'pro'),
    ('Free','free')
)

class Memberships(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(max_length=30,
                                       choices=MEMBERSHIP_CHOICES,
                                       default='Free')
    price=models.IntegerField(default=15)
    stripe_plan_id=models.CharField(max_length=40)

    def __str__(self):
        return self.membership_type
    
class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank=True,null=True)
    stripe_customer_id=models.CharField(max_length=40)
    membership = models.ForeignKey(Memberships,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.user.username
    
def post_save_usermembership_create(sender,instance, created, *args, **kwargs):
    if created:
        UserMembership.objects.get_or_create(user=instance)
    user_membership,created=UserMembership.objects.get_or_create(user=instance)
    if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id== '':
        new_customer_id=stripe.Customer.create(email=instance.email)
        user_membership.stripe_customer_id = new_customer_id["id"]
        user_membership.save()

post_save.connect(post_save_usermembership_create, sender=settings.AUTH_USER_MODEL)

class Subcription(models.Model):
    user_membership = models.ForeignKey(UserMembership,on_delete=models.CASCADE,blank=True,null=True)
    stripe_subcription = models.CharField(max_length=40)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username