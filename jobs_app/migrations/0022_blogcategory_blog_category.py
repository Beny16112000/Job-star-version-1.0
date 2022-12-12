# Generated by Django 4.1.3 on 2022-12-11 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0021_remove_blog_category_delete_blogcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name_plural': 'A14. Blog category',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs_app.blogcategory'),
            preserve_default=False,
        ),
    ]
