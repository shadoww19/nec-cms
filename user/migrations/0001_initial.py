# Generated by Django 2.2.3 on 2019-08-05 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('collegeId', models.CharField(db_column='College Id', max_length=20)),
                ('name', models.CharField(db_column='Name', max_length=500)),
                ('email', models.CharField(db_column='Email', max_length=500)),
                ('password', models.CharField(db_column='Password', max_length=1000)),
                ('role', models.CharField(db_column='Role', max_length=50)),
            ],
        ),
    ]