from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Skill(models.Model):

	name = models.CharField(max_length=30)
	imagename = models.CharField(max_length=50)

	def __str__(self):

		return self.name

class Social(models.Model):

	name = models.CharField(max_length=30)
	imagename = models.CharField(max_length=50)
	link = models.CharField(max_length=100)

	def __str__(self):

		return self.name

class Profile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	imagename = models.CharField(max_length=50)
	bio = models.TextField()
	skill = models.ManyToManyField(Skill, blank=False, null=False)
	social = models.ManyToManyField(Social, blank=False, null=False)

	def __str__(self):

		return f'{self.user.username}'

class Project(models.Model):

	title = models.CharField(max_length=30)
	dateposted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	imagename = models.CharField(max_length=50)
	skill = models.ManyToManyField(Skill, blank=False, null=False)
	shortcontent = models.TextField(max_length=300)
	longcontent = RichTextUploadingField()
	slug = models.SlugField(unique=True, blank=True)

	def save(self, *args, **kwargs):

		self.slug = slugify(self.title)
		super(Project, self).save(*args, **kwargs)

	def __str__(self):

		return self.title

class ProjectView(models.Model):

	project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='views')
	view = models.IntegerField(default=0)

	def __int__(self):
		
		return self.view

class SessionIPUrlKey(models.Model):

	sessionipurlkey = models.TextField()

	def __str__(self):

		return self.sessionipurlkey