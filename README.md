# Employee Salary Ranking System

**DAA Mini Project | Python**

## 📌 About the Project
The Employee Salary Ranking System is a Python-based application developed as a mini project for Design and Analysis of Algorithms (DAA). It allows users to manage employee records, rank employees according to their salaries, and search for employees using their Employee ID.

## ✨ Features
- Add employee details
- Rank employees by salary in descending order
- Search employees using Employee ID
- Delete employee records
- Display employee rankings in a graphical interface

## 🛠️ Technologies Used
- Python 3
- Tkinter for the graphical user interface
- Data Structures and Algorithms

## 🧠 Algorithms Used

### 1. Selection Sort
Used to arrange employees in descending order of salary.

- Time Complexity: O(n²)
- Auxiliary Space Complexity: O(1)

### 2. Binary Search
Used to search for an employee by Employee ID after arranging employee records by ID.

- Time Complexity: O(log n) for the search phase
- Space Complexity: O(n) for the temporary sorted list used by the current implementation

## ▶️ How to Run
1. Install Python 3 on your computer.
2. Download `employee_salary_ranking_system.py` from this repository.
3. Open a terminal in the downloaded file's folder.
4. Run:

```bash
python employee_salary_ranking_system.py
```

Tkinter is included with many standard Python installations. On some Linux systems, it may need to be installed separately.

## 🎓 Project Purpose
This project demonstrates the practical application of sorting and searching algorithms, along with their time and space complexity, in a simple employee management system.
