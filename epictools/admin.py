__author__ = 'sean'

# Aaron Neuhauser, Sean Fallon
# Date Created: 7-1-2012
# Date Changed:

from django.contrib import admin

from epictools.models import epicTools, Post

class epicToolsAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug":("name",)}
    list_display = ('active', 'name', 'description', 'user')
    list_display_links = ('name',)
    list_editable = ('active',)
    list_filter = ('modified', 'created', 'active')

class PostAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug":("title",)}
    list_display = ('active', 'title', 'excerpt', 'active', 'publish_at')
    list_display_links = ('title',)
    list_editable = ('active',)
    list_filter = ('publish_at', 'modified', 'created', 'active')
    date_hierarchy =  'publish_at'
    search_fields = ['title', 'excerpt', 'body', 'blog__name', 'blog__user__username',]
    fieldsets = (

        (None, {
            'fields': ( 'title', 'blog'),


        }),


        ('Publication', {
            'fields': ('active', 'publish_at'),
            'description': "Control <strong>whether</strong> and <strong>when</strong> a post is visible to the world.",
        }),

        ('Content', {
            'fields':('excerpt','body', 'tags')
        }),

        ('Optional',{
         'fields': ('slug',),
         'classes': ('collapse',),
         })
    )


admin.site.register(epicTools, epicToolsAdmin)
admin.site.register(Post, PostAdmin)
