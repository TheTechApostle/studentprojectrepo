# Generated by Django 5.1.6 on 2025-03-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0002_projectidea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='documents/')),
                ('summary', models.TextField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
