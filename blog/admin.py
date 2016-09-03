from django.contrib import admin
from .models import Post
from .models import Writing

admin.site.register(Post)
admin.site.register(Writing)