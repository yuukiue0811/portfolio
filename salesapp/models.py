from django.db import models
from django.utils import timezone

CHOICES = (('yes', 'ドリンク別'), ('no', 'ドリンク込み'))
CHOICES2 = (('yes', ' TAXあり'), ('no', 'TAXなし'))

class SalesModel(models.Model):
    tablenumber = models.CharField('テーブル番号', max_length=100)
    girlsdrink_confirmation = models.CharField('ドリンク別か込みか', max_length=50, choices=CHOICES)
    tax_confirmation = models.CharField('TAXありかなしか', max_length=50, choices=CHOICES2)
    tablecharge = models.IntegerField('セット料金')
    custermer = models.IntegerField('お客さんの人数')
    girlsdrink_count = models.IntegerField('ドリンクの杯数')
    staff_reservation_fee = models.IntegerField('指名料', null=True, blank=True)
    champagne_fee = models.IntegerField('シャンパン料金', null=True, blank=True)
    tax_total = models.IntegerField(null=True, blank=True, default=0)
    bill = models.IntegerField('お会計', null=True, blank=True, default=0)
    sales = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    singlecharge = models.IntegerField('シングルチャージ', null=True, blank=True)
    sales_total = models.IntegerField('売上', null=True, blank=True, default=0)
    
