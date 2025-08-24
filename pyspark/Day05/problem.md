# 📝 Problem 1: PySpark – Calculate Percentage Contribution of Each Product

### **Problem Statement**

You have a PySpark DataFrame with total sales for different products. Write a PySpark program to **calculate the percentage contribution of each product** towards the total sales across all products.

### **Sample Input** (`product_sales`)

| product | sales |
| ------- | ----- |
| Laptop  | 1200  |
| Phone   | 800   |
| Tablet  | 500   |
| Desktop | 500   |

### **Expected Output**

| product | sales | percentage\_contribution |
| ------- | ----- | ------------------------ |
| Laptop  | 1200  | 40.0                     |
| Phone   | 800   | 26.7                     |
| Tablet  | 500   | 16.7                     |
| Desktop | 500   | 16.7                     |

*(Percentages rounded to 1 decimal place)*

---

# 📝 Problem 2: SQL – Identify Months with No Transactions

### **Problem Statement**

You have a SQL table `transactions(txn_id, txn_date, amount)`. Write a query to find **months in 2025 where there were no transactions**. Assume `txn_date` is in `YYYY-MM-DD` format.

### **Sample Input** (`transactions`)

| txn\_id | txn\_date  | amount |
| ------- | ---------- | ------ |
| T1      | 2025-01-10 | 100    |
| T2      | 2025-01-15 | 200    |
| T3      | 2025-03-05 | 300    |
| T4      | 2025-05-20 | 400    |

### **Expected Output**

| missing\_month |
| -------------- |
| 2025-02        |
| 2025-04        |
| 2025-06        |
| 2025-07        |
| 2025-08        |
| 2025-09        |
| 2025-10        |
| 2025-11        |
| 2025-12        |

---