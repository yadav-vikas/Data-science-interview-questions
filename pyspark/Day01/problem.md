# 📝 Problem 1: PySpark – Detect Missing Dates in a Time Series

### **Problem Statement**

You are given a PySpark DataFrame containing daily sales records. However, some dates are missing. Write a PySpark program to **identify all the missing dates** within the given range of dates.

### **Sample Input** (DataFrame `sales`)

| date       | sales |
| ---------- | ----- |
| 2025-01-01 | 100   |
| 2025-01-02 | 150   |
| 2025-01-04 | 120   |
| 2025-01-06 | 200   |

### **Expected Output**

| missing\_date |
| ------------- |
| 2025-01-03    |
| 2025-01-05    |

---

# 📝 Problem 2: SQL – Find the Longest Streak of Active Days per User

### **Problem Statement**

You are given a SQL table `user_logins(user_id, login_date)`. Write a SQL query to find the **longest streak of consecutive login days** for each user.

### **Sample Input** (`user_logins`)

| user\_id | login\_date |
| -------- | ----------- |
| 1        | 2025-01-01  |
| 1        | 2025-01-02  |
| 1        | 2025-01-04  |
| 2        | 2025-01-01  |
| 2        | 2025-01-02  |
| 2        | 2025-01-03  |
| 2        | 2025-01-05  |

### **Expected Output**

| user\_id | longest\_streak |
| -------- | --------------- |
| 1        | 2               |
| 2        | 3               |

---
