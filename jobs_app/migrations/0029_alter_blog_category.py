# Generated by Django 4.1.3 on 2022-12-11 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0028_blog_blogcategory_blogcomment_replayoncomment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='jobs_app.blogcategory'),
        ),
    ]
