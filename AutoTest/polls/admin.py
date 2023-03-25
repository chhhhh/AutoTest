from django.contrib import admin
from .models import Subject, Teacher, User


# Register your models here.
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'intro', 'is_hot')
    search_fields = ('name', )
    ordering = ('no', )


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'good_count', 'bad_count', 'subject')
    search_fields = ('name', )
    ordering = ('no', )


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'tel', 'reg_date', 'last_visit')
    ordering = ('no', )


admin.site.register(Subject, SubjectModelAdmin)
admin.site.register(Teacher, TeacherModelAdmin)
admin.site.register(User, UserAdmin)
