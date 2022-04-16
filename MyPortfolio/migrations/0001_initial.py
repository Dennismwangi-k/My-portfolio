# Generated by Django 4.0.4 on 2022-04-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('description', models.CharField(max_length=200)),
                ('technology', models.CharField(max_length=20)),
            ],
        ),
    ]
