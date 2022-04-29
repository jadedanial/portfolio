from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Skill, Social, Profile, Project, ProjectView, SessionIPUrlKey
from django.db.models import F

def home(request):

	context = {
		'skills': Skill.objects.all(),
		'socials': Social.objects.all(),
		'profiles': Profile.objects.all(),
		'projects': Project.objects.all(),
		'projectviews': ProjectView.objects.all(),
	}

	for project in Project.objects.all():

		projectobject = ProjectView.objects.filter(project=project)

		if projectobject:

			pass

		else:

			projectView = ProjectView.objects.create(project=project, view=0)
			projectView.save()

	return render(request, 'blog/section.html', context)

def getSession(request):

	if not request.session.session_key:

		request.session.save()

	session_id = request.session.session_key
	return session_id

def getIP(request):

	forwardedfor = request.META.get('HTTP_X_FORWARDED_FOR')

	if forwardedfor:

		ip = forwardedfor.split(',')[0]

	else:

		ip = request.META.get('REMOTE_ADDR')

	return ip

def projectdetail(request, category, pk, slug):

	SessionIPUrl = getSession(request) + getIP(request) + request.build_absolute_uri()

	project = get_object_or_404(Project, pk=pk)

	if(SessionIPUrlKey.objects.filter(sessionipurlkey=SessionIPUrl).count() <= 0):

		Sessionipurlkey = SessionIPUrlKey.objects.create(sessionipurlkey=SessionIPUrl)
		Sessionipurlkey.save()

		if(ProjectView.objects.filter(project=project).count() <= 0):

			projectView = ProjectView.objects.create(project=project, view=1)
			projectView.save()

		else:

			ProjectView.objects.filter(project=project).update(view=F('view') + 1)

	context = {
		'subject': project,
		'profiles': Profile.objects.all(),
		'views': ProjectView.objects.all(),
		'allcontents': Project.objects.all().order_by('title'),
		'category': category
	}

	return render(request, 'blog/post.html', context)