from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from jobs_app.models import Resume, Category, Experience, Education, Army, Skills, Language, AboutYou, Paid, HrRegister, Newsletter, Apply, Contact, Blog, BlogComment, BlogLike, BlogCategory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from xhtml2pdf import pisa
from datetime import datetime


"""
Superuser: 
    username = bsbin6866@gmail.com
    email = bsbin6866@gmail.com
    password = Beny132001
"""


# Create your views here.


def index(request):
    """
    Home Page
    """
    user = request.user
    user_resume = Resume.objects.all()[:10]
    catergory = Category.objects.all()
    blogs = Blog.objects.all()[:3]
    return render(request, 'index.html', {'user':user,'resume':user_resume,'category':catergory,'blogs':blogs})



def sign_up(request):
    """
    Register Page
    """
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if User.objects.filter(username=username):
            messages.error(request, 'The Username already exists please try other Username')
            return redirect('/register')

        if User.objects.filter(email=email):
            messages.error(request, 'The Email already exists please try other Email')
            return redirect('/register')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('/register')

        else:
            new_user = User.objects.create_user(username, email, pass1)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.is_active = True
            new_user.save()

            messages.success(request, 'Your Account successfully created')
            return redirect('/login')
    return render(request, 'register.html')



def sign_in(request):
    """
    Login Page
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('/')
        else:
            messages.error(request, 'Please Try Again') 
    return render(request, 'login.html')



def sign_out(request):
    """
    Logout page
    """
    logout(request)
    messages.success(request, 'You are successfully Logged out')
    return redirect('/')



def resume(request):
    """
    Start To Create Resume
    """
    if request.user.is_authenticated:
        paid = Paid.objects.filter(user=request.user)
        if not paid:
            return redirect('/price')
        else:  
            get_category = Category.objects.all()
            if request.method == 'POST' and request.FILES['img']:
                category = Category.objects.get(id=request.POST['category'])
                img = request.FILES['img']
                job = request.POST['job']
                gender = request.POST['gender']
                age = request.POST['age']
                phone = request.POST['phone']
                location = request.POST['location']
                resume = Resume.objects.create(user=request.user,category=category,img=img,job=job,gender=gender,age=age,phone=phone,location=location)
                resume.save()
                return redirect('/resume/experience')
            return render(request, 'resume.html',{'category':get_category})
    else:
        return redirect('/login')


def add_category(request):
    """
    Add Category Page
    """
    if request.method == 'POST' and request.FILES['img']:
        title = request.POST['title']
        img = request.FILES['img']
        category = Category.objects.create(title=title,img=img)
        category.save()
        messages.success(request, 'Category added')
    return render(request, 'add_category.html')



def experience (requset):
    """
    Add Experience Page
    """
    if requset.method == 'POST':
        job = requset.POST['job']
        company = requset.POST['company']
        start = requset.POST['start']
        end = requset.POST['end']
        description = requset.POST['description']
        only = requset.POST['only']
        experience = Experience.objects.create(user=requset.user,job=job,company=company,start=start,end=end,description=description)
        experience.save()
        if only == 'yes':
            return render(requset, 'experience.html')
        else:
            return redirect('/resume/education')
    return render(requset, 'experience.html')



def education(request):
    """
    Add Education Page
    """
    if request.method == 'POST':
        institution = request.POST['institution']
        edication = request.POST['edication']
        start = request.POST['start']
        end = request.POST['end']
        description = request.POST['description']
        only = request.POST['only']
        institution_save = Education.objects.create(user=request.user,institution=institution,edication=edication,start=start,end=end,description=description)
        institution_save.save()
        if only == 'yes':
            return render(request, 'education.html')
        else:
            return redirect('/resume/army-service')
    return render(request, 'education.html')



def army_service(request):
    """
    Add Army service
    """
    if request.method == 'POST':
        role = request.POST['role']
        start = request.POST['start']
        end = request.POST['end']
        description = request.POST['description']
        army = Army.objects.create(user=request.user,role=role,start=start,end=end,description=description)
        army.save()
        return redirect('/resume/skills')
    return render(request, 'army_service.html')



def skills(request):
    """
    Add Skills PAge
    """
    user_skill = Skills.objects.filter(user=request.user)
    if request.method == 'POST':
        skill = request.POST['skill']
        skills_save = Skills.objects.create(user=request.user,skill=skill)
        skills_save.save()
    return render(request, 'skills.html', {'userSkills': user_skill})



def language(request):
    """
    Add Language Page
    """
    user_languages = Language.objects.filter(user=request.user)
    if request.method == 'POST':
        language_get = request.POST['language']
        language_save = Language.objects.create(user=request.user,language=language_get)
        language_save.save()
    return render(request, 'language.html', {'language':user_languages})



def about_you(request):
    """
    More Details Page
    """
    if request.method == 'POST':
        about = request.POST['aboutYou']
        about_save = AboutYou.objects.create(user=request.user,about=about)
        about_save.save()
        return redirect('/profile')
    return render(request, 'about_you.html')



def profile(request):
    """
    Main Profile Page After Creating Resume
    """
    user = request.user
    resume = Resume.objects.get(user=request.user)
    experience = Experience.objects.filter(user=request.user)
    education = Education.objects.filter(user=request.user)
    army = Army.objects.get(user=request.user)
    skills = Skills.objects.filter(user=request.user)
    language = Language.objects.filter(user=request.user)
    about = AboutYou.objects.get(user=request.user)
    return render(request, 'profile.html',{'resume':resume,'experience':experience,'education':education,'army':army,'skills':skills,'language':language,'about':about,'user':user})



def price(request):
    """
    Price Page
    """
    return render(request, 'price.html')



@login_required
def pay(request):
    """
    Payment page
    """
    if request.method == 'POST':
        card_number = request.POST['cardnumber']
        card_expiration = request.POST['cardexpiration']
        card_csv = request.POST['cardcvc']
        if len(card_number) != 16:
            messages.error(request, 'Card number to short')
        elif len(card_expiration) != 4:
            messages.error(request, 'card expiration to short')
        elif len(card_csv) != 3:
            messages.error(request, 'card CSV to short')
        else:
            paid = Paid.objects.create(user=request.user,paid=True)
            paid.save()
            return redirect('/resume')
    return render(request, 'pay.html',{'user':request.user})



def profile_public(request, username):
    """
    Public profile for HR 
    """
    if not HrRegister.objects.filter(user=request.user,approved=True): # Give To only approve HR's See users profile 
        return redirect('/')
    else:
        user = User.objects.get(username=username)
        resume = Resume.objects.get(user=user)
        experience = Experience.objects.filter(user=user)
        education = Education.objects.filter(user=user)
        army = Army.objects.get(user=user)
        skills = Skills.objects.filter(user=user)
        language = Language.objects.filter(user=user)
        about = AboutYou.objects.get(user=user)
    return render(request, 'public_profile.html',{'resume':resume,'experience':experience,'education':education,'army':army,'skills':skills,'language':language,'about':about,'user':user})



@login_required
def hr_register(request):
    """
    HR register * > need to register as regular user for register as HR < *
    """
    if HrRegister.objects.filter(user=request.user): # check if he still registered
        messages.error(request, 'You alaredy have account')
        return redirect('/')
    if request.method == 'POST':
        company = request.POST['company']
        role = request.POST['role']
        hr = HrRegister(user=request.user,company=company,role=role)
        hr.save()
        return redirect('/')
    return render(request, 'hr_register.html')



@user_passes_test(lambda u: u.is_superuser) # Only superuser can approve 
def approve_HR(request):
    """
    Approve HR users * > Only Superuser Can approve hr's < *
    """
    hr_users = HrRegister.objects.filter(approved=False)
    if request.method == 'POST':
        user_to_approve =  User.objects.get(username=request.POST['approve'])
        hr = HrRegister.objects.get(user=user_to_approve)
        hr.approved = True
        hr.save()
    return render(request ,'approve_hr.html', {'hr':hr_users})



def employees(request):
    """
    All employees page
    """
    all_employees = Resume.objects.all()
    all_categories = Category.objects.all()
    blogs = Blog.objects.all()[:3]
    return render(request, 'employees.html',{'resume':all_employees,'all':all_categories,'blogs':blogs})



def newsletter(request):
    if request.method == 'POST':
        try:
            email = Newsletter.objects.get(email=request.POST['email'])
        except ObjectDoesNotExist:
            save_email = Newsletter(email=request.POST['email'])
            save_email.save()
            message = 'success'
            return redirect(f'/newsletter/{message}')
        else:
            messages.error(request, 'Email alaredy registered to newsletter')
            message = 'error'
            return redirect(f'/newsletter/{message}')



def newsletter_success_error(request, message):
    """
    After registered to newsletter, redirected to current url for success or error.
    """
    if message == 'success':
        message = 'You are registered to the newsletter'
    else:
        message = 'You are alaredy regisdered to the newsletter'        
    return render(request, 'newsletter_message.html',{'message':message})



@login_required
def apply(request, id):
    """
    Send apply to employee that you want start to conect with him
    """
    company = HrRegister.objects.filter(user=request.user)
    if not company:
        return redirect('/employees')
    else:
        receiver = User.objects.get(id=id)
    if request.method == 'POST':
        salary = request.POST['salary']
        message = request.POST['message']
        save_apply = Apply(sender=request.user,company=company[0].company,receiver=receiver,salary=salary,message=message)
        save_apply.save()
        messages.success(request, 'Apply sent')
        return redirect('/employees')
    return render(request, 'apply.html',{'receiver':receiver,'company':company})



def hr_admin_panel(request):
    """
    HR admin panel
    """
    data = Apply.objects.filter(sender=request.user)
    return render(request, 'hr_admin.html',{'data':data})



def hr_admin_full_apply(request, id):
    """
    Full apply review
    """
    data = Apply.objects.get(id=id)
    return render(request, 'hr_admin_apply.html',{'data':data})



def admin_panel(request):
    """
    Regular Admin panel
    """
    data = Apply.objects.filter(receiver=request.user)
    if request.method == 'POST':
        apply_id = request.POST['id']
        apply_update = Apply.objects.get(id=apply_id)
        apply_update.confirm = True
        apply_update.save()
    return render(request, 'admin_panel.html',{'data':data})



def delete_apply(request):
    """
    Delete Apply
    """
    apply_id = request.GET['id']
    apply_delete = Apply.objects.get(id=apply_id)
    apply_delete.delete()
    return redirect('/admin-panel')



def admin_panel_full_apply(request, id):
    """
    Full apply review admin panel
    """
    data = Apply.objects.get(id=id)
    if request.method == 'POST':
        apply_id = request.POST['id']
        apply_update = Apply.objects.get(id=apply_id)
        apply_update.confirm = True
        apply_update.save()
        return redirect('/admin-panel')
    return render(request, 'admin_panel_apply.html',{'data':data})    



def category_page(request, cat_name):
    """
    Job listing by category
    """
    category = Category.objects.get(title=cat_name)
    all_categories = Category.objects.all().exclude(title=category.title)
    resume = Resume.objects.filter(category=category)
    blogs = Blog.objects.all()[:3]
    return render(request, 'category.html',{'resume':resume,'all':all_categories,'category':category,'blogs':blogs})



def search_result(request):
    """
    Search result page
    """
    q = request.GET['q']
    category_search = Category.objects.get(id=request.GET['category'])
    result = Resume.objects.filter(job__icontains=q,category=category_search)
    categories = Category.objects.all().exclude(id=category_search.id) 
    blogs = Blog.objects.all()[:3]
    return render(request, 'search.html',{'result':result,'category':categories,'q':q,'blogs':blogs})



def pdf_download_profile(request, username):
    """
    Download resume from Public profile page, this function gelps to convert html to pdf
    """
    user = User.objects.get(username=username)
    resume = Resume.objects.get(user=user)
    experience = Experience.objects.filter(user=user)
    education = Education.objects.filter(user=user)
    army = Army.objects.get(user=user)
    skills = Skills.objects.filter(user=user)
    language = Language.objects.filter(user=user)
    about = AboutYou.objects.get(user=user)

    template_path = 'profile_pdf.html'
    context = {'resume':resume,'experience':experience,'education':education,'army':army,'skills':skills,'language':language,'about':about,'user':user}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{username}-resume.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    
    if pisa_status.err:
        return HttpResponse('We had sime error <pre>' + html + '</pre>')
    else:
        return response



def contact(request):
    """
    Contact page
    """
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_form = Contact(name=name,email=email,subject=subject,message=message)
        contact_form.save()
        messages.success(request, 'send')
    return render(request, 'contact.html')



def blog(request):
    """
    Main Blog Page - All posts
    """
    blog_posts = Blog.objects.all().order_by('-id')
    categories = BlogCategory.objects.all()
    return render(request, 'blog.html',{'blogs':blog_posts,'categories':categories})



def add_blog_category(request):
    """
    Add Blog Category
    """
    if request.method == 'POST':
        title = request.POST['title']
        try: # Check if the category already exist 
            BlogCategory.objects.get(title=title)
            messages.error(request, 'The category exist')
        except ObjectDoesNotExist:
            blog_category = BlogCategory(title=title)
            blog_category.save()
            messages.success(request, 'The category added')
    return render(request, 'add_blog_category.html')



def add_blog(request):
    """
    Add Blog
    """
    blog_category = BlogCategory.objects.all()
    if request.method == 'POST' and request.FILES['img']:
        title = request.POST['title']
        category = BlogCategory.objects.get(id=request.POST['category'])
        img = request.FILES['img']
        context = request.POST['context']
        blog_save = Blog(user=request.user,title=title,category=category,img=img,context=context,created_at=datetime.now())
        blog_save.save()
        """
        Add here redirect to the post
        """
    return render(request, 'add_blog.html',{'category':blog_category})



def single_blog(request, id):
    """
    Single blog page
    """
    blog_post = Blog.objects.get(id=id)
    blog_likes = BlogLike.objects.filter(blog=blog_post)
    blog_comments = BlogComment.objects.filter(blog=blog_post)
    categories = BlogCategory.objects.all()
    if request.method == 'POST':
        blog_id = Blog.objects.get(id=request.POST['id']) 
        subject = request.POST['subject']
        message = request.POST['message']
        comment_save = BlogComment(user=request.user,blog=blog_id,subject=subject,message=message,created_at=datetime.now())
        comment_save.save()
        messages.success(request, 'Comment added')
    try:
        blog_like = BlogLike.objects.get(user=request.user)
        return render(request, 'single_blog.html',{'blog':blog_post,'likes':blog_likes,'comments':blog_comments,'like':blog_like,'categories':categories})
    except ObjectDoesNotExist:
        return render(request, 'single_blog.html',{'blog':blog_post,'likes':blog_likes,'comments':blog_comments,'categories':categories})



def blog_like_add(request, id):
    """
    Blog like
    """
    print(id)
    blog_post = Blog.objects.get(id=id)
    blog_like = BlogLike(user=request.user,blog=blog_post)
    blog_like.save()
    return redirect(f'/blog/{id}')



def blog_like_remove(request, id):
    """
    Blog unlike
    """
    blog_post = Blog.objects.get(id=id)
    blog_unlike = BlogLike.objects.get(user=request.user,blog=blog_post)
    blog_unlike.delete()
    return redirect(f'/blog/{id}')



def blog_search(request):
    """
    Search blogs
    """
    q = request.GET['q']
    blog_posts = Blog.objects.filter(title__icontains=q)
    categories = BlogCategory.objects.all()
    return render(request, 'blog_search.html',{'blogs':blog_posts,'categories':categories})



def blog_category(request, title):
    """
    Blogs by category
    """
    category = BlogCategory.objects.get(title=title)
    blogs = Blog.objects.filter(category=category)
    categories = BlogCategory.objects.all().exclude(id=category.id) # To get all categories without same category
    return render(request, 'blog_category.html',{'blogs':blogs,'title':title,'categories':categories})



