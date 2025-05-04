from django.contrib.auth.models import User
from django.db import IntegrityError, models
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import randrange

from rest_framework.fields import empty


# Contact model to store additional information related to a user.
class Contact(models.Model):
    linked_user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=256, null=True)
    initial = models.CharField(max_length=2, editable=False)
    color = models.CharField(max_length=128, blank=True, editable=False)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ["name"]

    def __str__(self):
        return self.name

    # Method to generate initials from the contact's name.

    def get_initial(self):
        name_parts = self.name.strip().split()
        if len(name_parts) == 1:
            return name_parts[0][0].upper()
        return name_parts[0][0].upper() + name_parts[1][0].upper()

    # Set the contact's fields based on the linked user.

    def set_fields(self):
        if self.linked_user:
            self.name = self.linked_user.get_full_name().title()
            self.email = self.linked_user.email or ""
            self.phone = None
            self.color = self.get_random_color()

    # Generate a random color for the contact.

    def get_random_color(self):
        num = randrange(100000, 1000000)
        self.color = '#' + str(num)
        return self.color

    # Override save method to set the necessary fields and handle errors.

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        try:

            if self.linked_user and is_new:
                self.set_fields()
            else:
                if self.color == '':
                    self.color = self.get_random_color()
                if self.name:
                    self.name = self.name.title()
            self.initial = self.get_initial()
            super().save(*args, **kwargs)
        except IntegrityError:
            print("Already exists!")
        except Exception as e:
            raise


# Signal to create a contact when a new user is created, excluding superusers.
@receiver(post_save, sender=User)
def create_contact_for_new_user(sender, instance, created, **kwargs):
    if created and not instance.is_superuser:
        contact, created = Contact.objects.update_or_create(
            linked_user=instance,
            defaults={
                "name": instance.get_full_name(),
                "email": instance.email
            }
        )
