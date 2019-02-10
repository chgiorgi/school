from django.db import models
from django.contrib.auth import models as a_model

# Create your models here.

class User(a_model.User,a_model.PermissionsMixin):

	def __str__(self):
		return "@{}".format(self.username)






