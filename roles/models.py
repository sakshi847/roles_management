from django.db import models

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)  

    def delete(self, *args, **kwargs):
        """ Soft delete instead of hard delete """
        self.status = False
        self.save()

    def __str__(self):
        return self.role_name

