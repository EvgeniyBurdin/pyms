# pyms

Сервис на python.

## База данных

Используется Postgres.

Для БД требуестя установить расширение для uuid, это можно сделать выполнив запрос к БД:

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

### Миграции

*Примечание:
`PYMS_SERVICE_DEV=1` в командах - загружает переменные среды (см. `settings.py`)*

Создать файл миграции

```bash
PYMS_SERVICE_DEV=1 alembic revision --autogenerate -m "Create pyms_people table"
```

Обновить БД до самой свежей версии (миграции)

```bash
PYMS_SERVICE_DEV=1 alembic upgrade head
```

Текущий статус

```bash
 PYMS_SERVICE_DEV=1 alembic current
```
