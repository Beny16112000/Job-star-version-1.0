from django.urls import path
from jobs_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.sign_up,name='sign_up'),
    path('login',views.sign_in,name='sign_in'),
    path('logout',views.sign_out,name='sign_out'),
    path('resume',views.resume,name='resume'),
    path('add-category',views.add_category,name='add_category'),
    path('resume/experience',views.experience,name='experience'),
    path('resume/education',views.education,name='education'),
    path('resume/army-service',views.army_service,name='army_service'),
    path('resume/skills',views.skills,name='skills'),
    path('resume/language',views.language,name='language'),
    path('resume/about-you',views.about_you,name='about_you'),
    path('profile',views.profile,name='profile'),
    path('price',views.price,name='price'),
    path('price/pay',views.pay,name='pay'),
    path('profile/<str:username>',views.profile_public,name='profile_public'),
    path('hr-register',views.hr_register,name='hr_register'),
    path('approve-hr',views.approve_HR,name='approve_HR'),
    path('employees',views.employees,name='employees'),
    path('newsletter',views.newsletter,name='newsletter'),
    path('newsletter/<str:message>',views.newsletter_success_error,name='newsletter_success_error'),
    path('apply/<int:id>',views.apply,name='apply'),
    path('hr-panel',views.hr_admin_panel,name='hr_admin_panel'),
    path('hr-panel/requests/<int:id>',views.hr_admin_full_apply,name='hr_admin_full_apply'),
    path('admin-panel',views.admin_panel,name='admin_panel'),
    path('admin-panel/delete-apply',views.delete_apply,name='delete_apply'),
    path('admin-panel/requests/<int:id>',views.admin_panel_full_apply,name='admin_panel_full_apply'),
    path('category/<str:cat_name>',views.category_page,name='category_page'),
    path('search-result',views.search_result,name='search_result'),
    path('profile/pdf/<str:username>', views.pdf_download_profile,name='pdf_download_profile'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('add-blog',views.add_blog,name='add_blog'),
    path('add-blog-category',views.add_blog_category,name='add_blog_category.html'),
    path('blog/<int:id>',views.single_blog,name='single_blog'),
    path('blog/like/<int:id>',views.blog_like_add,name='blog_like_add'),
    path('blog/unlike/<int:id>',views.blog_like_remove,name='blog_like_remove'),
    path('blog/search',views.blog_search,name='blog_search'),
    path('blog/category/<str:title>',views.blog_category,name='blog_category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)