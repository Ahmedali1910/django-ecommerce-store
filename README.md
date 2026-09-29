# E-Commerce Website

## Short Project Description:

A simple E-Commerce website built with Django for managing products and categories. The website allows users to view products, view product details, filter products by category and price, and perform basic product management operations.

## Technologies Used

* Python
* Django
* HTML
* CSS
* SQLite
* Git & GitHub
* uv

## Installation Steps

1. Clone the repository.

2. Navigate to the project directory.

3. Install the project dependencies using uv:

```bash
uv sync
```

4. Apply the database migrations:

```bash
uv run python manage.py migrate
```

## How to Run the Development Server

Run the Django development server using:

```bash
uv run python manage.py runserver
```

Then open the development server in your browser.

## Main Features

* View all products.
* View details of a specific product.
* Create a new product.
* Edit an existing product.
* Delete a product.
* View products by category.
* Search/filter products by price.
* Manage product information using Django Forms.
* Responsive and styled user interface.
