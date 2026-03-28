# 🏗️ Application Architecture

**Developer**: Aman Kanojiya

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│           Expenza                       │
│                    Desktop Application                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         Application Layers              │
        ├─────────────────────────────────────────┤
        │  1. Presentation Layer (UI)             │
        │  2. Business Logic Layer                │
        │  3. Data Access Layer                   │
        └─────────────────────────────────────────┘
```

---

## 1. Presentation Layer (UI)

### Component Hierarchy

```
tkinter.Window (root)
│
├── InputFrame (Grid 0,0)
│   ├── Label: "Category"
│   ├── Entry: category_var
│   ├── Label: "Amount"
│   ├── Entry: amount_var
│   ├── Label: "Description"
│   └── Entry: description_var
│
├── StatsFrame (Grid 0,1 rowspan=2)
│   ├── Label: total_label
│   ├── Label: count_label
│   ├── Label: category_count_label
│   └── SearchFilterFrame
│       ├── Label: "Search"
│       ├── Entry: search_var
│       ├── Label: "Filter by Category"
│       ├── Combobox: filter_var
│       └── Button: reset_btn
│
├── ButtonFrame (Grid 1,0)
│   ├── Button: add_button → add_expense()
│   ├── Button: edit_button → edit_expense()
│   ├── Button: delete_button → delete_expense()
│   ├── Button: clear_button → clear_fields()
│   ├── Button: export_button → export_expenses()
│   ├── Button: chart_button → show_chart()
│   └── Menubutton: report_button
│       └── Menu: report_menu
│           ├── daily → generate_report('day')
│           ├── weekly → generate_report('week')
│           ├── monthly → generate_report('month')
│           └── yearly → generate_report('year')
│
└── TreeFrame (Grid 2,0 columnspan=2)
    ├── Treeview: tree
    │   ├── Column: Date
    │   ├── Column: Category
    │   ├── Column: Amount
    │   └── Column: Description
    └── Scrollbar: scrollbar
```

---

## 2. Business Logic Layer

### Function Map

```
┌─────────────────────────────────────────────────────────┐
│                    Core Functions                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Data Management                                         │
│  ├── initialize_file()      → Create CSV if not exists  │
│  ├── add_expense()          → Add new expense           │
│  ├── edit_expense()         → Modify existing expense   │
│  ├── delete_expense()       → Remove expense            │
│  └── view_expenses()        → Load and display all      │
│                                                          │
│  Search & Filter                                         │
│  ├── search_expenses()      → Real-time search          │
│  └── filter_by_category()  → Category-based filter      │
│                                                          │
│  Analytics                                               │
│  ├── update_statistics()    → Calculate totals          │
│  ├── generate_report()      → Period-based reports      │
│  └── show_chart()          → Visual analytics           │
│                                                          │
│  Data Export                                             │
│  └── export_expenses()      → CSV/JSON export           │
│                                                          │
│  UI Helpers                                              │
│  └── clear_fields()         → Reset input fields        │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Function Dependencies

```
add_expense()
    ├── Validates input
    ├── Writes to CSV
    ├── Calls clear_fields()
    ├── Calls view_expenses()
    └── Calls update_statistics()

edit_expense()
    ├── Gets selected item
    ├── Populates input fields
    ├── Removes old entry
    └── Calls view_expenses()

delete_expense()
    ├── Gets selected item
    ├── Shows confirmation
    ├── Removes from CSV
    ├── Calls view_expenses()
    └── Calls update_statistics()

view_expenses()
    ├── Reads CSV file
    ├── Clears treeview
    └── Populates treeview

search_expenses()
    ├── Gets search term
    ├── Reads CSV file
    └── Filters and displays

filter_by_category()
    ├── Gets category filter
    ├── Reads CSV file
    └── Filters and displays

update_statistics()
    ├── Reads CSV file
    ├── Calculates totals
    └── Updates labels

generate_report()
    ├── Determines date range
    ├── Reads CSV file
    ├── Filters by date
    ├── Calculates total
    └── Shows messagebox

show_chart()
    ├── Reads CSV file
    ├── Aggregates by category
    ├── Creates matplotlib figure
    ├── Creates toplevel window
    └── Embeds chart

export_expenses()
    ├── Shows file dialog
    ├── Reads CSV file
    ├── Converts to format
    └── Writes to file
```

---

## 3. Data Access Layer

### Data Flow

```
┌──────────────────────────────────────────────────────────┐
│                    Data Storage                          │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  expenses.csv (Primary Storage)                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Date       │ Category  │ Amount │ Description   │    │
│  ├─────────────────────────────────────────────────┤    │
│  │ 2024-01-15 │ Food      │ 250.50 │ Lunch at cafe │    │
│  │ 2024-01-15 │ Transport │ 100.00 │ Taxi fare     │    │
│  └─────────────────────────────────────────────────┘    │
│                                                           │
│  Format: CSV (Comma-Separated Values)                    │
│  Encoding: UTF-8                                          │
│  Location: Same directory as script                      │
│                                                           │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│                  Data Operations                         │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  CREATE (Initialize)                                      │
│  └── initialize_file() → Create CSV with header          │
│                                                           │
│  READ (View/Search/Filter)                               │
│  ├── view_expenses() → Read all records                  │
│  ├── search_expenses() → Read and filter                 │
│  ├── filter_by_category() → Read and filter              │
│  ├── update_statistics() → Read and aggregate            │
│  ├── generate_report() → Read and calculate              │
│  └── show_chart() → Read and visualize                   │
│                                                           │
│  UPDATE (Edit)                                            │
│  └── edit_expense() → Read, modify, write                │
│                                                           │
│  DELETE                                                   │
│  └── delete_expense() → Read, remove, write              │
│                                                           │
│  APPEND (Add)                                             │
│  └── add_expense() → Append new record                   │
│                                                           │
│  EXPORT                                                   │
│  └── export_expenses() → Read and convert format         │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

---

## 4. Module Dependencies

### Import Structure

```
expenza.py
│
├── Standard Library
│   ├── csv              → CSV file operations
│   ├── json             → JSON export
│   ├── os               → File system operations
│   └── datetime         → Date/time handling
│       └── timedelta    → Date calculations
│
├── Third-Party UI
│   ├── ttkbootstrap     → Modern themed widgets
│   │   └── constants    → Style constants
│   └── tkinter          → Base GUI framework
│       ├── messagebox   → Dialogs
│       └── filedialog   → File selection
│
├── Data Processing
│   └── collections
│       └── defaultdict  → Category aggregation
│
└── Visualization
    ├── matplotlib.pyplot → Chart creation
    └── matplotlib.backends.backend_tkagg
        └── FigureCanvasTkAgg → Chart embedding
```

---

## 5. Event Flow

### User Action → System Response

```
┌─────────────────────────────────────────────────────────┐
│                   Event Handlers                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Button Click Events                                     │
│  ├── Add Expense Button                                 │
│  │   └── add_expense()                                  │
│  │       ├── Validate input                             │
│  │       ├── Write to CSV                               │
│  │       ├── Show success message                       │
│  │       ├── Clear fields                               │
│  │       ├── Refresh view                               │
│  │       └── Update statistics                          │
│  │                                                       │
│  ├── Edit Button                                        │
│  │   └── edit_expense()                                 │
│  │       ├── Get selected item                          │
│  │       ├── Load into fields                           │
│  │       ├── Remove old entry                           │
│  │       └── Show edit message                          │
│  │                                                       │
│  ├── Delete Button                                      │
│  │   └── delete_expense()                               │
│  │       ├── Get selected item                          │
│  │       ├── Show confirmation                          │
│  │       ├── Remove from CSV                            │
│  │       ├── Show success message                       │
│  │       ├── Refresh view                               │
│  │       └── Update statistics                          │
│  │                                                       │
│  ├── Clear Button                                       │
│  │   └── clear_fields()                                 │
│  │       └── Empty all input fields                     │
│  │                                                       │
│  ├── Export Button                                      │
│  │   └── export_expenses()                              │
│  │       ├── Show file dialog                           │
│  │       ├── Read CSV data                              │
│  │       ├── Convert format                             │
│  │       ├── Write to file                              │
│  │       └── Show success message                       │
│  │                                                       │
│  ├── View Charts Button                                 │
│  │   └── show_chart()                                   │
│  │       ├── Read CSV data                              │
│  │       ├── Aggregate by category                      │
│  │       ├── Create charts                              │
│  │       ├── Create window                              │
│  │       └── Display charts                             │
│  │                                                       │
│  └── Report Menu Items                                  │
│      └── generate_report(period)                        │
│          ├── Calculate date range                       │
│          ├── Filter expenses                            │
│          ├── Calculate total                            │
│          └── Show message                               │
│                                                          │
│  Keyboard Events                                         │
│  ├── Search Entry KeyRelease                            │
│  │   └── search_expenses()                              │
│  │       ├── Get search term                            │
│  │       ├── Filter expenses                            │
│  │       └── Update view                                │
│  │                                                       │
│  └── Filter Combobox Selection                          │
│      └── filter_by_category()                           │
│          ├── Get category                               │
│          ├── Filter expenses                            │
│          └── Update view                                │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 6. State Management

### Application State

```
┌─────────────────────────────────────────────────────────┐
│                  Global Variables                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Configuration                                           │
│  └── FILE_NAME = 'expenses.csv'                         │
│                                                          │
│  UI State Variables (StringVar)                         │
│  ├── category_var       → Current category input        │
│  ├── amount_var         → Current amount input          │
│  ├── description_var    → Current description input     │
│  ├── search_var         → Current search term           │
│  └── filter_var         → Current category filter       │
│                                                          │
│  UI Components (Widgets)                                 │
│  ├── root               → Main window                    │
│  ├── tree               → Expense list treeview          │
│  ├── total_label        → Total expenses display         │
│  ├── count_label        → Entry count display            │
│  └── category_count_label → Category count display      │
│                                                          │
└─────────────────────────────────────────────────────────┘

State Transitions:
1. Initial State → Empty fields, no data
2. Data Entry → Fields populated
3. After Add → Fields cleared, view updated
4. After Edit → Fields populated with selection
5. After Delete → Selection removed, view updated
6. During Search → View filtered
7. During Filter → View filtered by category
```

---

## 7. Error Handling Strategy

```
┌─────────────────────────────────────────────────────────┐
│                 Error Handling Layers                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Layer 1: Input Validation                              │
│  ├── Check for empty fields                             │
│  ├── Validate amount is numeric                         │
│  └── Show warning messagebox                            │
│                                                          │
│  Layer 2: File Operations                               │
│  ├── Try-except for file access                         │
│  ├── Handle FileNotFoundError                           │
│  ├── Handle PermissionError                             │
│  └── Show error messagebox                              │
│                                                          │
│  Layer 3: Data Processing                               │
│  ├── Try-except for CSV parsing                         │
│  ├── Handle malformed data                              │
│  ├── Skip invalid rows                                  │
│  └── Continue processing                                │
│                                                          │
│  Layer 4: User Confirmation                             │
│  ├── Confirm before delete                              │
│  ├── Allow cancel                                       │
│  └── Prevent accidental data loss                       │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 8. Performance Considerations

### Optimization Strategies

```
┌─────────────────────────────────────────────────────────┐
│              Performance Optimizations                   │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Data Loading                                            │
│  ├── Load only when needed                              │
│  ├── Cache in memory during session                     │
│  └── Incremental updates for add/delete                 │
│                                                          │
│  UI Updates                                              │
│  ├── Batch treeview updates                             │
│  ├── Lazy chart generation                              │
│  └── Debounced search (real-time)                       │
│                                                          │
│  File Operations                                         │
│  ├── Append for new entries                             │
│  ├── Full rewrite only for edit/delete                  │
│  └── Buffered I/O                                       │
│                                                          │
│  Memory Management                                       │
│  ├── Close file handles promptly                        │
│  ├── Clear chart figures after display                  │
│  └── Minimal global state                               │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 9. Security Considerations

```
┌─────────────────────────────────────────────────────────┐
│                Security Measures                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Data Protection                                         │
│  ├── Local storage only (no network)                    │
│  ├── User-controlled file location                      │
│  └── No sensitive data encryption (user responsibility) │
│                                                          │
│  Input Sanitization                                      │
│  ├── Type validation (amount must be numeric)           │
│  ├── Length limits (implicit)                           │
│  └── No SQL injection risk (CSV-based)                  │
│                                                          │
│  File System Safety                                      │
│  ├── Relative paths only                                │
│  ├── User-selected export paths                         │
│  └── No arbitrary code execution                        │
│                                                          │
│  User Confirmation                                       │
│  ├── Confirm destructive operations                     │
│  └── Clear error messages                               │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 10. Extensibility Points

### How to Extend the Application

```
┌─────────────────────────────────────────────────────────┐
│              Extension Opportunities                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  1. Add New Categories                                   │
│     └── Modify filter_combo['values'] list              │
│                                                          │
│  2. Change Theme                                         │
│     └── Modify tb.Window(themename="...")               │
│                                                          │
│  3. Add New Report Types                                 │
│     └── Add menu items to report_menu                    │
│     └── Extend generate_report() function               │
│                                                          │
│  4. Add New Export Formats                               │
│     └── Extend export_expenses() function               │
│     └── Add format handlers                             │
│                                                          │
│  5. Add Database Backend                                 │
│     └── Replace CSV functions with DB queries           │
│     └── Keep same function signatures                   │
│                                                          │
│  6. Add Budget Tracking                                  │
│     └── Add budget_var and budget functions             │
│     └── Add budget comparison in statistics             │
│                                                          │
│  7. Add Recurring Expenses                               │
│     └── Add recurrence field and scheduler              │
│     └── Auto-add on schedule                            │
│                                                          │
│  8. Add Multi-Currency                                   │
│     └── Add currency field                              │
│     └── Add conversion functions                        │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 11. Testing Strategy

### Recommended Test Cases

```
┌─────────────────────────────────────────────────────────┐
│                  Test Coverage                           │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Unit Tests                                              │
│  ├── test_add_expense()                                 │
│  ├── test_edit_expense()                                │
│  ├── test_delete_expense()                              │
│  ├── test_search_expenses()                             │
│  ├── test_filter_by_category()                          │
│  ├── test_update_statistics()                           │
│  ├── test_generate_report()                             │
│  └── test_export_expenses()                             │
│                                                          │
│  Integration Tests                                       │
│  ├── test_add_and_view()                                │
│  ├── test_edit_workflow()                               │
│  ├── test_delete_workflow()                             │
│  └── test_export_import()                               │
│                                                          │
│  UI Tests                                                │
│  ├── test_button_clicks()                               │
│  ├── test_search_input()                                │
│  ├── test_filter_selection()                            │
│  └── test_chart_display()                               │
│                                                          │
│  Edge Cases                                              │
│  ├── test_empty_file()                                  │
│  ├── test_corrupted_file()                              │
│  ├── test_invalid_input()                               │
│  ├── test_large_dataset()                               │
│  └── test_special_characters()                          │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 12. Deployment Architecture

```
┌─────────────────────────────────────────────────────────┐
│              Deployment Structure                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Application Files                                       │
│  ├── expenza.py      (Main application)          │
│  ├── requirements.txt        (Dependencies)             │
│  ├── README.md              (Documentation)             │
│  ├── USER_GUIDE.md          (User manual)               │
│  ├── QUICKSTART.md          (Quick guide)               │
│  ├── ARCHITECTURE.md        (This file)                 │
│  └── config_example.json    (Configuration template)    │
│                                                          │
│  Runtime Files (Generated)                              │
│  ├── expenses.csv           (Data storage)              │
│  └── __pycache__/           (Python cache)              │
│                                                          │
│  Optional                                                │
│  ├── screenshots/           (Application images)         │
│  ├── backups/              (Data backups)               │
│  └── exports/              (Exported files)             │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

<div align="center">

**Architecture Documentation**

*Expenza*

**Developer**: Aman Kanojiya

[Back to README](README.md)

</div>
