-- Assuming a table named customers with fields customerID and customerFirstName
-- Assuming a table named orders with fields customerID, orderCost
SELECT customerFirstName, totalCost FROM (
        SELECT customerID, customerFirstName, SUM(orderCost) AS totalCost
        FROM customers AS c
        LEFT JOIN orders AS o
        ON c.customerID = o.customerID
        GROUP BY customerID, customerFirstName)
ORDER BY totalCost
LIMIT 5