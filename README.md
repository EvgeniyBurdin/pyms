# pyms

Сервис на python.

## Запуск сервиса

```bash
PYMS_SERVICE_DEV=1 python run_service.py
```

*Примечание:
`PYMS_SERVICE_DEV=1` в этой и других командах - загружает переменные среды (см. `settings.py`)*

## Переменные среды

Пример файла:

```bash
PYMS_ENV_VARS_PREFIX=PYMS_DEV_

PYMS_DEV_SERVICE_NAME=simple_pyms
PYMS_DEV_SERVICE_HOST=0.0.0.0
PYMS_DEV_SERVICE_PORT=5000

PYMS_DEV_POSTGRES_DB=pyms
PYMS_DEV_POSTGRES_HOST=localhost
PYMS_DEV_POSTGRES_PORT=5432
PYMS_DEV_POSTGRES_USER=postgres
PYMS_DEV_POSTGRES_PASSWORD=0
```

## База данных

Используется Postgres.

Для БД требуется установить расширение для полей `uuid`, это можно сделать выполнив запрос:

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
```

## Миграции

Команды для работы с миграциями:

- Создать файл миграции

```bash
PYMS_SERVICE_DEV=1 alembic revision --autogenerate -m "Create people table"
```

- Обновить БД до самой свежей версии (миграции)

```bash
PYMS_SERVICE_DEV=1 alembic upgrade head
```

- Текущий статус

```bash
PYMS_SERVICE_DEV=1 alembic current
```
