# Generated by Django 5.0.1 on 2024-01-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
    ]
