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


 ## Небольшие пояснения: 

1. Конечно на реальном многоязычном проекте я бы не использовал локаторы вида //button[text()='Принять'], 
но как мы знаем тестирование зависит от контекста и конкретно на этом ресурсе, где только один язык, я счел это уместным
2. К сожалению нет возможности уделить заданию больше времени, а затягивать не хочется, поэтому все что касается 
скриншотов сделано весьма поверхносто, это некое очень-очень раннее дэмо без отчетов и логирования
3. Конечно скриншотные проверки можно было легко сделать и в TestLogin, но я не счел нужным - области проверки там 
весьма небольшие и их достаточно надежно проверяем "по старинке"
4. Хотел успеть прикрутить хорошие отчеты и логирование и запуск в облаке, ибо есть богатый опыт, но опять-таки, 
мало времени и не хотелось затягивать. 
