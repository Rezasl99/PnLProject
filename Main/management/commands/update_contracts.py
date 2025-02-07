from django.core.management.base import BaseCommand
from Main.task import update_prices_for_active_contracts

class Command(BaseCommand):
    def handle(self, *args, **options):
        update_prices_for_active_contracts()
        self.stdout.write(self.style.SUCCESS("updated contract prices"))
