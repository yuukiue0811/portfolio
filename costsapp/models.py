from django.db import models
from django.utils import timezone
CHOICES = (('yes', 'はい'), ('no', 'いいえ'))


class BoycostsModel(models.Model):
    name = models.CharField('スタッフ名', max_length=100)
    hour = models.IntegerField('勤務時間')
    wage = models.IntegerField('時給')
    fixedsalary = models.IntegerField('固定給')
    allowance = models.IntegerField('手当', null=True, blank=True)
    mounth_allowance = models.IntegerField('月末手当', null=True, blank=True)
    salary = models.IntegerField('給料', null=True, blank=True, default=0)
    salary_total = models.IntegerField('給料トータル', null=True, blank=True, default=0)
    date = models.DateTimeField(default=timezone.now)

class GirlscostsModel(models.Model):
    name = models.CharField('スタッフ名', max_length=100)
    hour = models.IntegerField('勤務時間')
    wage = models.IntegerField('時給')
    drinkbag = models.IntegerField('ドリンクバック(別)', null=True, blank=True)
    drinkbag_count = models.IntegerField('ドリンクバックの杯数(別)', null=True, blank=True)
    drinkbag_in = models.IntegerField('ドリンクバック(込み)', null=True, blank=True)
    drinkbagin_count = models.IntegerField('ドリンクバックの杯数(込み)', null=True, blank=True)
    bag = models.IntegerField('指名料のバック', null=True, blank=True)
    champagne_bag = models.IntegerField('シャンパンバック', null=True, blank=True)
    salary = models.IntegerField('給料', null=True, blank=True, default=0)
    salary_total = models.IntegerField('給料トータル', null=True, blank=True, default=0)
    date = models.DateTimeField(default=timezone.now)


class ShoppingcostsModel(models.Model):
    shopping_costs = models.IntegerField('買い物代')
    others = models.IntegerField('他にかかった費用', null=True, blank=True)
    profit = models.IntegerField('臨時収入', null=True, blank=True)
    shopping_total = models.IntegerField('出費総額', null=True, blank=True, default=0)
    date = models.DateTimeField(default=timezone.now)
    
class ProfitModel(models.Model):
    salestotal = models.IntegerField('今日の売上', null=True, blank=True)
    boyscosts = models.IntegerField('ボーイの給料合計', null=True, blank=True)
    girlscosts = models.IntegerField('キャストの給料合計', null=True, blank=True)
    costs = models.IntegerField('買い物代などの他費用', null=True, blank=True)
    profit = models.IntegerField('今日の利益',null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    people = models.IntegerField(null=True, blank=True)
