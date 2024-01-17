# MySQL Learning Guide on Linux

## Table of Contents
1. [Introduction](#introduction)
2. [Creating a New MySQL User](#creating-a-new-mysql-user)
3. [Managing Privileges](#managing-privileges)
4. [PRIMARY KEY](#primary-key)
5. [FOREIGN KEY](#foreign-key)
6. [NOT NULL and UNIQUE Constraints](#not-null-and-unique-constraints)
7. [Retrieving Data from Multiple Tables](#retrieving-data-from-multiple-tables)
8. [Subqueries](#subqueries)
9. [JOIN and UNION](#join-and-union)

## Introduction
This guide is designed to help students learn MySQL on Linux by providing detailed explanations and examples for key concepts and tasks. MySQL is a popular open-source relational database management system widely used for web development.

### Prerequisites
Before you begin, ensure that you have MySQL installed on your Linux system. You can install it using the package manager specific to your distribution (e.g., `apt`, `yum`, `zypper, etc.).

```bash
# For Ubuntu/Debian
sudo apt-get update
sudo apt-get install mysql-server

# For CentOS
sudo yum install mysql-server

# For openSUSE
sudo zypper install mysql-server
```

## Creating a New MySQL User
To create a new MySQL user, you can use the `CREATE USER` statement. Here's an example:

```sql
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password';
```

Replace 'new_user' with the desired username and 'password' with the password for the new user.

## Managing Privileges
MySQL provides the `GRANT` statement to manage privileges for a user. To grant all privileges on a specific database:

```sql
GRANT ALL PRIVILEGES ON your_database.* TO 'your_user'@'localhost';
FLUSH PRIVILEGES;
```

Replace 'your_database' with the target database and 'your_user' with the username.

## PRIMARY KEY
A `PRIMARY KEY` is a unique identifier for a record in a table. It must contain unique values and cannot have NULL values.

Example:

```sql
CREATE TABLE students (
  student_id INT PRIMARY KEY,
  student_name VARCHAR(50) NOT NULL
);
```

## FOREIGN KEY
A `FOREIGN KEY` is a field in one table that refers to the `PRIMARY KEY` in another table. It establishes a link between the two tables.

Example:

```sql
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  product_id INT,
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

## NOT NULL and UNIQUE Constraints
- `NOT NULL` ensures that a column cannot contain NULL values.
- `UNIQUE` ensures that all values in a column are distinct.

Example:

```sql
CREATE TABLE employees (
  employee_id INT PRIMARY KEY,
  employee_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE
);
```

## Retrieving Data from Multiple Tables
To retrieve data from multiple tables in one request, you can use the `JOIN` statement. For example, to get a list of students and their enrolled courses:

```sql
SELECT students.student_id, students.student_name, courses.course_name
FROM students
JOIN enrollments ON students.student_id = enrollments.student_id
JOIN courses ON enrollments.course_id = courses.course_id;
```

## Subqueries
A subquery is a query nested inside another query. It can be used in various clauses, such as SELECT, FROM, WHERE, etc.

Example:

```sql
SELECT product_name
FROM products
WHERE price > (SELECT AVG(price) FROM products);
```

## JOIN and UNION
- `JOIN` combines rows from two or more tables based on a related column.
- `UNION` combines the result sets of two or more SELECT statements into a single result set.

Example:

```sql
-- JOIN
SELECT customers.customer_id, orders.order_id
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id;

-- UNION
SELECT product_id, product_name FROM electronics
UNION
SELECT product_id, product_name FROM appliances;
```

![image](https://github.com/LWSSIM/alx-higher_level_programming/assets/127129101/74e86347-8742-486a-a551-d01fc1e4498c)

## PS;
### How to import a SQL dump
```shell
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

This guide provides a foundation for understanding key MySQL concepts and performing common tasks. Experiment with these examples to reinforce your understanding of MySQL on Linux.
