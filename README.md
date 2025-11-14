# Описание
Бот в MAX, содержащий информацию для абитуриентов, поступающих в МГЛУ

# Запуск бота
## Запуск бота с помощью предоставленного Docker образа
```bash
docker pull ghcr.io/digital-crusader/maxbot387:latest
docker run -d -e BOT_TOKEN=токен_бота --name max-bot-387-container ghcr.io/digital-crusader/maxbot387:latest
```
"токен_бота" заменить на ваш токен бота (без кавычек)

## Запуск бота из из скопированной репозитори
1) Скоприровать репозиторию
```bash
git clone https://github.com/digital-crusader/MaxBot387 && cd MaxBot387
```
2) Добавить токен бота в файл с именем .env в корневую директорию проекта   
```.env
BOT_TOKEN=токен_бота
```
"токен_бота" заменить на ваш токен бота (без кавычек)

### Запуск бота напрямую
В корневой директории проекта:
```bash
python main.py
```

### Запуск бота с Docker
В корневой директории проекта:
```bash
docker build -t max-bot-387 .
docker run -d --name max-bot-387-container max-bot-387
```