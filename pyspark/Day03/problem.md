# 📝 Problem 1: PySpark – Identify First Purchase per Customer

### **Problem Statement**

You have a PySpark DataFrame containing customer purchase data. Each row represents a purchase. Write a PySpark program to **find the first purchase date for each customer** and the amount spent on that date.

### **Sample Input** (`purchases`)

| customer\_id | purchase\_date | amount |
| ------------ | -------------- | ------ |
| 101          | 2025-01-03     | 250    |
| 101          | 2025-01-05     | 300    |
| 102          | 2025-01-01     | 150    |
| 102          | 2025-01-02     | 200    |
| 103          | 2025-01-04     | 500    |

### **Expected Output**

| customer\_id | first\_purchase\_date | amount |
| ------------ | --------------------- | ------ |
| 101          | 2025-01-03            | 250    |
| 102          | 2025-01-01            | 150    |
| 103          | 2025-01-04            | 500    |

---

# 📝 Problem 2: SQL – Detect Employees with Salary Changes

### **Problem Statement**

You have a table `employee_salaries(emp_id, effective_date, salary)` containing salary history for employees. Write a SQL query to **find employees whose salary changed more than once** and display the number of changes for each.

### **Sample Input** (`employee_salaries`)

| emp\_id | effective\_date | salary |
| ------- | --------------- | ------ |
| 1       | 2025-01-01      | 50000  |
| 1       | 2025-02-01      | 55000  |
| 1       | 2025-03-01      | 60000  |
| 2       | 2025-01-15      | 40000  |
| 2       | 2025-03-01      | 45000  |
| 3       | 2025-01-10      | 30000  |

### **Expected Output**

| emp\_id | salary\_change\_count |
| ------- | --------------------- |
| 1       | 2                     |
| 2       | 1                     |

---