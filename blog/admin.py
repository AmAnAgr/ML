from django.contrib import admin
from blog.models import BlogPost, Topic, Image

class BlogPostAdmin(admin.ModelAdmin):
  list_display = ('title', 'publish_time',)

admin.site.register(Image)
admin.site.register(BlogPost, BlogPostAdmin)

class BlogPostInLine(admin.StackedInline):
    model = BlogPost
    extra = 1


class TopicAdmin(admin.ModelAdmin):

    inlines = [BlogPostInLine]

admin.site.register(Topic, TopicAdmin)