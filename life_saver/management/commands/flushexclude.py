from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Flush all data except the specified table(s)'

    def add_arguments(self, parser):
        parser.add_argument('--exclude', nargs='*', type=str, help='List of tables to exclude')

    def handle(self, *args, **options):
        excluded_tables = options['exclude'] or []
        excluded_tables = set(excluded_tables)

        with connection.cursor() as cursor:
            # Get the list of all tables in the database
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            all_tables = [row[0] for row in cursor.fetchall()]

            # Determine which tables to flush
            tables_to_flush = [table for table in all_tables if table not in excluded_tables]

            # Generate SQL to delete all records from tables
            for table in tables_to_flush:
                cursor.execute(f"DELETE FROM {table};")

        self.stdout.write(self.style.SUCCESS('Data flushed successfully.'))
