# Generated by Django 4.1 on 2023-09-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("practest", "0002_remove_person_hobbies_delete_hobby_person_hobbies"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
