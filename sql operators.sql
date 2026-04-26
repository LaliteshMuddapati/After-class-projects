create table if not exists customers (customer_id text primary key, customer_name text not null, customer_city text, customer_grade int);

insert into customers (customer_id, customer_name, customer_city, customer_grade) values
('c1', 'jeff', 'new_york', 100),
('c2', 'jack', 'new_york', 120),
('c3', 'james', 'WDC', 98),
('c4', 'joe', 'tokyo', 49),
('c5', 'jim', 'new_york', 200),
('c6', 'jerry', 'WDC', 111),
('c7', 'jake', 'new_york', 72),
('c8', 'Joseph', 'London', 218),
('c9', 'jessy', 'berlin', 318),
('c10', 'jeremy', 'London', 85);

select * from customers WHERE
customer_city='new_york' or customer_grade>100;


select * from customers WHERE customer_city='new_york' and customer_grade>100;