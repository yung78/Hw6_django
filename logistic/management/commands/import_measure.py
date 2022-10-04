from django.core.management.base import BaseCommand
from measurement.models import Sensor, Measurement


#  Тест для записи бездаты)
class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        sensor = Sensor.objects.get(id=1)
        Measurement.objects.create(
            sensor=sensor,
            temperature=200.8,
        )

