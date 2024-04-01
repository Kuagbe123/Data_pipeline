-- 1. Count the number of customers
SELECT COUNT(*) AS total_customers FROM customer_data;

-- 2. Find customers who prefer the app over the website
SELECT * FROM customer_data WHERE app_preference = 'Yes' AND website_preference = 'No';

-- 3. Get the top 10 customers with the highest transaction activity
SELECT * FROM customer_data ORDER BY transaction_activity DESC LIMIT 10;

-- 4. Find customers who have a specific email domain
SELECT * FROM customer_data WHERE email LIKE '%@example.com%';

-- 5. Calculate the average transaction activity
SELECT AVG(transaction_activity) AS avg_transaction_activity FROM customer_data;

-- 6. Find customers with transaction activity above a certain threshold
SELECT * FROM customer_data WHERE transaction_activity > 500;

-- 7. Count the number of customers who prefer using the app
SELECT COUNT(*) AS app_users FROM customer_data WHERE app_preference = 'Yes';

-- 8. Get the email addresses of customers with the lowest transaction activity
SELECT email FROM customer_data ORDER BY transaction_activity ASC LIMIT 10;

-- 9. Find customers who have both app and website preferences
SELECT * FROM customer_data WHERE app_preference = 'Yes' AND website_preference = 'Yes';

-- 10. Calculate the total transaction activity of all customers
SELECT SUM(transaction_activity) AS total_transaction_activity FROM customer_data;
