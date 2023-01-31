# Manage a pizza restaurant
## project_description
This project manage a restaurant that receives array of orders, while each order is for one Pizza that contains an array of
toppings.
The pizza passes through several stations before it is served to the customer - Dough chef -> Topping chef -> Oven -> Serving
At the end the program print a report, The report contains:
*  The preparation time from start to end.
*  The preparation time for each order.

## Execution instructions python
* Install Python
* Clone this repo
* From the  directory you clone this project run:
`python pizzas.py "topping1, topping2" "topping1, topping2, topping3, topping4"`
For the input each "topping1, topping2" represents a single order with the toppings.

## Execution instructions docker
* Clone this repo
* cd Pizzas
* Run - `docker build ./ -t pizzas`
* Run - `docker run pizzas "topping1, topping2" "topping1, topping2, topping3, topping4"`
