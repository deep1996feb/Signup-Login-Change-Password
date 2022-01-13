# Generated by Django 4.0 on 2022-01-12 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=122)),
                ('lastname', models.CharField(max_length=122)),
                ('username', models.CharField(max_length=122)),
                ('password1', models.IntegerField()),
                ('password2', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]