# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-14 15:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import register.course.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='assignment/')),
                ('submission_last_date', models.DateTimeField(null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseNo', models.CharField(max_length=20, unique=True)),
                ('course_name', models.CharField(max_length=100, null=True, unique=True)),
                ('credits', models.IntegerField(null=True)),
                ('elective', models.NullBooleanField()),
                ('offered_to', models.CharField(choices=[('CS', 'Computer Science'), ('IT', 'Information Technology'), ('CS&IT', 'Computer Science and Information Technology')], max_length=20, null=True)),
                ('faculty', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='course/', validators=[register.course.validators.validate_file_extension])),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('course_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course', to_field='courseNo')),
                ('faculty', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesInSemester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_electives', models.IntegerField(null=True)),
                ('number_of_core', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfferedIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='coursesinsemester',
            name='semester',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.OfferedIn', to_field='semester'),
        ),
        migrations.AddField(
            model_name='course',
            name='offered_in',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.OfferedIn'),
        ),
        migrations.AddField(
            model_name='assignmentmaterial',
            name='course_no',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course', to_field='courseNo'),
        ),
        migrations.AddField(
            model_name='assignmentmaterial',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
