from django.contrib import admin
from .models import Post, Category, Tag
from .models import Post

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)