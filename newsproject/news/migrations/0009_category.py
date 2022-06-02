# Generated by Django 4.0.4 on 2022-06-02 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_remove_author_email_remove_author_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
