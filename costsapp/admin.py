from django.contrib import admin
from .models import BoycostsModel, GirlscostsModel, ShoppingcostsModel, ProfitModel

admin.site.register(BoycostsModel)

admin.site.register(GirlscostsModel)

admin.site.register(ShoppingcostsModel)

admin.site.register(ProfitModel)
