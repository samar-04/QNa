# Generated by Django 3.2.6 on 2021-08-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='post_q',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pquestion', models.CharField(max_length=1000)),
                ('puser', models.CharField(max_length=100)),
            ],
        ),
    ]
