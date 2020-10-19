from django.contrib import admin
from fApp.models import Post,Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'created', 'updated', 'status']
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    ordering = ('status', 'publish')

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','name','body','date_added']
    search_fields = ('body',)

admin.site.register(Comment,CommentAdmin)
#uername:-raghav
#pa:-raghav1234