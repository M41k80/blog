# Generated by Django 5.1.2 on 2024-10-16 23:08

import apps.blog.models
import ckeditor.fields
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('slug', models.SlugField(max_length=254, unique=True)),
                ('thumbnail', models.ImageField(max_length=700, upload_to=apps.blog.models.blog_thumbnail_directory)),
                ('description', models.TextField(max_length=254)),
                ('content', ckeditor.fields.RichTextField()),
                ('time_read', models.IntegerField()),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('views', models.IntegerField(blank=True, default=0)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.category')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=254)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogpost_view_count', to='blog.post')),
            ],
        ),
    ]
