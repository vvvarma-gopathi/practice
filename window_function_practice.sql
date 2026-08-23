---creating a table called employee_sales to perform window functions
CREATE TABLE employee_sales (
    sale_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(50),
    department VARCHAR(30),
    city VARCHAR(30),
    sale_date DATE,
    sales_amount NUMERIC(10,2),
    target_amount NUMERIC(10,2)
);

----inserting 50 records to table employee_sales

INSERT INTO employee_sales
(employee_name, department, city, sale_date, sales_amount, target_amount)
VALUES
('Arjun', 'Sales', 'Hyderabad', '2026-01-05', 45000, 50000),
('Priya', 'Sales', 'Hyderabad', '2026-01-10', 62000, 55000),
('Rahul', 'Sales', 'Bangalore', '2026-01-15', 58000, 60000),
('Sneha', 'Sales', 'Chennai', '2026-01-20', 71000, 65000),
('Kiran', 'Sales', 'Hyderabad', '2026-01-25', 49000, 50000),
('Arjun', 'Sales', 'Hyderabad', '2026-02-05', 67000, 60000),
('Priya', 'Sales', 'Hyderabad', '2026-02-10', 72000, 65000),
('Rahul', 'Sales', 'Bangalore', '2026-02-15', 55000, 60000),
('Sneha', 'Sales', 'Chennai', '2026-02-20', 78000, 70000),
('Kiran', 'Sales', 'Hyderabad', '2026-02-25', 61000, 55000),
('Arjun', 'Sales', 'Hyderabad', '2026-03-05', 73000, 65000),
('Priya', 'Sales', 'Hyderabad', '2026-03-10', 68000, 65000),
('Rahul', 'Sales', 'Bangalore', '2026-03-15', 64000, 60000),
('Sneha', 'Sales', 'Chennai', '2026-03-20', 82000, 75000),
('Kiran', 'Sales', 'Hyderabad', '2026-03-25', 59000, 60000),
('Arjun', 'Sales', 'Hyderabad', '2026-04-05', 76000, 70000),
('Priya', 'Sales', 'Hyderabad', '2026-04-10', 81000, 70000),
('Rahul', 'Sales', 'Bangalore', '2026-04-15', 70000, 65000),
('Sneha', 'Sales', 'Chennai', '2026-04-20', 88000, 80000),
('Kiran', 'Sales', 'Hyderabad', '2026-04-25', 63000, 60000),
('Arjun', 'Sales', 'Hyderabad', '2026-05-05', 80000, 75000),
('Priya', 'Sales', 'Hyderabad', '2026-05-10', 85000, 75000),
('Rahul', 'Sales', 'Bangalore', '2026-05-15', 76000, 70000),
('Sneha', 'Sales', 'Chennai', '2026-05-20', 91000, 85000),
('Kiran', 'Sales', 'Hyderabad', '2026-05-25', 68000, 65000),
('Vikram', 'IT', 'Hyderabad', '2026-01-07', 90000, 85000),
('Meena', 'IT', 'Bangalore', '2026-01-12', 85000, 80000),
('Suresh', 'IT', 'Chennai', '2026-01-17', 78000, 75000),
('Anjali', 'IT', 'Hyderabad', '2026-01-22', 95000, 90000),
('Ravi', 'IT', 'Bangalore', '2026-01-27', 82000, 85000),
('Vikram', 'IT', 'Hyderabad', '2026-02-07', 92000, 90000),
('Meena', 'IT', 'Bangalore', '2026-02-12', 88000, 85000),
('Suresh', 'IT', 'Chennai', '2026-02-17', 81000, 80000),
('Anjali', 'IT', 'Hyderabad', '2026-02-22', 98000, 95000),
('Ravi', 'IT', 'Bangalore', '2026-02-27', 86000, 85000),
('Vikram', 'IT', 'Hyderabad', '2026-03-07', 97000, 95000),
('Meena', 'IT', 'Bangalore', '2026-03-12', 91000, 90000),
('Suresh', 'IT', 'Chennai', '2026-03-17', 85000, 85000),
('Anjali', 'IT', 'Hyderabad', '2026-03-22', 102000, 100000),
('Ravi', 'IT', 'Bangalore', '2026-03-27', 89000, 90000),
('Vikram', 'IT', 'Hyderabad', '2026-04-07', 99000, 95000),
('Meena', 'IT', 'Bangalore', '2026-04-12', 94000, 90000),
('Suresh', 'IT', 'Chennai', '2026-04-17', 88000, 85000),
('Anjali', 'IT', 'Hyderabad', '2026-04-22', 105000, 100000),
('Ravi', 'IT', 'Bangalore', '2026-04-27', 93000, 90000),
('Vikram', 'IT', 'Hyderabad', '2026-05-07', 103000, 100000),
('Meena', 'IT', 'Bangalore', '2026-05-12', 97000, 95000),
('Suresh', 'IT', 'Chennai', '2026-05-17', 90000, 90000),
('Anjali', 'IT', 'Hyderabad', '2026-05-22', 110000, 105000),
('Ravi', 'IT', 'Bangalore', '2026-05-27', 96000, 95000);

--1.Display every employee's sales along with a unique row number ordered by sales_amount 
--from highest to lowest.

select e.*,row_number() over(order by sales_amount desc) as row_num from employee_sales e;

--2.Assign a row number to each employee's sales record based on sale_date.

select employee_name,department,sale_date,sales_amount,row_number() 
over(partition by sale_date order by sales_amount desc) as row_num from employee_sales;

--3.Assign a separate row number to employees within each department based on highest sales.

select *,row_number() over(partition by department order by sales_amount desc) as row_num from employee_sales;

--4.Find the highest-selling record from each department using ROW_NUMBER().
select * from(
select employee_name,department,sale_date,sales_amount,row_number() 
over(partition by department order by sales_amount desc) as row_num from employee_sales)
where row_num=1;

--5.Find the latest sales record of each employee using ROW_NUMBER().

select employee_name,department,sale_date,sales_amount,row_number() 
over(partition by department order by sale_date desc) as row_num from employee_sales;

--6.Rank all sales records based on sales_amount from highest to lowest.

select employee_name,department,sale_date,sales_amount,rank() over(order by sales_amount desc) as sales_rank
from employee_sales;

--7.Rank employees separately within each department based on sales_amount.

select employee_name,department,sale_date,sales_amount,rank() 
over(partition by department order by sales_amount desc) as sales_rank from employee_sales;

--8.Find the top 3 sales records in each department using RANK().

select * from (
select employee_name,department,sale_date,sales_amount,rank() 
over(partition by department order by sales_amount desc) as sales_rank from employee_sales)
where sales_rank<=3;

--9.Display employees whose rank within their department is 1.
select * from(
	select employee_name,department,sale_date,sales_amount,rank() 
	over(partition by department order by sales_amount desc) as sales_rank from employee_sales
) where sales_rank=1;

--10.Compare RANK() with ROW_NUMBER() when two employees have the same sales amount.

select employee_name,department,sale_date,sales_amount,
	rank() over(order by sales_amount desc) as sales_rank,
	row_number() over(order by sales_amount desc) as row_num from employee_sales;


--11.Rank all sales using DENSE_RANK() based on sales amount.

select employee_name,department,sale_date,sales_amount,dense_rank() 
over(order by sales_amount desc) as d_rank from employee_sales;


--12.Rank employees within each department using DENSE_RANK().

select employee_name,department,sale_date,sales_amount,dense_rank() 
over(partition by department order by sales_amount desc) as d_rank from employee_sales;

--13.Find the top 3 distinct sales amounts in each department.

select distinct * from(
	select employee_name,department,sale_date,sales_amount,dense_rank() 
	over(partition by department order by sales_amount desc) as d_rank from employee_sales
	) where d_rank<=3;

--14.Display the difference between RANK() and DENSE_RANK() for every record.

select employee_name,department,sale_date,sales_amount,
	dense_rank() over(partition by department order by sales_amount desc) as d_rank,
	rank() over (partition by department order by sales_amount desc) as sales_rank
from employee_sales;

--15.Find all employees who achieved the second-highest sales amount within their department.

select distinct * from (
select employee_name,department,sale_date,sales_amount,
	dense_rank() over(partition by department order by sales_amount desc) as d_rank
from employee_sales) where d_rank=2;

--16.Calculate the total sales for each department while still displaying every individual record.

select employee_name,department,sale_date,sales_amount,
	max(sales_amount) over(partition by department) as max_sales
from employee_sales;

--17.Calculate the average sales for each department alongside every employee's sale.

select employee_name,department,sale_date,sales_amount,
	avg(sales_amount) over(partition by department) as avg_sales
from employee_sales;

--18.Calculate the maximum sale achieved in each department.

select distinct department,max(sales_amount) over(partition by department)
as max_sales from employee_sales; 

--19.Calculate the minimum sale achieved in each department.

select distinct department,min(sales_amount) over(partition by department)
as min_sales from employee_sales;

--20.Display each employee's sales and the total sales of their department.

select employee_name,department,sale_date,sales_amount,
	sum(sales_amount) over(partition by department) as total_s_a from employee_sales;

--21.Display each employee's sales and calculate: employee sales / department total sales

select employee_name,department,sale_date,sales_amount,round( 100*
	sales_amount/sum(sales_amount) over(partition by department),2) as percatage_amount from employee_sales;
	
--22.Calculate the running total of sales across all employees ordered by sale_date.

select employee_name,department,sale_date,sales_amount,
sum(sales_amount) over(order by sale_date desc) as running_total from employee_sales;

--23.Calculate a running total separately for each department.

select employee_name,department,sale_date,sales_amount,
sum(sales_amount) over(partition by department order by sales_amount desc) as running_amount from employee_sales;

--24.Display each employee's current sales and their previous month's sales.

select employee_name,department,sale_date,sales_amount,
lag(sales_amount) over(partition by employee_name order by sale_date) as prev_sale from employee_sales;


--25.Display each employee's current sales and their next month's sales.

select employee_name,department,sale_date,sales_amount,
lead(sales_amount) over(partition by employee_name order by sale_date) as next_sale from employee_sales;

--26.Calculate the difference between current month's sales and previous month's sales.

select employee_name,department,sale_date,sales_amount,
round(sales_amount-lag(sales_amount) over(partition by employee_name order by sale_date),2) as r_sale
from employee_sales;

--27.For each employee, display their first recorded sales amount alongside every record

select distinct employee_name,department,sale_date,sales_amount,
first_value(sale_date) over(partition by employee_name order by sales_amount) as f_record from employee_sales;

--28.For each employee, display their highest sales amount using a window function.

select employee_name,department,sale_date,sales_amount,
first_value(sales_amount) over(partition by employee_name order by sales_amount desc) as highest_amount from employee_sales;

--29.For each department, display the first employee's sales amount based on sale_date.

select employee_name,department,sale_date,sales_amount,
first_value(sales_amount) over(partition by department order by sale_date) as first_sales_amount 
from employee_sales;

--30.For each department, display the latest sales amount based on sale_date.

select employee_name,department,sale_date,sales_amount,
last_value(sales_amount) over(partition by department order by sale_date 
rows between unbounded preceding and unbounded following) as latest_amount
from employee_sales;

--31.For each employee, display their 2nd recorded sales amount alongside every record.

select employee_name,department,sale_date,sales_amount,
nth_value(sales_amount,2) over(partition by employee_name rows between unbounded preceding and unbounded following)
as sec_sale_amount from employee_sales;

--32.For each department, display the 3rd highest sales amount using a window function.

select employee_name,department,sale_date,sales_amount,
nth_value(sales_amount,3) over(partition by department rows between unbounded preceding and unbounded following)
as third_sale_amount from employee_sales;

--33.Divide all sales records into 4 performance groups using NTILE(4).

select employee_name,department,sale_date,sales_amount,
ntile(4) over(order by sales_amount desc) as part from employee_sales;

--34.Divide employees within each department into 4 performance groups.

select employee_name,department,sale_date,sales_amount,
ntile(4) over(partition by department order by sales_amount desc) as part from employee_sales;

----advanced questions---------

--35.Find the top 3 employees in each department, but include ties.

select * from (
select employee_name,department,sale_date,sales_amount,
dense_rank() over(partition by department order by sales_amount) as d_rank from employee_sales)
where d_rank<=3;

--36.Find the top 3 employees in each department without including ties.

select distinct * from(
select employee_name,department,sale_date,sales_amount,
rank() over(partition by department order by sales_amount desc) as sales_rank from employee_sales)
where sales_rank <=3;

--37.Find employees whose sales are greater than the previous month's sales for at least two consecutive months.

select employee_name,department,sale_date,sales_amount,
rank() over()





