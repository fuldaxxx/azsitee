# Generated by Django 3.2.6 on 2021-09-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210902_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usernet',
            name='midle_name',
        ),
        migrations.AlterField(
            model_name='usernet',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user/avatar/'),
        ),
        migrations.AlterField(
            model_name='usernet',
            name='first_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usernet',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usernet',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6),
        ),
        migrations.AlterField(
            model_name='usernet',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
