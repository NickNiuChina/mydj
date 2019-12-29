from django.contrib import admin

# Register your models here.

from .models import Publisher, Author, Book


class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ('first_name', 'last_name')
	list_filter = ('first_name',)


class BookAdmin(admin.ModelAdmin):

	# show_authors 是用来获取外键的多关系的，Book.author.all() 中, author为在外键所在的表, 寻找作者names

	# def show_authors(self, obj):

		# author_list = []

		# for author in obj.authors.all():
		# 	author_list.append(author.first_name + '-' + author.last_name)
		# return ','.join(author_list)

	list_display = ('title', 'show_authors', 'publisher', 'publication_date')
	# filter_horizontal = ('authors',)  
	raw_id_fields = ('authors',)    # 只针对外键的
	list_filter = ('publication_date',)
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)
	filter_horizontal = ('authors',)
	raw_id_fields = ('publisher',)


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
