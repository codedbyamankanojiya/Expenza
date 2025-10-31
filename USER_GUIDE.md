# 📖 User Guide - Professional Expense Tracker

**Developer**: Aman Kanojiya

## Table of Contents
1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Basic Operations](#basic-operations)
4. [Advanced Features](#advanced-features)
5. [Tips & Best Practices](#tips--best-practices)
6. [Troubleshooting](#troubleshooting)

---

## Getting Started

### First Launch

When you first launch the application:
1. The main window will open with an empty expense list
2. A file named `expenses.csv` will be automatically created in the same directory
3. All statistics will show zero values

### Understanding the Interface

The application is divided into four main sections:

```
┌─────────────────────────────────────────────────────────┐
│  1. Input Section    │  2. Statistics & Search Panel    │
│  (Left Top)          │  (Right Side)                    │
├──────────────────────┴──────────────────────────────────┤
│  3. Action Buttons                                      │
│  (Left Middle)                                          │
├─────────────────────────────────────────────────────────┤
│  4. Expense Records Table                               │
│  (Bottom - Full Width)                                  │
└─────────────────────────────────────────────────────────┘
```

---

## Interface Overview

### 1. Input Section
**Purpose**: Add new expenses or edit existing ones

**Fields**:
- **Category**: Type of expense (Food, Transport, etc.)
- **Amount**: Cost in rupees (numbers only)
- **Description**: Brief note about the expense

### 2. Statistics Panel
**Purpose**: Real-time overview of your spending

**Displays**:
- **Total Expenses**: Sum of all expense amounts
- **Total Entries**: Number of expense records
- **Categories**: Count of unique categories used

### 3. Search & Filter Panel
**Purpose**: Quickly find specific expenses

**Tools**:
- **Search Box**: Type to filter expenses in real-time
- **Category Filter**: Dropdown to show only specific categories
- **Reset View**: Button to clear all filters

### 4. Action Buttons
**Purpose**: Perform operations on expenses

**Buttons**:
- ➕ **Add Expense**: Save a new expense
- ✏️ **Edit**: Modify selected expense
- 🗑️ **Delete**: Remove selected expense
- 🔄 **Clear Fields**: Empty all input fields
- 📤 **Export**: Save data to file
- 📊 **View Charts**: Open visualization window
- 📋 **Generate Report**: Create period-based summaries

### 5. Expense Records Table
**Purpose**: Display all expenses in organized format

**Columns**:
- **Date**: When the expense was recorded (YYYY-MM-DD)
- **Category**: Type of expense
- **Amount**: Cost in rupees
- **Description**: Details about the expense

---

## Basic Operations

### Adding an Expense

**Step-by-Step**:
1. Click in the **Category** field
2. Type the category name (e.g., "Food", "Transport")
3. Press Tab or click in the **Amount** field
4. Enter the amount (numbers only, e.g., "250.50")
5. Press Tab or click in the **Description** field
6. Type a brief description (e.g., "Lunch at cafe")
7. Click **➕ Add Expense** button
8. A success message will appear
9. The expense will be added to the table
10. Statistics will update automatically

**Example**:
```
Category: Food
Amount: 250.50
Description: Lunch at downtown cafe
```

**Tips**:
- Use consistent category names for better analytics
- Be specific in descriptions for future reference
- Amount accepts decimals (e.g., 250.50)

### Editing an Expense

**Step-by-Step**:
1. Click on the expense you want to edit in the table
2. The row will be highlighted
3. Click **✏️ Edit** button
4. The expense details will populate the input fields
5. Modify any field as needed
6. Click **➕ Add Expense** to save changes
7. The old entry is removed and new one is added

**Note**: The date will be updated to the current date when you save the edited expense.

### Deleting an Expense

**Step-by-Step**:
1. Click on the expense you want to delete
2. Click **🗑️ Delete** button
3. A confirmation dialog will appear
4. Click **Yes** to confirm deletion
5. The expense will be removed
6. Statistics will update automatically

**Warning**: Deletion is permanent and cannot be undone!

### Clearing Input Fields

**Purpose**: Quickly empty all input fields to start fresh

**How to Use**:
- Click **🔄 Clear Fields** button
- All three input fields will be emptied
- Useful when you want to cancel an edit or start a new entry

---

## Advanced Features

### 🔍 Smart Search

**How It Works**:
- Type any text in the search box
- Results filter in real-time as you type
- Searches across ALL fields (date, category, amount, description)
- Case-insensitive search

**Examples**:
- Type "food" → Shows all food-related expenses
- Type "250" → Shows all expenses with 250 in amount
- Type "cafe" → Shows expenses with "cafe" in description
- Type "2024-01" → Shows all January 2024 expenses

**To Clear Search**:
- Delete text from search box, OR
- Click **Reset View** button

### 🎯 Category Filter

**How It Works**:
- Click the category dropdown
- Select a specific category
- Only expenses from that category will be shown

**Available Categories**:
- All (shows everything)
- Food
- Transport
- Entertainment
- Bills
- Shopping
- Health
- Other

**To Clear Filter**:
- Select "All" from dropdown, OR
- Click **Reset View** button

### 📊 Visual Charts

**How to Access**:
1. Click **📊 View Charts** button
2. A new window will open with two charts

**Chart Types**:

1. **Pie Chart** (Left)
   - Shows percentage distribution
   - Each category has a different color
   - Percentages displayed on slices
   - Great for seeing spending proportions

2. **Bar Chart** (Right)
   - Shows actual amounts per category
   - Y-axis shows amount in rupees
   - X-axis shows categories
   - Easy comparison of spending levels

**Tips**:
- Charts update based on ALL expenses (not filtered view)
- Close chart window to return to main application
- Generate charts regularly to track spending patterns

### 📋 Generate Reports

**How to Access**:
1. Click **📋 Generate Report** button
2. Select report period from dropdown menu

**Report Types**:

1. **📅 Daily Report**
   - Shows today's expenses only
   - Total spending for the current day

2. **📆 Weekly Report**
   - Shows last 7 days
   - Total spending for the week

3. **📊 Monthly Report**
   - Shows current month (from 1st to today)
   - Total spending for the month

4. **📈 Yearly Report**
   - Shows current year (from Jan 1 to today)
   - Total spending for the year

**Report Display**:
- A popup window shows the total amount
- Format: "Total spent in the [period]: Rs X.XX"

**Example**:
```
Report
Total spent in the month: Rs 15,250.75
```

### 📤 Export Data

**How to Export**:
1. Click **📤 Export** button
2. A file dialog will open
3. Choose save location
4. Select file format (CSV or JSON)
5. Click Save

**Export Formats**:

1. **CSV Format** (.csv)
   - Opens in Excel, Google Sheets
   - Maintains table structure
   - Easy to share and analyze
   - Example structure:
   ```csv
   Date,Category,Amount,Description
   2024-01-15,Food,250.50,Lunch at cafe
   2024-01-15,Transport,100.00,Taxi fare
   ```

2. **JSON Format** (.json)
   - Structured data format
   - Good for backups
   - Programmatically accessible
   - Example structure:
   ```json
   [
     {
       "Date": "2024-01-15",
       "Category": "Food",
       "Amount": "250.50",
       "Description": "Lunch at cafe"
     }
   ]
   ```

**Use Cases**:
- **Regular Backups**: Export weekly to prevent data loss
- **Tax Preparation**: Export yearly data for tax filing
- **Sharing**: Send CSV to accountant or family member
- **Analysis**: Import into Excel for advanced analysis

---

## Tips & Best Practices

### Data Entry Tips

1. **Consistent Categories**
   - Use the same category names every time
   - "Food" not "food" or "FOOD" or "Foods"
   - Helps with filtering and analytics

2. **Descriptive Details**
   - Be specific: "Lunch at Cafe Coffee Day" not just "Food"
   - Include location if relevant
   - Note payment method if needed

3. **Regular Updates**
   - Add expenses daily for accuracy
   - Don't wait until end of week/month
   - Fresh memory = better descriptions

4. **Amount Precision**
   - Include cents/paise: 250.50 not 250
   - Double-check amounts before saving
   - Round up if unsure

### Organization Tips

1. **Category System**
   - Stick to predefined categories when possible
   - Create your own system if needed
   - Don't over-categorize (keep it simple)

2. **Regular Reviews**
   - Check statistics weekly
   - Generate monthly reports
   - View charts to spot patterns

3. **Data Hygiene**
   - Delete duplicate entries
   - Edit mistakes immediately
   - Keep descriptions clean and professional

### Backup Strategy

1. **Weekly Exports**
   - Export every Sunday
   - Save to cloud storage (Google Drive, Dropbox)
   - Name files with date: "expenses_2024_01_15.csv"

2. **Monthly Archives**
   - Create monthly export at month-end
   - Store in organized folder structure
   - Keep at least 12 months of history

3. **Multiple Formats**
   - Export both CSV and JSON
   - CSV for viewing, JSON for backup
   - Store in different locations

---

## Troubleshooting

### Common Issues

#### Issue: "Please fill all fields" warning

**Cause**: One or more input fields are empty

**Solution**:
1. Check that Category field has text
2. Check that Amount field has a number
3. Check that Description field has text
4. All three fields are required

#### Issue: "Invalid amount entered" error

**Cause**: Non-numeric value in Amount field

**Solution**:
1. Remove any letters or symbols
2. Use only numbers and decimal point
3. Examples: 250, 250.50, 1000.75
4. Don't use: Rs, $, commas, spaces

#### Issue: Search not working

**Cause**: No matching results

**Solution**:
1. Check spelling
2. Try partial words
3. Search is case-insensitive
4. Click "Reset View" to see all expenses

#### Issue: Charts not displaying

**Cause**: No expense data available

**Solution**:
1. Add at least one expense first
2. Ensure expenses have valid amounts
3. Check that expenses.csv file exists

#### Issue: Export fails

**Cause**: File permission or path issue

**Solution**:
1. Choose a different save location
2. Ensure you have write permissions
3. Close any open CSV files
4. Try a different filename

#### Issue: Statistics showing zero

**Cause**: No expenses added yet, or file corrupted

**Solution**:
1. Add an expense to test
2. Click "Reset View" button
3. Restart the application
4. Check if expenses.csv exists and is readable

### Data Recovery

#### If expenses.csv is deleted:

1. Application will create a new empty file
2. Previous data is lost unless you have a backup
3. Import from your last export file

#### If expenses.csv is corrupted:

1. Rename the corrupted file to expenses_old.csv
2. Restart the application (creates new file)
3. Manually copy valid entries from old file

### Performance Issues

#### Application running slow:

**Causes & Solutions**:
1. **Too many expenses**: 
   - Archive old expenses
   - Keep only current year in main file

2. **Chart generation slow**:
   - Normal for 1000+ expenses
   - Wait a few seconds
   - Consider filtering data first

3. **Search lagging**:
   - Clear search and try again
   - Restart application
   - Reduce total expense count

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Tab` | Move to next field |
| `Shift+Tab` | Move to previous field |
| `Enter` | Add expense (when in input field) |
| `Delete` | Delete selected expense |
| `Esc` | Clear all input fields |
| `Ctrl+A` | Select all text in current field |

---

## Data File Location

**Default Location**: Same folder as expensetracker.py

**File Name**: expenses.csv

**File Format**: CSV (Comma-Separated Values)

**Structure**:
```
Date,Category,Amount,Description
2024-01-15,Food,250.50,Lunch at cafe
```

**Manual Editing**:
- You can open expenses.csv in Excel
- Edit carefully to avoid corruption
- Always keep a backup before manual edits
- Close file before running application

---

## Getting Help

### In-App Help
- Hover over buttons for tooltips (if available)
- Error messages provide specific guidance
- Success messages confirm actions

### External Resources
- Check README.md for overview
- Visit GitHub repository for updates
- Contact maintainer (see README for details)

### Reporting Issues
1. Note the exact error message
2. List steps to reproduce the problem
3. Include your Python version
4. Open an issue on GitHub

---

## Appendix: Category Suggestions

### Food & Dining
- Groceries
- Restaurant
- Fast Food
- Coffee/Tea
- Snacks

### Transportation
- Fuel/Gas
- Public Transit
- Taxi/Uber
- Parking
- Vehicle Maintenance

### Entertainment
- Movies
- Concerts
- Games
- Subscriptions (Netflix, etc.)
- Hobbies

### Bills & Utilities
- Electricity
- Water
- Internet
- Phone
- Rent/Mortgage

### Shopping
- Clothing
- Electronics
- Home Goods
- Gifts
- Personal Care

### Health & Fitness
- Doctor Visits
- Medications
- Gym Membership
- Sports Equipment
- Health Insurance

### Other
- Education
- Charity/Donations
- Pet Care
- Travel
- Miscellaneous

---

<div align="center">

**Happy Expense Tracking! 💰**

*For more information, see README.md*

</div>
