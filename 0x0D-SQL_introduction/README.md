# Database Concepts and MySQL Usage Guide

## What is a Database?

A **database** is a structured collection of data that is organized in a way that makes it easy to manage, access, and update. It serves as a central repository for storing and managing information.

## What is a Relational Database?

A **relational database** is a type of database that uses a structure called tables to organize and store data. Tables are related to each other based on common fields, enabling efficient data retrieval and management.

## What does SQL Stand For?

**SQL** stands for Structured Query Language. It is a domain-specific language used for managing and manipulating relational databases. SQL allows users to interact with databases by defining and executing queries.

## What's MySQL?

**MySQL** is a popular open-source relational database management system (RDBMS) that uses SQL. It is widely used for web development and is known for its speed, reliability, and ease of use.

## How to Create a Database in MySQL

To create a database in MySQL, you can use the following SQL command:

```sql
CREATE DATABASE your_database_name;
```

Replace `your_database_name` with the desired name for your database.

## DDL and DML

- **DDL (Data Definition Language):** DDL deals with the structure of the database, defining and modifying schema objects such as tables and indexes.

  Example:

  ```sql
  CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE
  );
  ```

- **DML (Data Manipulation Language):** DML deals with the manipulation of data stored in the database, including operations such as inserting, updating, and deleting data.

  Example:

  ```sql
  INSERT INTO users (id, username, email) VALUES (1, 'john_doe', 'john@example.com');
  ```

## CREATE or ALTER a Table

To create a table in MySQL, use the `CREATE TABLE` statement. To alter a table, use the `ALTER TABLE` statement.

Example:

```sql
-- Create a table
CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(255),
  price DECIMAL(10,2)
);

-- Alter table, add a new column
ALTER TABLE products
ADD COLUMN quantity INT;
```

## SELECT Data from a Table

To retrieve data from a table, use the `SELECT` statement.

Example:

```sql
SELECT * FROM products WHERE price > 50;
```

## INSERT, UPDATE, or DELETE Data

- **INSERT:**

  ```sql
  INSERT INTO products (product_id, product_name, price, quantity)
  VALUES (1, 'Laptop', 999.99, 10);
  ```

- **UPDATE:**

  ```sql
  UPDATE products
  SET price = 1099.99
  WHERE product_id = 1;
  ```

- **DELETE:**

  ```sql
  DELETE FROM products WHERE quantity < 5;
  ```

## Subqueries

**Subqueries** are queries embedded within other queries. They can be used in SELECT, FROM, WHERE, and other clauses.

Example:

```sql
SELECT product_name
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

## MySQL Functions

MySQL provides various built-in functions for data manipulation and analysis. Example using `COUNT`:

```sql
SELECT COUNT(*) FROM products;
```

For a comprehensive list of functions, refer to the [MySQL documentation](https://dev.mysql.com/doc/).

Feel free to explore and experiment with these SQL concepts using MySQL. This guide provides a foundation for understanding and using databases effectively.