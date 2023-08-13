# Generated by Django 4.2.4 on 2023-08-13 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketsystem.user'),
        ),
        migrations.CreateModel(
            name='AssignedTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketsystem.ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketsystem.user')),
            ],
        ),
    ]
