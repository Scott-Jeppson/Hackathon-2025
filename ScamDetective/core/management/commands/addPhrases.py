from django.core.management.base import BaseCommand
from core.models import Phrase

class Command(BaseCommand):
    help = 'Adds phrases to the database'

    def add_arguments(self, parser):
        # Add a positional argument for the file path
        parser.add_argument('file_path', type=str, help='The path to the text file containing phrases')

    def handle(self, *args, **kwargs):
        # Retrieve the file path from the arguments
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if not line.strip():
                        continue
                    try:
                        phrase, score = line.strip().rsplit(' ', 1)
                        phrase = phrase.strip('"')
                        score = int(score)
                        Phrase.objects.create(body=phrase, score=score)
                        self.stdout.write(f"Added phrase: {phrase} with score: {score}")
                    except ValueError:
                        self.stderr.write(f"Invalid line format: {line.strip()}")
        except FileNotFoundError:
            self.stderr.write(f"File not found: {file_path}")