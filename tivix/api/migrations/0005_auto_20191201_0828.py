# Generated by Django 2.2.7 on 2019-12-01 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191201_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='teachers_students', to='api.Student'),
        ),
    ]
