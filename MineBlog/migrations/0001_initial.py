# Generated by Django 2.1.2 on 2019-03-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('nickname', models.TextField()),
                ('title', models.TextField()),
                ('content', models.TextField()),
                ('summary', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
