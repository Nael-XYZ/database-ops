"""Database migration tool."""
import hashlib
from pathlib import Path

class Migrator:
    def __init__(self, db_url):
        self.db_url = db_url
        self.migrations_dir = Path("migrations")
        
    def create(self, name):
        version = len(list(self.migrations_dir.glob("*.sql"))) + 1
        path = self.migrations_dir / f"{version:04d}_{name}.sql"
        path.write_text(f"-- Migration: {name}\n-- Version: {version}\n\n")
        return path
        
    def upgrade(self):
        pass
        
    def rollback(self):
        pass
