# Generated by Django 4.1.3 on 2023-04-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birthday', models.DateField(max_length=8)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('subject', models.CharField(choices=[('c1', 'Design and development of drone hardware and software systems'), ('c2', 'Flight testing and data collection'), ('c3', 'Algorithm development and optimization for image processing and navigation'), ('c4', 'Integration of drone systems with other technologies such as GIS, wireless communication, and cloud computing'), ('c5', 'Project management and coordination')], default='c1', max_length=90)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=90)),
            ],
        ),
    ]
