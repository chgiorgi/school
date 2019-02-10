import misaka
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from groups.models import Group

# Create your models here.

User = get_user_model()


class Post(models.Model):
	user = models.ForeignKey(get_user_model(), related_name='posts', on_delete=False)
	created_at = models.DateTimeField(auto_now=True)
	message = models.TextField()
	message_html = models.TextField(editable=False)
	group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=False)

	def __str__(self):
		return self.message

	def save(self, *args, **kwargs):
		self.message_html = misaka.html(self.message)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('posts:single',
					   kwargs={'username': self.user.username,
							   'pk': self.pk})

	class Meta:
		ordering = ['-created_at']
		unique_together = ['user', 'message']
