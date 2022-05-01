from django.contrib import admin
from .models import Skill, Social, Profile, Project, ProjectView, SessionIPUrlKey

class SkillAdmin(admin.ModelAdmin):
	
	list_display = ('name', 'imagename')
	list_filter = ('name', 'imagename')
	search_fields = ('name', 'imagename')

class SocialAdmin(admin.ModelAdmin):

	list_display = ('name', 'imagename', 'link')
	list_filter = ('name', 'imagename', 'link')
	search_fields = ('name', 'imagename', 'link')

class ProfileAdmin(admin.ModelAdmin):

	list_display = ('user', 'imagename', 'bio')
	list_filter = ('user', 'imagename', 'bio')
	search_fields = ('user', 'imagename', 'bio')

class ProjectAdmin(admin.ModelAdmin):

	list_display = ('title', 'dateposted', 'author', 'imagename', 'shortcontent', 'slug', 'repo')
	list_filter = ('title', 'dateposted', 'author', 'imagename', 'shortcontent', 'slug', 'repo')
	search_fields = ('title', 'dateposted', 'author', 'imagename', 'shortcontent', 'slug', 'repo')

class ProjectViewAdmin(admin.ModelAdmin):

	list_display = ('project', 'view')
	list_filter = ('project', 'view')
	search_fields = ('project', 'view')

class SessionIPUrlKeyAdmin(admin.ModelAdmin):

	list_display = ('sessionipurlkey',)
	list_filter = ('sessionipurlkey',)
	search_fields = ('sessionipurlkey',)

admin.site.register(Skill, SkillAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectView, ProjectViewAdmin)
admin.site.register(SessionIPUrlKey, SessionIPUrlKeyAdmin)