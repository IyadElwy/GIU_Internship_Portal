# Generated by Django 4.0 on 2021-12-30 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_studentphonenumbers_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentphonenumbers',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.student'),
        ),
    ]