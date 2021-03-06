# Generated by Django 3.1.4 on 2020-12-12 22:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tablenumber', models.CharField(max_length=100, verbose_name='テーブル番号')),
                ('girlsdrink_confirmation', models.CharField(choices=[('yes', 'ドリンク別'), ('no', 'ドリンク込み')], max_length=50, verbose_name='ドリンク別か込みか')),
                ('tax_confirmation', models.CharField(choices=[('yes', ' TAXあり'), ('no', 'TAXなし')], max_length=50, verbose_name='TAXありかなしか')),
                ('tablecharge', models.IntegerField(verbose_name='セット料金')),
                ('custermer', models.IntegerField(verbose_name='お客さんの人数')),
                ('girlsdrink_count', models.IntegerField(verbose_name='ドリンクの杯数')),
                ('staff_reservation_fee', models.IntegerField(blank=True, null=True, verbose_name='指名料')),
                ('champagne_fee', models.IntegerField(blank=True, null=True, verbose_name='シャンパン料金')),
                ('tax_total', models.IntegerField(blank=True, default=0, null=True)),
                ('bill', models.IntegerField(blank=True, default=0, null=True, verbose_name='お会計')),
                ('sales', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('singlecharge', models.IntegerField(blank=True, null=True, verbose_name='シングルチャージ')),
                ('sales_total', models.IntegerField(blank=True, default=0, null=True, verbose_name='売上')),
            ],
        ),
    ]
