# Используем официальный Python-образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app


# Копируем код и зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY . .

# Открываем порт (по желанию)
EXPOSE 8080

# Команда запуска
CMD ["python", "app.py"]