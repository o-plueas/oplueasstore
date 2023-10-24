# Generated by Django 4.1.1 on 2023-10-13 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('zipcode', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paystack_ref', models.CharField(blank=True, max_length=15)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]