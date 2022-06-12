# Generated by Django 4.0.1 on 2022-03-12 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_delete_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_title', models.CharField(max_length=100)),
                ('m_date_and_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('m_summary', models.TextField(default='')),
                ('m_categories', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]