# Aaron Neuhauser, Sean Fallon
# Date Created: 7-1-2012
# Date Changed:

import datetime


from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class PostManager(models.Manager):

    def get_visible(self):
        # lte means less than equal to.
        return self.get_query_set().filter(publish_at__lte=datetime.datetime.now(), active=True)


class TimeStampedActivate(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    active = models.BooleanField(default=False,
                                  help_text="controls whether or not this epic tool is live.")

    class Meta:
        abstract = True


class epicTools(TimeStampedActivate):
    """
    An epic tool belonging to an epic user.
    Epic tools have multiuple tools and one user can have many epic tools.
    """

    name = models.CharField(max_length=255,
                             help_text = "Name of your epic tool. Can be anything up to 255 Characters.")
    slug = models.SlugField()
    description = models.TextField(blank=True,
                                    help_text="Describe your epic tool.")
    user = models.ForeignKey(User, related_name="epictools")

    def __unicode__(self):
        return self.name

    # in order for the link to work in the index.html template, this has been made to link to another page.

    # The @ sign is a decorator in python
    # it takes get_absolute_url function and wraps it in another function called permalink, which uses our named urls.
    @models.permalink
    def get_absolute_url(self):
        # this is returning the view name
        # the empty tuple is for positional arguments.
        # epicBlog is the name of the url.
        return ('epicBlog', (),{
            # the url is going to ask for a slug
            # when it asks for a slug, django will give epicBlog's slug.
            'slug': self.slug
        })



class Post(TimeStampedActivate):

    """
    A Post that belongs to an epic tool

    """

    title = models.CharField(max_length=255, help_text = "Title of the post")

    slug = models.SlugField()
    excerpt = models.TextField(blank=True, help_text = "A small teaser of your comment")
    body = models.TextField()
    publish_at = models.DateTimeField(default=datetime.datetime.now(), help_text = "Date and time post should become visible.")

    blog = models.ForeignKey(epicTools, related_name="posts")
    tags = TaggableManager()
    objects = PostManager()

    def __unicode__(self):
        return self.title

    class Meta:

        # The dashes are showing it's in reverse order.
        # South doesn't recognize order. Only Ordering.
        ordering = ['-publish_at', '-modified', '-created']






