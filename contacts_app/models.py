from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Contact(models.Model):
    linked_user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=256, null=True)
    initial = models.CharField(max_length=2, editable=False)
    color = models.CharField(max_length=128, blank=True, )

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ["name"]

    def __str__(self):
        return self.name
    
    def get_initial(self):
        name_parts = self.name.strip().split()
        if len(name_parts) == 1:
            return name_parts[0][0].upper()
        return name_parts[0][0].upper() + name_parts[1][0].upper()
    
    def set_fields(self):
        if self.linked_user:
            self.name = self.linked_user.get_full_name()
            self.email = self.linked_user.email or ""
            self.phone = None
            self.color = "--yellow"

    def save(self, *args, **kwargs):
        if self.linked_user:
            self.set_fields()
        self.initial = self.get_initial()
        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_contact_for_new_user(sender, instance, created, **kwargs):
    if created and not Contact.objects.filter(linked_user=instance).exists():
        Contact.objects.create(
            linked_user=instance,
            name=instance.get_full_name(),
            email = instance.email
        )