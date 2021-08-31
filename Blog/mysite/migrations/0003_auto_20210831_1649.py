# Generated by Django 3.2.6 on 2021-08-31 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20210831_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(default='blog name', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='subjects',
            field=models.ManyToManyField(blank=True, null=True, related_name='blogs', to='mysite.Subject'),
        ),
    ]
