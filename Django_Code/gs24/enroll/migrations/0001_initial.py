# Generated by Django 3.0.2 on 2020-03-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=70)),
                ('stuemail', models.EmailField(max_length=70)),
                ('stupass', models.CharField(max_length=70)),
            ],
        ),
    ]
