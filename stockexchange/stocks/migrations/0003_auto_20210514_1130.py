# Generated by Django 3.1.3 on 2021-05-14 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_mutualfunds'),
    ]

    operations = [
        migrations.CreateModel(
            name='FixedDeposits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=7)),
                ('minAmount', models.IntegerField()),
                ('compounding', models.CharField(max_length=200)),
                ('preWithdrawal', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=2048)),
                ('crisilRating', models.CharField(max_length=200)),
                ('CEO', models.CharField(max_length=250)),
                ('headquaters', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='USStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('openPrice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('prevPrice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('volume', models.IntegerField()),
                ('avgVolume', models.IntegerField()),
                ('marketCap', models.IntegerField()),
                ('peRatio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('pbRatio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('roe', models.DecimalField(decimal_places=2, max_digits=7)),
                ('eps', models.DecimalField(decimal_places=2, max_digits=7)),
                ('dividendYield', models.DecimalField(decimal_places=2, max_digits=7)),
                ('enterpriseValue', models.DecimalField(decimal_places=2, max_digits=7)),
                ('bookValue', models.DecimalField(decimal_places=2, max_digits=7)),
                ('todayslow', models.DecimalField(decimal_places=2, max_digits=7)),
                ('todayshigh', models.DecimalField(decimal_places=2, max_digits=7)),
                ('about', models.CharField(max_length=2048)),
                ('organisation', models.CharField(max_length=250)),
                ('industry', models.CharField(max_length=250)),
                ('headquarters', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='stocks',
            name='NSE',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='stocks',
            name='about',
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.AddField(
            model_name='stocks',
            name='director',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='stocks',
            name='parentOrg',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]