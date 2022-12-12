# Generated by Django 4.1.3 on 2022-12-11 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0031_alter_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bloglike',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='bloglike',
            name='user',
        ),
        migrations.RemoveField(
            model_name='replayoncomment',
            name='comment_on_comment',
        ),
        migrations.RemoveField(
            model_name='replayoncomment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='BlogCategory',
        ),
        migrations.DeleteModel(
            name='BlogComment',
        ),
        migrations.DeleteModel(
            name='BlogLike',
        ),
        migrations.DeleteModel(
            name='ReplayOnComment',
        ),
    ]