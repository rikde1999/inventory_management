Inventory Management System

Models:
- Category
- Products


Database:
- Postgres


Functions: 
Task to create a basic Inventory Management System that supports CRUD
(Create, Read, Update, Delete) operations for managing Products and Categories.

Deployment via Docker: 
Build command : docker-compose -f docker-compose-local.yml up --build -d
Make migrations: docker exec -it container_name bash, python manage.py makemigrations, python manage.py migrate


Category APIS:

1. Category Creation API:
    curl --location 'http://127.0.0.1:9050/category/category_list' \
    --header 'Content-Type: application/json' \
    --data '{
        "name": "Laptops",
        "description": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English"
    }'

2. Category Get API:

    curl --location 'http://127.0.0.1:9050/category/category_list'


3. Category Update API:
    curl --location --request PUT 'http://127.0.0.1:9050/category/category_details/1' \
        --header 'Content-Type: application/json' \
        --data '{
            "name": "Mouse",
            "description": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English"
        }'

4. Category Delete API:
    curl --location --request DELETE 'http://127.0.0.1:8000/category/category_details/1'



----------------------------------------------------------------------------------------------------

Product APIs:

1. Product Creation API:
    curl --location 'http://127.0.0.1:9050/products/product_list' \
    --header 'Content-Type: application/json' \
    --data '{
        "name": "Asus",
        "category_id": "2",
        "price": 1000,
        "quantity": 2,
        "description": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English"
    }'

2. Product Get API:

    curl --location 'http://127.0.0.1:9050/products/product_list'


3. Product Update API:
    curl --location --request PUT 'http://127.0.0.1:8000/products/product_details/1' \
    --header 'Content-Type: application/json' \
    --data '{
        "name": "red gear",
        "category_id": 2,
        "price": 102,
        "quantity": 100,
        "description": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English"
        
    }'

4. Product Delete API:
    curl --location --request DELETE 'http://127.0.0.1:8000/products/product_details/1' \
    --data ''