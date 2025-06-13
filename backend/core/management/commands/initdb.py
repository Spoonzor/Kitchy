# core/management/commands/initdb.py
from django.core.management.base import BaseCommand
from django.db import connections
from django.core.management import call_command

class Command(BaseCommand):
    help = "Initialise la base de données si les tables n'existent pas (exécute 'migrate')."

    def handle(self, *args, **options):
        connection = connections['default']
        try:
            with connection.cursor() as cursor:
                # Teste l'existence de la table django_migrations
                cursor.execute("SELECT 1 FROM django_migrations LIMIT 1;")
            self.stdout.write(self.style.SUCCESS("Les tables existent déjà."))
        except Exception as e:
            self.stdout.write("Aucune table trouvée ou erreur, initialisation de la base...")
            call_command('migrate')
            self.stdout.write(self.style.SUCCESS("La base de données a été initialisée."))
