from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'middle_name', 'role',
        'is_staff', 'is_superuser', 'is_active', 'created_at', 'updated_at'
    )
    search_fields = ('email', 'first_name', 'last_name', 'middle_name')
    ordering = ('email',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'middle_name', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic', 'full_name')
    search_fields = ('name', 'surname', 'patronymic')

    def full_name(self, obj):
        return f"{obj.name or ''} {obj.surname or ''} {obj.patronymic or ''}".strip()
    full_name.short_description = 'Full Name'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description_short', 'count', 'authors_list', 'created_at')
    filter_horizontal = ('authors',)
    search_fields = ('id', 'name', 'authors__name', 'authors__surname')
    list_filter = ('authors', 'count', 'created_at')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Static Information', {
            'fields': ('name', 'authors', 'count'),
        }),
        ('Dynamic Information', {
            'fields': ('created_at',),
        }),
    )

    def description_short(self, obj):
        if obj.description:
            return (obj.description[:75] + '...') if len(obj.description) > 75 else obj.description
        return ''
    description_short.short_description = 'Description'

    def authors_list(self, obj):
        return ", ".join(f"{author.name or ''} {author.surname or ''}".strip() for author in obj.authors.all())
    authors_list.short_description = 'Authors'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'user_email', 'created_at', 'end_at', 'plated_end_at', 'is_returned')
    list_filter = ('book__id', 'book__name', 'created_at', 'end_at')
    search_fields = ('book__id', 'book__name', 'user__email')
    readonly_fields = ('created_at',)

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'User Email'

    def is_returned(self, obj):
        return obj.end_at is not None
    is_returned.boolean = True
    is_returned.short_description = 'Returned'
