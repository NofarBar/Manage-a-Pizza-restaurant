FROM python:3.9 
ADD . /Pizzas
WORKDIR /Pizzas
ENTRYPOINT ["python", "pizzas.py"]