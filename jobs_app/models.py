from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField(upload_to='media/category_images')

    class Meta:
        verbose_name_plural = '1. Category'


class Resume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,models.CASCADE)
    img = models.ImageField(upload_to='media/resume_images')
    job = models.CharField(max_length=200)
    gender = models.CharField(max_length=150)
    age = models.FloatField()
    phone = models.FloatField()
    location = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = '2. Resume'


class Experience(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    job = models.CharField(max_length=150)
    company = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField()
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = '3. experience'


class Education(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    institution = models.CharField(max_length=150)
    edication = models.CharField(max_length=150)
    start = models.DateField()
    end = models.DateField()
    description = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = '4. education'


class Army(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    start = models.DateField()
    end = models.DateField()
    description = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = '5. army service'


class Skills (models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    skill = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = '6. skills'


class Language(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    language = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = '7. language'


class AboutYou(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    about = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = '8. About You'


class Paid(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '9. Paid Status'


class HrRegister(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.CharField(max_length=40)
    role = models.CharField(max_length=40)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'A10. HR users'


class Newsletter(models.Model):
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name_plural = 'A11. Newsletter'


class Apply(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    company = models.CharField(max_length=255)
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    salary = models.IntegerField()
    message = models.TextField(blank=True)
    confirm = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'A12. Apply`s'


class Contact(models.Model):
    name = models.CharField(max_length=54)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'A13. Contact'


class BlogCategory(models.Model):
    title = models.CharField(max_length=70)

    class Meta:
        verbose_name_plural = 'A14. Blog category'    


class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory,db_constraint=False,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=400)
    img = models.ImageField(upload_to='media/blog_images')
    context = models.TextField(blank=True)
    created_at = models.DateField()

    class Meta:
        verbose_name_plural = 'A15. Blog Post'


class BlogComment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    subject = models.CharField(max_length=254)
    message = models.TextField(blank=True)
    created_at = models.DateField()

    class Meta:
        verbose_name_plural = 'A16. Blog comment'


class BlogLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,models.CASCADE)

    class Meta:
        verbose_name_plural = 'A17. Blog Like'



