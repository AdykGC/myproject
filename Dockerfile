# Используем официальный Python-образ
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только нужные файлы
COPY backend /app/backend

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r backend/requirements.txt

# Устанавливаем рабочую директорию на папку backend, где manage.py
WORKDIR /app/backend

# Открываем порт
EXPOSE 8000

# Команда для запуска сервера
CMD ["gunicorn", "backend.backend.wsgi:application", "--bind", "0.0.0.0:8000"]
