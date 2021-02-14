# Generated by Django 3.0.3 on 2020-02-22 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hello',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=34, null=True)),
                ('title', models.CharField(blank=True, max_length=13, null=True)),
            ],
            options={
                'db_table': 'hello',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('picture', models.TextField()),
                ('role', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('content', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('edited', models.IntegerField()),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Theme')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User')),
            ],
        ),
    ]
