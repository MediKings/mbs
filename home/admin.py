from django.contrib import admin
from .models import Serie, Episode, Post, Genre, Comment


class SerieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class EpisodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Serie, SerieAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Comment)
