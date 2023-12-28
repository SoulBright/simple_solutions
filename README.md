# simple_solutions
simple_solutions test task

https://hub.docker.com/repository/docker/soulbright/simple_solutions/general - ссылка на Docker контейнер

API Test Endpoints :
'admin' - доступ к админ панели (log: admin pass: admin
'api/item/<int:id>' - простейшая страница с товаром.
'api/order/<int:id>/' - простейшая страница со списком товаров.
'api/buy/<int:id>/' - позволяет получить Stripe Session Id для оплаты выбранного товара.
'api/buy_order/<int:id>/' - позволяет получить Stripe Session Id для оплаты выбранного списка товаров с учётом скидок и налогов.
'api/item_payment_intent/<int:id>/' - позволяет получить client_secret для оплаты выбранного товара.
'api/order_payment_intent/<int:id>/' - позволяет получить client_secret для оплаты выбранного списка товаров с учётом скидок и налогов.
