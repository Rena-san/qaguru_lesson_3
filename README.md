##Task 0

## Описание
Пробные тесты для тестирования api reqres.in и кастомного микросервиса

## Технологический стек
- Python
- Pytest
- Allure

## Предварительные требования
Для запуска автотестов необходимо установить:
- python==3.12.8
- Java 17 или 21
- Allure commandline -- https://www.npmjs.com/package/allure-commandline
- Poetry

## Установка и запуск на ОС MacOS
1. Склонируйте репозиторий:
```bash
git clone git@github.com:Rena-san/guru_task_0.git
```
2. Создайте виртуальное окружение в директории проекта:
```bash
poetry config virtualenvs.in-project true
poetry self add poetry-plugin-shell
```
3. Установите зависимости:
```bash
poetry install
```
4. Активируйте виртуальное окружение:
```bash
poetry shell
```
5. Запуск автотестов

   5.1. Запустить микросервис:
   ```bash
   uvicorn custom_api.main:app --reload
   ```

   5.2. Запустить тесты :
   ```bash
   poetry run pytest 
   ```
   5.3. Просмотр allure отчета:
   ```bash
   allure serve
   ```
  
Установка зависимостей через pip

2.Создайте виртуальное окружение в директории проекта:
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

## Документация 
- https://reqres.in/api-docs/
