# Generated by Django 3.2.3 on 2021-05-15 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RiskField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128)),
                ('type', models.CharField(max_length=20)),
                ('required', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.risk')),
            ],
        ),
        migrations.CreateModel(
            name='FieldOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.riskfield')),
            ],
        ),
    ]