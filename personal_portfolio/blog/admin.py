from django.contrib import admin
from blog.models import Category,Post,Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category),
admin.site.register(Post,PostAdmin),
admin.site.register(Comment,CategoryAdmin),
