##Task 0

## Описание
Пробные тесты для тестирования api reqres.in и кастомного микросервиса

## Технологический стек
- Python
- Pytest
- Allure
- Docker

## Предварительные требования
Для запуска автотестов необходимо установить:
- python==3.12.8
- Java 17 или 21
- Allure commandline -- https://www.npmjs.com/package/allure-commandline

## Установка и запуск на ОС MacOS
1. Склонируйте репозиторий:
```bash
git clone git@github.com:Rena-san/guru_task_0.git
```
2. Создайте виртуальное окружение:
```bash
python -m venv venv
```
3. Активируйте виртуальное окружение:
```bash
 . venv/bin/activate
```
4. Установите зависимости:
```bash
pip install -r requirements.txt
```

4.1 Заруск БД (Docker должен быть запущен)
```bash
docker compose up -d
```

5. Запуск автотестов

   5.1. Запустить микросервис:
   ```bash
   uvicorn app.main:app --reload
   ```

   5.2. Запустить тесты :
   ```bash
   pytest 
   ```
   5.3. Просмотр allure отчета:
   ```bash
   allure serve
   ```
  


