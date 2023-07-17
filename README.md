## Запуск
```
docker build -t test_task .
docker run --name test_task -p8000:8000 test_task
```

## Путь к Swagger-документации
`127.0.0.1:8000/docs`