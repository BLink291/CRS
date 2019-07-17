from django.contrib import admin

from .models import Article
# Register your models here.
# admin.site.register(Article)

@admin.register(Article)
class	ArticleAdmin(admin.ModelAdmin):
    list_display	=	('title',	'slug',	'author', 'created' )
    list_filter	    =	('created', )
    search_fields	=	('title',	'body')
    prepopulated_fields	=	{'slug':	('title',) }				
    raw_id_fields	=	('author',)	
    date_hierarchy	=	'created'
    ordering = ('created',)

