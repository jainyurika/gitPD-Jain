from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from accounts.models import Account

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60, null=False, verbose_name="Title")
    description = models.TextField(
        max_length=5000, null=False, verbose_name="Description"
    )
    upvotecount = models.IntegerField(default=0, verbose_name="Upvote Count")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Post Created On")
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.TextField(
        max_length=5000, null=True, verbose_name="Description"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Comment Created On")


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title).title()
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)