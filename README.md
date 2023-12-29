# simple_solutions
simple_solutions test task

Задача
· 	Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
· 	Django Модель Item с полями (name, description, price)
· 	API с двумя методами:
· 	GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
· 	GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
· 	Запуск используя Docker
· 	Использование environment variables
· 	Просмотр Django Моделей в Django Admin панели
· 	Запуск приложения на удаленном сервере, доступном для тестирования
· 	Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
· 	Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
· 	Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
· 	Реализовать не Stripe Session, а Stripe Payment Intent.


https://hub.docker.com/repository/docker/soulbright/simple_solutions/general - ссылка на Docker контейнер

API Test Endpoints :

'62.109.29.6:37342/admin' - доступ к админ панели (log: admin pass: admin)

'62.109.29.6:37342/api/item/<int:id>' - простейшая страница с товаром.

'62.109.29.6:37342/api/order/<int:id>/' - простейшая страница со списком товаров.

'62.109.29.6:37342/api/buy/<int:id>/' - позволяет получить Stripe Session Id для оплаты выбранного товара.

'62.109.29.6:37342/api/buy_order/<int:id>/' - позволяет получить Stripe Session Id для оплаты выбранного списка товаров с учётом скидок и налогов.

'62.109.29.6:37342/api/item_payment_intent/<int:id>/' - позволяет получить client_secret для оплаты выбранного товара.

'62.109.29.6:37342/api/order_payment_intent/<int:id>/' - позволяет получить client_secret для оплаты выбранного списка товаров с учётом скидок и налогов.
