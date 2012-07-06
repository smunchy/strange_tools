# Author: Sean Fallon
# Shout out to Kenneth Love
# Date Created:
# Date Changed:

# All standard imports used in Django
from django.http import HttpResponse
from django.shortcuts import render_to_response , get_object_or_404
from django.template import RequestContext

# Custom
from epictools.models import epicTools, Post

# request is the httprequest that comes in.
def epictools_index(request):

    epicBlogTools = epicTools.objects.filter(active=True)

     #must have full  path in order to render template.
    return render_to_response('///home/sean/newproject/epictools/templates/index.html', {
        'epicBlogTools': epicBlogTools
        # standard in Django: context_instance=RequestContext(request)
        # context instance built from existing request.
    }, context_instance=RequestContext(request)) # standard in Django: context_instance=RequestContext(request)

    # return HttpResponse("You've reached my epic tool!")

# Two variables: (request, slug)
def epicBlog(request, slug):
    epicBigBlog = get_object_or_404(epicTools, active=True, slug=slug)

    return render_to_response('///home/sean/newproject/epictools/templates/index.html', {
             'epicBigBlog': epicBigBlog
    }, context_instance=RequestContext(request))

