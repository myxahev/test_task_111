# Generated by Django 4.0.4 on 2022-05-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('answer', models.CharField(max_length=300)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]