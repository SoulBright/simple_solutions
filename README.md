# simple_solutions
simple_solutions test task

https://hub.docker.com/repository/docker/soulbright/simple_solutions/general - ссылка на Docker контейнер

API Test Endpoints :

'62.109.29.6:37342/admin' - доступ к админ панели (log: admin pass: admin)

'62.109.29.6:37342/api/item/<int:id>' - простейшая страница с товаром.

'62.109.29.6:37342/api/order/<int:id>/' - простейшая страница со списком товаров.

'62.109.29.6:37342/api/buy/<int:id>/' - позволяет получить Stripe Session Id для оплаты выбранного товара.

'62.109.29.6:37342/api/buy_order/<int:id>/' - позволяет получить Stripe Session Id для оплаты выбранного списка товаров с учётом скидок и налогов.

'62.109.29.6:37342/api/item_payment_intent/<int:id>/' - позволяет получить client_secret для оплаты выбранного товара.

'62.109.29.6:37342/api/order_payment_intent/<int:id>/' - позволяет получить client_secret для оплаты выбранного списка товаров с учётом скидок и налогов.
