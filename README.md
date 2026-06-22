# Database Ops 🗄️

Database operations toolkit for PostgreSQL and MySQL.

## Features

- **Migrations**: Schema versioning with rollback
- **Backups**: Automated with encryption
- **Replication**: Lag monitoring + failover
- **Performance**: Query analysis + index suggestions

## Quick Start

```python
from db_ops import Migrator

migrator = Migrator(db_url="postgresql://localhost/mydb")
migrator.create("add_users_table")
migrator.upgrade()
```

## License

MIT