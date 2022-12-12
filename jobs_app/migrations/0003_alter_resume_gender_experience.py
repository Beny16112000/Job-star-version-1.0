# Generated by Django 4.1.3 on 2022-11-14 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs_app', '0002_category_alter_resume_options_resume_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=200)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('description', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '3. experience',
            },
        ),
    ]
