from django.core.management.base import BaseCommand
from logistic.models import Product, Stock, StockProduct
import random


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        products = {
            "Картофель": "новый урожай",
            "Огурцы": "тепличные",
            "Помидоры": "розовые",
            "Капуста": "белокачанная, новый урожай",
            "Перец": "красный, Турция"
        }
        stocks = [
            "Санкт-Петербург Южный склад",
            "Санкт-Петербург Северный склад",
            "Гатчина Центральный склад"
            ]

        for title, description in products.items():
            Product.objects.create(title=title, description=description)

        for stock in stocks:
            Stock.objects.create(address=stock)

        for stock in Stock.objects.all():
            for product in Product.objects.all():
                StockProduct.objects.create(
                    stock=stock,
                    product=product,
                    quantity=random.randint(10, 50),
                    price=round(random.uniform(9, 12), 2)
                )
