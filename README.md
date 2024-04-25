# may_readyscript_test
Test task

## Запуск в докере: 

Собираем образ
` docker build --platform linux/amd64 -t may_readyscript_test . ` (для систем на ARM архитектуре)

` docker build -t may_readyscript_test . ` (для всех остальных систем) 

Запускаем контейнер
` docker run --privileged may_readyscript_test `

Внутри контейнера:

Запуск всех тестов в хедлесс режиме. Можно указать директорию, тогда пройдут все тесты в этой директории.

` python3 -m pytest tests/ui_tests `

Запуск конкретных тестов в хедлесс режиме 

`  python3 -m pytest -k {имя теста} `

Для локального запуска вне докера не в headless режиме есть ключ ` --disable-headless  `, 
пример команды - ` python3 -m pytest --disable-headless tests/ui_tests/login_tests/ `

