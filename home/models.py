from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model


User = get_user_model()

class Serie(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='image/')
    genre = models.ManyToManyField('Genre')
    realisateur = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Episode(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    synopsis = models.TextField()
    video = models.FileField(upload_to='video/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to='image/')
    synopsis = models.TextField()
    realisateur = models.CharField(max_length=30)
    genre = models.ManyToManyField('Genre')
    video = models.FileField(upload_to='video/')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post
