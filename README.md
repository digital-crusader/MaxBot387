# Описание
Бот в MAX, содержащий информацию для абитуриентов, поступающих в МГЛУ

# Запуск бота
Скоприровать репозиторию
```bash
git clone https://github.com/digital-crusader/MaxBot387 && cd MaxBot387
```

## Запуск бота напрямую
В корневой директории проекта:
```bash
python main.py
```

## Запуск бота с Docker
В корневой директории проекта:
```bash
docker build -t max-bot-387 .
docker run -d --name max-bot-387-container max-bot-387
```