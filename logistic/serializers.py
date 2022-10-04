from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description"]


class ProductPositionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = StockProduct
        fields = ["id", "product", "quantity", "price"]


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ["id", "address", "positions"]

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop("positions")
        print(positions)
        # создаем склад по его параметрам
        stock = super().create(validated_data)
        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for el in positions:
            StockProduct.objects.create(
                stock=stock,
                product=el["product"],
                quantity=el["quantity"],
                price=el["price"],
            )
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop("positions")
        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for el in positions:
            obj, created = StockProduct.objects.update_or_create(
                stock=stock,
                product=el["product"],
                defaults={
                    "quantity": el["quantity"],
                    "price": el["price"]
                }
            )
        return stock
