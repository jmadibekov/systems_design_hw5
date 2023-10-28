from django.contrib import admin

from .models import User, Group, UserGroup, PopupGroup, AdPopup

admin.site.register(User)
admin.site.register(Group)
admin.site.register(UserGroup)
admin.site.register(PopupGroup)
admin.site.register(AdPopup)
