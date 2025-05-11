from django.contrib import admin
from first_app.models import BlogPost, Comment, PostAuthor

@admin.action(description="make post to shown")
def make_shown(self, request, queryset):
    queryset.update(is_shown=True)

class BaseAdmin(admin.ModelAdmin):

    actions = ['hard_delete']

    @admin.action(description="clear deleted objects from server")
    def hard_delete(self, request, queryset):
        queryset.delete()


@admin.register(BlogPost)
class BlogPostAdmin(BaseAdmin):
    list_display=('title', 'is_shown', 'created_at')
    list_filter=('is_shown','title')


@admin.register(Comment)
class CommentAdmin(BaseAdmin):
    list_display=('id', 'blog_post', 'author')
    search_fields=('blog_post__title','author')
    raw_id_fields = ('blog_post',)

@admin.register(PostAuthor)
class PostAuthorAdmin(BaseAdmin):
    pass