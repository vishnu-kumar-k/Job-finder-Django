# Generated by Django 4.0.4 on 2022-05-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='explore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('job_tittle', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='explore')),
                ('refer', models.CharField(max_length=400)),
                ('salary', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=400)),
            ],
        ),
        migrations.DeleteModel(
            name='background',
        ),
    ]