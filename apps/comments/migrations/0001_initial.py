# Generated by Django 4.1 on 2022-09-01 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Commets', to='cards.card')),
            ],
        ),
    ]
