# Generated by Django 2.1.4 on 2018-12-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='obras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Obra',
                'verbose_name_plural': 'Obras',
            },
        ),
    ]
