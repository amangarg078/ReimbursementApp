from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Reimbursement(models.Model):
    user = models.ForeignKey(User)
    amount = models.FloatField(blank=False)
    description = models.CharField(max_length=256)
    attachment = models.ImageField(upload_to=user_directory_path)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    reimbursed_flag = models.BooleanField(default=False)
    date_reimbursed = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return '%s - %s' % (self.user.username, self.description)


