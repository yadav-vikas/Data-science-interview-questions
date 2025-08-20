# 📝 Problem 1: PySpark – Find Top N Products per Category

### **Problem Statement**

You have a PySpark DataFrame containing product sales. Each product belongs to a category, and you need to find the **top 2 products by sales amount within each category**.

### **Sample Input** (`products`)

| category    | product | sales |
| ----------- | ------- | ----- |
| Electronics | Laptop  | 1200  |
| Electronics | Phone   | 900   |
| Electronics | Tablet  | 700   |
| Clothing    | Shirt   | 400   |
| Clothing    | Jeans   | 600   |
| Clothing    | Jacket  | 800   |

### **Expected Output**

| category    | product | sales |
| ----------- | ------- | ----- |
| Electronics | Laptop  | 1200  |
| Electronics | Phone   | 900   |
| Clothing    | Jacket  | 800   |
| Clothing    | Jeans   | 600   |

---

# 📝 Problem 2: SQL – Calculate Running Balance

### **Problem Statement**

You are given a SQL table `transactions(user_id, txn_date, amount)` where **amount** can be positive (credit) or negative (debit). Write a SQL query to calculate the **running balance** for each user ordered by `txn_date`.

### **Sample Input** (`transactions`)

| user\_id | txn\_date  | amount |
| -------- | ---------- | ------ |
| 1        | 2025-01-01 | 500    |
| 1        | 2025-01-03 | -200   |
| 1        | 2025-01-05 | 300    |
| 2        | 2025-01-02 | 1000   |
| 2        | 2025-01-04 | -400   |

### **Expected Output**

| user\_id | txn\_date  | amount | running\_balance |
| -------- | ---------- | ------ | ---------------- |
| 1        | 2025-01-01 | 500    | 500              |
| 1        | 2025-01-03 | -200   | 300              |
| 1        | 2025-01-05 | 300    | 600              |
| 2        | 2025-01-02 | 1000   | 1000             |
| 2        | 2025-01-04 | -400   | 600              |

---
