# Тестове завдання для DevIT group

Система управління інцидентами з REST API та підтримкою карт.

## Особливості

- CRUD операції для інцидентів
- PostgreSQL база даних
- GeoJSON формат для карт
- Swagger документація
- Docker контейнеризація

## Швидкий старт

### Використання Docker

1. Клонувати репозиторій:
```bash
git clone https://github.com/Kyivnik/testove_devit.git
cd incident-manager
```

2. Запустити проект:
```bash
docker-compose up --build
```

3. Виконати міграції:
```bash
docker-compose exec web python manage.py migrate
```

4. Створити суперюзера:
```bash
docker-compose exec web python manage.py createsuperuser
```

### Локальне встановлення

1. Встановити залежності:
```bash
pip install -r requirements.txt
```

2. Налаштувати PostgreSQL та змінити параметри в settings.py

3. Виконати міграції:
```bash
python manage.py migrate
```

4. Запуск сервера:
```bash
python manage.py runserver
```

## API Endpoints

### Інциденти
- `GET /api/incidents/` - список всіх інцидентів
- `POST /api/incidents/` - створити інцидент
- `GET /api/incidents/{id}/` - отримати інцидент
- `PUT /api/incidents/{id}/` - оновити інцидент
- `DELETE /api/incidents/{id}/` - видалити інцидент

### Карти
- `GET /api/incidents/active_geojson/` - активні інциденти в GeoJSON форматі

## Документація API

- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## Структура проекту

```
incident-manager/
├── incident_manager/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── incidents/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── admin.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Формат даних інциденту

```json
{
  "id": 1,
  "title": "Пограбування",
  "latitude": 50.4501,
  "longitude": 30.5234,
  "created_at": "2025-05-22T18:30:00Z",
  "status": "active"
}
```

## GeoJSON формат

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [30.5234, 50.4501]
      },
      "properties": {
        "id": 1,
        "title": "Пограбування",
        "status": "active",
        "created_at": "2025-05-22T18:30:00Z"
      }
    }
  ]
}
```

## Тестування

Можна використати curl для тестування API:

```bash
# Створити інцидент
curl -X POST http://localhost:8000/api/incidents/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Тестовий інцидент", "latitude": 50.4501, "longitude": 30.5234, "status": "active"}'

# Отримати всі інциденти
curl http://localhost:8000/api/incidents/

# Отримати GeoJSON
curl http://localhost:8000/api/incidents/active_geojson/
```

## Використані технології

- Django 4.2
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- drf-yasg (Swagger)
