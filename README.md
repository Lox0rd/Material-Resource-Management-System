# Material Resource Management System

Веб-сервис для автоматического формирования ведомостей материалов, спецификаций и расчёта сметной стоимости на основе входного Excel-файла.

## 🚀 Функциональность

- Загрузка Excel-файла со схемой
- Парсинг и обработка данных
- Формирование ведомости материалов
- Расчёт стоимости по прайс-листу
- Экспорт отчётов в Excel

## 🛠 Технологии

- Python 3
- Flask
- pandas
- openpyxl

## 📂 Структура проекта
app.py              # Flask-приложение
services/           # Логика обработки данных
templates/          # HTML-шаблоны
static/             # CSS и изображения
uploads/            # Загруженные файлы
reports/            # Сформированные отчёты

## ▶ Запуск
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

После запуска открыть:
http://127.0.0.1:5000