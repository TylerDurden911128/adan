# adan
We create the cars table and insert several rows to it. The execute() executes a database operation (query or command).

you should have installed, docker, docker-compose and psycopg2

0.- in your project directory

1.- run command: docker-compose up

2.- open new terminal and run commad: python create_table.py

3.- write one by one the next lines:
    
    Audi 52642
    
    Mercedes 57127
    
    Skoda 9000
    
    Volvo 29000
    
    Bentley 350000
    
    Citroen 21000
    
    Hummer 41400
    
    Volkswagen 21600
    
4.- open new terminal and run: psql -h :: -p 8001 -U postgres -d todos

5.- run command: SELECT * FROM cars;
    you'll see the next output:
    
        id |    name    | price
    ----+------------+--------
	 1 | Audi       |  52642
         2 | Mercedes   |  57127
         3 | Skoda      |   9000
         4 | Volvo      |  29000
         5 | Bentley    | 350000
         6 | Citroen    |  21000
         7 | Hummer     |  41400
         8 | Volkswagen |  21600
    (8 rows)
