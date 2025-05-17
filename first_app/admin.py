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

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        print('\n\n\n\n',type(request.user))
        if request.user.has_perm('change_comment'):
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
        return True
    
    def has_view_permission(self, request, obj=None):
        return True


@admin.register(PostAuthor)
class PostAuthorAdmin(BaseAdmin):
    pass