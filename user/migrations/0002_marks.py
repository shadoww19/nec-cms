# Generated by Django 2.2.3 on 2019-08-06 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('subject1', models.IntegerField(db_column='Subject 1')),
                ('subject2', models.IntegerField(db_column='Subject 2')),
                ('subject3', models.IntegerField(db_column='Subject 3')),
                ('collegeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]