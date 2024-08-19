# Generated by Django 5.1 on 2024-08-17 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expensetracker', '0003_remove_expense_transaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='income',
            options={'verbose_name_plural': 'income'},
        ),
        migrations.AddField(
            model_name='income',
            name='typeMonthYear',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='expensetracker.sheet'),
        ),
    ]
