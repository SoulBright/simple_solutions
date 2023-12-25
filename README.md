# simple_solutions
simple_solutions test task

API Test Endpoints :
'api/item/<int:id>' - простейшая страница с товаром.
'api/order/<int:id>/' - простейшая страница со списком товаров.
'api/buy/<int:id>/' - позволяет получить Stripe Session Id для оплаты выбранного товара.
'api/buy_order/<int:id>/' - позволяет получить Stripe Session Id для оплаты выбранного списка товаров с учётом скидок и налогов.