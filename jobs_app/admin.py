from django.contrib import admin
from jobs_app.models import Resume, Category, Experience, Education, Army, Skills, Language, AboutYou, Paid, HrRegister, Newsletter, Apply, Contact, Blog, BlogComment, BlogLike, BlogCategory


# Register your models here.


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user','job')
admin.site.register(Resume, ResumeAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Category, CategoryAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('user','job')
admin.site.register(Experience, ExperienceAdmin)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('user','edication')
admin.site.register(Education, EducationAdmin)

class ArmyAdmin(admin.ModelAdmin):
    list_display = ('user','role')
admin.site.register(Army, ArmyAdmin)

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('user','skill')
admin.site.register(Skills, SkillsAdmin)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('user','language')
admin.site.register(Language, LanguageAdmin)

class AboutYouAdmin(admin.ModelAdmin):
    list_display = ('user',)
admin.site.register(AboutYou, AboutYouAdmin)

class PaidAdmin(admin.ModelAdmin):
    list_display = ('user','paid')
admin.site.register(Paid, PaidAdmin)

class HrRegisterAdmin(admin.ModelAdmin):
    list_display = ('user','company','approved')
admin.site.register(HrRegister, HrRegisterAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email',)
admin.site.register(Newsletter, NewsletterAdmin)

class ApplyAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver','confirm')
admin.site.register(Apply, ApplyAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject')
admin.site.register(Contact, ContactAdmin)

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(BlogCategory, BlogCategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('user','title','created_at')
admin.site.register(Blog, BlogAdmin)

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('user','subject','blog','created_at')
admin.site.register(BlogComment, BlogCommentAdmin)

class BlogLikeAdmin(admin.ModelAdmin):
    list_display = ('user','blog')
admin.site.register(BlogLike, BlogLikeAdmin)
