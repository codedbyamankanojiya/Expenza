import csv
import json
import os
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox, filedialog
from datetime import datetime, timedelta
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# File to store expenses
FILE_NAME = 'expenses.csv'

# Function to initialize file
def initialize_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
    except FileExistsError:
        pass

# Function to add a new expense
def add_expense():
    date = datetime.now().strftime('%Y-%m-%d')
    category = category_var.get()
    amount = amount_var.get()
    description = description_var.get()

    if not category or not amount or not description:
        messagebox.showwarning("Warning", "Please fill all fields.")
        return
    
    try:
        with open(FILE_NAME, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, float(amount), description])
        messagebox.showinfo("Success", "Expense added successfully!")
        clear_fields()
        view_expenses()
        update_statistics()
    except ValueError:
        messagebox.showerror("Error", "Invalid amount entered.")

# Function to clear fields
def clear_fields():
    category_var.set('')
    amount_var.set('')
    description_var.set('')

# Function to view all expenses
def view_expenses():
    for row in tree.get_children():
        tree.delete(row)
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            try:
                header = next(reader)  # Skip header if present
                for row in reader:
                    tree.insert('', END, values=row)
            except StopIteration:
                pass  # File exists but is empty
    except FileNotFoundError:
        pass

# Function to delete selected expense
def delete_expense():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select an expense to delete.")
        return
    
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this expense?"):
        item_values = tree.item(selected_item[0])['values']
        
        # Read all expenses
        expenses = []
        try:
            with open(FILE_NAME, 'r') as file:
                reader = csv.reader(file)
                header = next(reader)
                expenses = list(reader)
        except FileNotFoundError:
            return
        
        # Remove the selected expense
        expenses = [exp for exp in expenses if exp != [str(v) for v in item_values]]
        
        # Write back
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
            writer.writerows(expenses)
        
        messagebox.showinfo("Success", "Expense deleted successfully!")
        view_expenses()
        update_statistics()

# Function to edit selected expense
def edit_expense():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Please select an expense to edit.")
        return
    
    item_values = tree.item(selected_item[0])['values']
    
    # Populate fields with selected values
    category_var.set(item_values[1])
    amount_var.set(item_values[2])
    description_var.set(item_values[3])
    
    # Delete the old entry
    expenses = []
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            expenses = list(reader)
    except FileNotFoundError:
        return
    
    expenses = [exp for exp in expenses if exp != [str(v) for v in item_values]]
    
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        writer.writerows(expenses)
    
    view_expenses()
    messagebox.showinfo("Edit Mode", "Expense loaded for editing. Modify and click 'Add Expense'.")

# Function to search expenses
def search_expenses():
    search_term = search_var.get().lower()
    for row in tree.get_children():
        tree.delete(row)
    
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if any(search_term in str(cell).lower() for cell in row):
                    tree.insert('', END, values=row)
    except FileNotFoundError:
        pass

# Function to filter by category
def filter_by_category():
    category_filter = filter_var.get()
    for row in tree.get_children():
        tree.delete(row)
    
    if category_filter == "All":
        view_expenses()
        return
    
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 2 and row[1].lower() == category_filter.lower():
                    tree.insert('', END, values=row)
    except FileNotFoundError:
        pass

# Function to export expenses
def export_expenses():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv"), ("JSON files", "*.json"), ("All files", "*.*")]
    )
    
    if not file_path:
        return
    
    try:
        expenses = []
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            expenses = list(reader)
        
        if file_path.endswith('.json'):
            json_data = []
            for exp in expenses:
                json_data.append({
                    'Date': exp[0],
                    'Category': exp[1],
                    'Amount': exp[2],
                    'Description': exp[3]
                })
            with open(file_path, 'w') as f:
                json.dump(json_data, f, indent=4)
        else:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(expenses)
        
        messagebox.showinfo("Success", f"Expenses exported to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Export failed: {e}")

# Function to show expense chart
def show_chart():
    try:
        category_totals = defaultdict(float)
        
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 3:
                    category_totals[row[1]] += float(row[2])
        
        if not category_totals:
            messagebox.showinfo("Info", "No data available for chart.")
            return
        
        # Create chart window
        chart_window = tb.Toplevel(root)
        chart_window.title("Expense Distribution")
        chart_window.geometry("800x600")
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Pie chart
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())
        colors = plt.cm.Set3(range(len(categories)))
        
        ax1.pie(amounts, labels=categories, autopct='%1.1f%%', colors=colors, startangle=90)
        ax1.set_title('Expense Distribution by Category')
        
        # Bar chart
        ax2.bar(categories, amounts, color=colors)
        ax2.set_xlabel('Category')
        ax2.set_ylabel('Amount (Rs)')
        ax2.set_title('Expenses by Category')
        ax2.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=BOTH, expand=True)
        
    except FileNotFoundError:
        messagebox.showerror("Error", "No expense file found.")
    except Exception as e:
        messagebox.showerror("Error", f"Chart generation failed: {e}")

# Function to update statistics
def update_statistics():
    try:
        total = 0.0
        count = 0
        categories = set()
        
        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if len(row) >= 3:
                    total += float(row[2])
                    count += 1
                    categories.add(row[1])
        
        total_label.config(text=f"Total Expenses: Rs {total:.2f}")
        count_label.config(text=f"Total Entries: {count}")
        category_count_label.config(text=f"Categories: {len(categories)}")
    except FileNotFoundError:
        total_label.config(text="Total Expenses: Rs 0.00")
        count_label.config(text="Total Entries: 0")
        category_count_label.config(text="Categories: 0")

# Function to generate report
def generate_report(period):
    try:
        total_spent = 0.0
        cutoff_date = None
        today = datetime.now()

        if period == 'day':
            cutoff_date = today
        elif period == 'week':
            cutoff_date = today - timedelta(days=7)
        elif period == 'month':
            cutoff_date = today.replace(day=1)
        elif period == 'year':
            cutoff_date = today.replace(month=1, day=1)

        with open(FILE_NAME, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            for row in reader:
                # Ensure row has at least 3 columns (Date, Category, Amount)
                if len(row) < 3:
                    continue  # Skip incomplete rows
                row_date = datetime.strptime(row[0], '%Y-%m-%d')
                if row_date >= cutoff_date:
                    total_spent += float(row[2])

        messagebox.showinfo("Report", f"Total spent in the {period}: Rs {total_spent:.2f}")
    except FileNotFoundError:
        messagebox.showerror("Error", "No expense file found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Initialize file
initialize_file()

# Main GUI application
root = tb.Window(themename="superhero")
root.title("💰 Expenza")
root.geometry("1200x700")
root.resizable(True, True)

# Frame for input fields
input_frame = tb.Frame(root, padding=(10, 10))
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Input fields
tb.Label(input_frame, text="Category:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
category_var = tb.StringVar()
category_entry = tb.Entry(input_frame, textvariable=category_var, width=30)
category_entry.grid(row=0, column=1, padx=5, pady=5)


tb.Label(input_frame, text="Amount:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
amount_var = tb.StringVar()
amount_entry = tb.Entry(input_frame, textvariable=amount_var, width=30)
amount_entry.grid(row=1, column=1, padx=5, pady=5)


tb.Label(input_frame, text="Description:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
description_var = tb.StringVar()
description_entry = tb.Entry(input_frame, textvariable=description_var, width=30)
description_entry.grid(row=2, column=1, padx=5, pady=5)

# Statistics Panel
stats_frame = tb.Labelframe(root, text="📊 Statistics", padding=(10, 10), bootstyle="info")
stats_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew", rowspan=2)

total_label = tb.Label(stats_frame, text="Total Expenses: Rs 0.00", font=("Arial", 12, "bold"))
total_label.pack(pady=5, anchor="w")

count_label = tb.Label(stats_frame, text="Total Entries: 0", font=("Arial", 10))
count_label.pack(pady=5, anchor="w")

category_count_label = tb.Label(stats_frame, text="Categories: 0", font=("Arial", 10))
category_count_label.pack(pady=5, anchor="w")

# Search and Filter Frame
search_filter_frame = tb.Labelframe(stats_frame, text="🔍 Search & Filter", padding=(10, 10))
search_filter_frame.pack(pady=10, fill="both", expand=True)

tb.Label(search_filter_frame, text="Search:").pack(anchor="w", pady=2)
search_var = tb.StringVar()
search_entry = tb.Entry(search_filter_frame, textvariable=search_var, width=25)
search_entry.pack(fill="x", pady=2)
search_entry.bind('<KeyRelease>', lambda e: search_expenses())

tb.Label(search_filter_frame, text="Filter by Category:").pack(anchor="w", pady=2)
filter_var = tb.StringVar(value="All")
filter_combo = tb.Combobox(search_filter_frame, textvariable=filter_var, width=23, state="readonly")
filter_combo['values'] = ("All", "Food", "Transport", "Entertainment", "Bills", "Shopping", "Health", "Other")
filter_combo.pack(fill="x", pady=2)
filter_combo.bind('<<ComboboxSelected>>', lambda e: filter_by_category())

reset_btn = tb.Button(search_filter_frame, text="Reset View", command=view_expenses, bootstyle="secondary")
reset_btn.pack(pady=10, fill="x")

# Buttons
button_frame = tb.Frame(root, padding=(10, 10))
button_frame.grid(row=1, column=0, sticky="ew")

add_button = tb.Button(button_frame, text="➕ Add Expense", command=add_expense, bootstyle="success", width=15)
add_button.grid(row=0, column=0, padx=5, pady=5)

edit_button = tb.Button(button_frame, text="✏️ Edit", command=edit_expense, bootstyle="info", width=15)
edit_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tb.Button(button_frame, text="🗑️ Delete", command=delete_expense, bootstyle="danger", width=15)
delete_button.grid(row=0, column=2, padx=5, pady=5)

clear_button = tb.Button(button_frame, text="🔄 Clear Fields", command=clear_fields, bootstyle="warning", width=15)
clear_button.grid(row=0, column=3, padx=5, pady=5)

export_button = tb.Button(button_frame, text="📤 Export", command=export_expenses, bootstyle="secondary", width=15)
export_button.grid(row=1, column=0, padx=5, pady=5)

chart_button = tb.Button(button_frame, text="📊 View Charts", command=show_chart, bootstyle="primary", width=15)
chart_button.grid(row=1, column=1, padx=5, pady=5)

report_button = tb.Menubutton(button_frame, text="📋 Generate Report", bootstyle="info", width=15)
report_menu = tb.Menu(report_button, tearoff=0)
report_button['menu'] = report_menu
report_menu.add_command(label="📅 Daily Report", command=lambda: generate_report('day'))
report_menu.add_command(label="📆 Weekly Report", command=lambda: generate_report('week'))
report_menu.add_command(label="📊 Monthly Report", command=lambda: generate_report('month'))
report_menu.add_command(label="📈 Yearly Report", command=lambda: generate_report('year'))
report_button.grid(row=1, column=2, padx=5, pady=5)

# Expense list (Treeview)
tree_frame = tb.Labelframe(root, text="📝 Expense Records", padding=(10, 10), bootstyle="primary")
tree_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

columns = ('Date', 'Category', 'Amount', 'Description')
tree = tb.Treeview(tree_frame, columns=columns, show='headings', bootstyle="info", height=15)

for col in columns:
    tree.heading(col, text=col)
    if col == 'Description':
        tree.column(col, anchor=W, width=300)
    elif col == 'Amount':
        tree.column(col, anchor=E, width=100)
    else:
        tree.column(col, anchor=CENTER, width=150)

scrollbar = tb.Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
tree.pack(fill=BOTH, expand=True)

# Configure grid weights for responsive design
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)

# Load initial data and statistics
view_expenses()
update_statistics()

# Run the application
root.mainloop()