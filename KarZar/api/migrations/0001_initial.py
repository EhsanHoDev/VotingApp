# Generated by Django 3.2.9 on 2021-12-24 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='images')),
                ('Q_Body', models.TextField()),
                ('Option_1', models.CharField(max_length=110)),
                ('Option_2', models.CharField(max_length=110)),
                ('Option_3', models.CharField(blank=True, max_length=110)),
                ('Option_4', models.CharField(blank=True, max_length=110)),
                ('Option_1_count', models.IntegerField(default=0)),
                ('Option_2_count', models.IntegerField(default=0)),
                ('Option_3_count', models.IntegerField(default=0)),
                ('Option_4_count', models.IntegerField(default=0)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Voter_Phone_Number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('Voter_Fullname', models.CharField(blank=True, max_length=50)),
                ('Voter_Choise', models.IntegerField(default=0)),
                ('Voter_Opinion', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
