from django.db import models

# Create your models here.
class Model_Form_Model(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    duration_field = models.DurationField()
    generic_ip_address_field = models.GenericIPAddressField()
    json_field = models.JSONField()
    null_boolean_field = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title 