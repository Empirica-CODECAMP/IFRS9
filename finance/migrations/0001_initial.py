# Generated by Django 3.2.5 on 2025-02-04 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialInstrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('classification', models.CharField(choices=[('AC', 'Amortized Cost'), ('FVOCI', 'Fair Value OCI'), ('FVTPL', 'Fair Value P&L')], max_length=10)),
                ('credit_rating', models.CharField(max_length=10)),
                ('exposure', models.FloatField()),
                ('ecl_stage', models.IntegerField(choices=[(1, 'Stage 1'), (2, 'Stage 2'), (3, 'Stage 3')])),
                ('pd', models.FloatField()),
                ('lgd', models.FloatField()),
                ('ead', models.FloatField()),
            ],
        ),
    ]
