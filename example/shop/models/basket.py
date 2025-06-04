# models.py
from uuid import uuid4

from django.db import models

from salesman.basket.models import BaseBasket, BaseBasketItem


class Basket(BaseBasket):
    ref = models.CharField(max_length=128, unique=True, default=uuid4)


class BasketItem(BaseBasketItem):
    pass
