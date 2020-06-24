from django.core.management.base import BaseCommand
from rooms.models import Factility


class Command(BaseCommand):

    help = "This command created facilities"

    """      def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        ) 
    """

    def handle(self, *args, **options):
        facilities = [
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Pool",
        ]
        for f in facilities:
            Factility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("건물유형 생성!"))
