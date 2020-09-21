from django.db import models

class Post(models.Model):
    post_text = models.CharField(max_length=200)
    post_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_text


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.comment_text