# Generated by Django 4.2.3 on 2023-07-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_alter_student_teachers_alter_teacher_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(related_name='students', to='school.teacher'),
        ),
    ]
