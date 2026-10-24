import tkinter as tk
from tkinter import ttk, messagebox

# Employee Salary Ranking System
# DAA Mini Project - Python + Tkinter
# Algorithm: Selection Sort
# Searching: Binary Search by Employee ID

employees = []

def add_employee():
    emp_id = entry_id.get().strip()
    name = entry_name.get().strip()
    salary_text = entry_salary.get().strip()

    if not emp_id or not name or not salary_text:
        messagebox.showwarning("Missing Data", "Please enter Employee ID, Name and Salary.")
        return

    try:
        emp_id = int(emp_id)
        salary = float(salary_text)
    except ValueError:
        messagebox.showerror("Invalid Data", "Employee ID and Salary must be numeric.")
        return

    if salary < 0:
        messagebox.showerror("Invalid Salary", "Salary cannot be negative.")
        return

    if any(emp["id"] == emp_id for emp in employees):
        messagebox.showerror("Duplicate ID", "Employee ID already exists.")
        return

    employees.append({
        "id": emp_id,
        "name": name,
        "salary": salary
    })

    clear_inputs()
    display_employees()


def clear_inputs():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_salary.delete(0, tk.END)
    entry_id.focus()


def selection_sort_by_salary():
    """Sort employees in descending order of salary.
    Time Complexity: O(n^2)
    Space Complexity: O(1) auxiliary space for the sorting process.
    """
    n = len(employees)

    for i in range(n - 1):
        max_index = i

        for j in range(i + 1, n):
            if employees[j]["salary"] > employees[max_index]["salary"]:
                max_index = j

        employees[i], employees[max_index] = employees[max_index], employees[i]


def rank_employees():
    if not employees:
        messagebox.showinfo("No Data", "Please add employees first.")
        return

    selection_sort_by_salary()
    display_employees()


def binary_search_employee(emp_id):
    """Binary search by Employee ID.
    The list is temporarily sorted by ID.
    Time Complexity: O(log n) after sorting.
    """
    sorted_employees = sorted(employees, key=lambda emp: emp["id"])

    low = 0
    high = len(sorted_employees) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_employees[mid]["id"] == emp_id:
            return sorted_employees[mid]
        elif sorted_employees[mid]["id"] < emp_id:
            low = mid + 1
        else:
            high = mid - 1

    return None


def search_employee():
    text = entry_search.get().strip()

    if not text:
        messagebox.showwarning("Search", "Enter an Employee ID.")
        return

    try:
        emp_id = int(text)
    except ValueError:
        messagebox.showerror("Invalid ID", "Employee ID must be numeric.")
        return

    employee = binary_search_employee(emp_id)

    if employee:
        messagebox.showinfo(
            "Employee Found",
            f"Employee ID: {employee['id']}\n"
            f"Name: {employee['name']}\n"
            f"Salary: ₹{employee['salary']:,.2f}"
        )
    else:
        messagebox.showinfo("Not Found", "Employee not found.")

def delete_selected():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Delete", "Select an employee from the table.")
        return

    item = tree.item(selected[0])
    emp_id = int(item["values"][1])

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            break

    display_employees()


def display_employees():
    for item in tree.get_children():
        tree.delete(item)

    for rank, emp in enumerate(employees, start=1):
        tree.insert(
            "",
            tk.END,
            values=(
                rank,
                emp["id"],
                emp["name"],
                f"₹{emp['salary']:,.2f}"
            )
        )

    count_label.config(text=f"Total Employees: {len(employees)}")

# ---------------------- GUI ----------------------

root = tk.Tk()
root.title("Employee Salary Ranking System")
root.geometry("850x600")
root.minsize(750, 520)

title = tk.Label(
    root,
    text="EMPLOYEE SALARY RANKING SYSTEM",
    font=("Arial", 20, "bold"),
    pady=15
)
title.pack()

subtitle = tk.Label(
    root,
    text="DAA Mini Project | Selection Sort + Binary Search",
    font=("Arial", 11)
)
subtitle.pack()

input_frame = tk.Frame(root, padx=15, pady=15)
input_frame.pack(fill="x")

tk.Label(input_frame, text="Employee ID:", font=("Arial", 11)).grid(
    row=0, column=0, padx=5, pady=5, sticky="e"
)
entry_id = tk.Entry(input_frame, width=20)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Employee Name:", font=("Arial", 11)).grid(
    row=0, column=2, padx=5, pady=5, sticky="e"
)
entry_name = tk.Entry(input_frame, width=20)
entry_name.grid(row=0, column=3, padx=5, pady=5)

tk.Label(input_frame, text="Salary:", font=("Arial", 11)).grid(
    row=1, column=0, padx=5, pady=5, sticky="e"
)
entry_salary = tk.Entry(input_frame, width=20)
entry_salary.grid(row=1, column=1, padx=5, pady=5)

tk.Button(
    input_frame,
    text="Add Employee",
    command=add_employee,
    width=18
).grid(row=1, column=2, padx=5, pady=5)

tk.Button(
    input_frame,
    text="Rank by Salary",
    command=rank_employees,
    width=18
).grid(row=1, column=3, padx=5, pady=5)

search_frame = tk.Frame(root, pady=5)
search_frame.pack(fill="x")

tk.Label(search_frame, text="Search Employee ID:", font=("Arial", 11)).pack(
    side="left", padx=(20, 5)
)

entry_search = tk.Entry(search_frame, width=18)
entry_search.pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Binary Search",
    command=search_employee,
    width=15
).pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Delete Selected",
    command=delete_selected,
    width=15
).pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Clear Inputs",
    command=clear_inputs,
    width=15
).pack(side="left", padx=5)

table_frame = tk.Frame(root, padx=20, pady=15)
table_frame.pack(fill="both", expand=True)

columns = ("rank", "id", "name", "salary")

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=12
)

tree.heading("rank", text="Rank")
tree.heading("id", text="Employee ID")
tree.heading("name", text="Employee Name")
tree.heading("salary", text="Salary")

tree.column("rank", width=80, anchor="center")
tree.column("id", width=130, anchor="center")
tree.column("name", width=250, anchor="center")
tree.column("salary", width=180, anchor="center")

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=tree.yview
)

tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

count_label = tk.Label(
    root,
    text="Total Employees: 0",
    font=("Arial", 11, "bold"),
    pady=10
)
count_label.pack()

entry_id.focus()

root.mainloop()