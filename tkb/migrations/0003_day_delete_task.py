# Generated by Django 4.0.4 on 2022-04-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tkb', '0002_delete_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=100)),
                ('day_subj', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
