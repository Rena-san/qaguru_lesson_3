## Lesson 4

docker build . -t qa_app

docker run -e DATABASE_ENGINE="postgresql+psycopg2://postgres:example@localhost:5432/postgres" --p 8002:80 qa_app

docker run -e DATABASE_ENGINE="postgresql+psycopg2://postgres:example@host.docker.internal:5432/postgres" --p 8002:80 qa_app

docker compose up

docker compose --build (пересобирает образ)

## Описание

Пробные тесты для тестирования api reqres.in и кастомного микросервиса

## Технологический стек

- Python
- Pytest
- Allure
- Poetry
- Docker

## Предварительные требования

Для запуска автотестов необходимо установить:

- python==3.12.8
- Java 17 или 21
- Allure commandline -- https://www.npmjs.com/package/allure-commandline

## Установка и запуск на ОС MacOS

1. Склонируйте репозиторий:

```bash
git https://github.com/Rena-san/qaguru_lesson_3.git
git checkout lesson_4
```

2. Cоздание виртуального окружения и установка зависимостей через pip:

   2.1 Выполните последовательно команды:

```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

3. Создание виртуального окружения и установка зависимостей через poetry

   3.1 Выполните последовательно команды:


```bash
poetry config virtualenvs.in-project true
poetry self add poetry-plugin-shell
poetry install
poetry shell
```

4. Запустите БД (Docker должен быть уже запущен на компьютере)

```bash
docker compose up -d
```

5. Запустите микросервис:

   ```bash
   uvicorn app.main:app --reload
   ```
6. Запуск автотестов если зависимости установлены через pip

   ```bash
   pytest 
   ```
6.1 Запуск автотестов если зависимости установлены через poetry

 ```bash
   poetry run pytest
   ```
7. Просмотр allure отчета:

   ```bash
   allure serve
   ```
   