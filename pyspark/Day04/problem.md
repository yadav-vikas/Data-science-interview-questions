# 📝 Problem 1: PySpark – Detect Outlier Transactions per Day

### **Problem Statement**

You have a PySpark DataFrame with daily transaction amounts. For each day, identify **transactions greater than the average amount for that day** (outliers).

### **Sample Input** (`transactions`)

| txn\_date  | txn\_id | amount |
| ---------- | ------- | ------ |
| 2025-01-01 | T1      | 100    |
| 2025-01-01 | T2      | 200    |
| 2025-01-01 | T3      | 500    |
| 2025-01-02 | T4      | 300    |
| 2025-01-02 | T5      | 400    |
| 2025-01-02 | T6      | 600    |

### **Expected Output**

| txn\_date  | txn\_id | amount |
| ---------- | ------- | ------ |
| 2025-01-01 | T3      | 500    |
| 2025-01-02 | T6      | 600    |

---

# 📝 Problem 2: SQL – Find Employees Always Reporting to the Same Manager

### **Problem Statement**

You have a table `employee_manager(emp_id, manager_id, change_date)` showing employees' managers over time. Write a SQL query to find employees who **never changed their manager** across all records.

### **Sample Input** (`employee_manager`)

| emp\_id | manager\_id | change\_date |
| ------- | ----------- | ------------ |
| 1       | 10          | 2025-01-01   |
| 1       | 10          | 2025-02-01   |
| 2       | 11          | 2025-01-01   |
| 2       | 12          | 2025-03-01   |
| 3       | 13          | 2025-01-05   |

### **Expected Output**

| emp\_id |
| ------- |
| 1       |
| 3       |

---