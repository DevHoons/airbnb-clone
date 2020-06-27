# Generated by Django 2.2.5 on 2020-06-27 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_login_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('github', 'Github'), ('kakao', 'Kakao')], default='email', max_length=50),
        ),
    ]
