# Generated by Django 4.1.3 on 2022-12-09 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_alter_tweet_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='likes_count',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]
