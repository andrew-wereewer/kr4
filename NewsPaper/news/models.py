from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Author(models.Model):
  user=models.OneToOneField(User, on_delete = models.CASCADE)
  rating=models.IntegerField(default=0)

  def update_rating(self):
    self.rating = Post.objects.filter(author_id=self.id).aggregate(Sum('rating'))['rating__sum']*3 + \
      Comment.objects.filter(user_id=self.user.id).aggregate(Sum('rating'))['rating__sum'] + \
      Comment.objects.filter(post_id__in = [q['id'] for q in Post.objects.filter(author_id=self.id).values('id')]).aggregate(Sum('rating'))['rating__sum']
    self.save()

class Category(models.Model):
  name=models.TextField(unique=True)

class Post(models.Model):
  author=models.ForeignKey(Author, on_delete = models.CASCADE)
  isnews=models.BooleanField(default = False)
  created=models.DateTimeField(auto_now_add=True)
  categories=models.ManyToManyField(Category, through = 'PostCategory')
  title=models.CharField(max_length = 64)
  text=models.CharField(max_length = 4096)
  rating=models.IntegerField(default=0)
  
  def preview():
    return (text[:124] + '...') if len(text) > 124 else text
  
  def like(self):
    self.rating += 1
    self.save()

  def dislike(self):
    self.rating -= 1
    self.save()

class PostCategory(models.Model):
  post=models.ForeignKey(Post, on_delete = models.CASCADE)
  category=models.ForeignKey(Category, on_delete = models.CASCADE)
 
class Comment(models.Model):
  post=models.ForeignKey(Post, on_delete = models.CASCADE)
  user=models.ForeignKey(User, on_delete = models.CASCADE)
  text=models.CharField(max_length = 4096)
  created=models.DateTimeField(auto_now_add=True)
  rating=models.IntegerField(default=0)

  def like(self):
    self.rating += 1
    self.save()

  def dislike(self):
    self.rating -= 1
    self.save()
