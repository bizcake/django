from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    content_at = models.CharField(max_length=8)
    use_yn = models.CharField(max_length=1)
    cnt = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Post_hist(Post):
    
    def __str__(self):
        return self.title
