# Generated by Django 4.1.3 on 2022-12-11 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0019_blog_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs_app.blogcategory'),
            preserve_default=False,
        ),
    ]