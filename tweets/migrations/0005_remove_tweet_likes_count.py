# Generated by Django 4.1.3 on 2022-12-09 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_likes_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='likes_count',
        ),
    ]
