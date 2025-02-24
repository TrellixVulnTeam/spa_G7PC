# Generated by Django 2.2.6 on 2019-12-03 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carriers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('mobileno', models.IntegerField()),
                ('totalexp', models.CharField(max_length=100)),
                ('lastsalary', models.IntegerField()),
                ('fileupload', models.FileField(upload_to='beautyapp/Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Citys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobileno', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beautyapp.Citys')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beautyapp.Services')),
            ],
        ),
    ]
