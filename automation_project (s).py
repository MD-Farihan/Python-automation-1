"""
Enhanced Python Automation Project with Data Analysis
Uses pandas and numpy for powerful automation and reporting
"""

import os
import shutil
from datetime import datetime, timedelta
import time
import pandas as pd
import numpy as np
from pathlib import Path

# ==========================================
# PART 1: SMART FILE ORGANIZER WITH REPORTS
# ==========================================

def organize_and_analyze_files():
    """
    Organizes files AND creates a detailed Excel report
    """
    
    home = os.path.expanduser("~")
    downloads_folder = os.path.join(home, "Downloads")
    
    if not os.path.exists(downloads_folder):
        print("Downloads folder not found!")
        return
    
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Music': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.7z']
    }
    
    # Collect file information in a list
    file_data = []
    
    print("Analyzing files in Downloads...")
    
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        
        if os.path.isfile(file_path):
            # Get file details
            file_size = os.path.getsize(file_path)  # in bytes
            file_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
            file_extension = os.path.splitext(filename)[1].lower()
            
            # Determine category
            category = 'Other'
            for cat, extensions in file_types.items():
                if file_extension in extensions:
                    category = cat
                    break
            
            # Add to our data list
            file_data.append({
                'Filename': filename,
                'Category': category,
                'Size (MB)': round(file_size / (1024*1024), 2),
                'Extension': file_extension,
                'Modified Date': file_modified,
                'Age (Days)': (datetime.now() - file_modified).days
            })
    
    # Create pandas DataFrame
    df = pd.DataFrame(file_data)
    
    if df.empty:
        print("No files found!")
        return
    
    # Display statistics
    print("\n" + "="*60)
    print("FILE ANALYSIS REPORT")
    print("="*60)
    
    print(f"\nTotal Files: {len(df)}")
    print(f"Total Size: {df['Size (MB)'].sum():.2f} MB")
    
    print("\n--- Files by Category ---")
    category_summary = df.groupby('Category').agg({
        'Filename': 'count',
        'Size (MB)': 'sum'
    }).rename(columns={'Filename': 'Count'})
    print(category_summary)
    
    print("\n--- Largest Files ---")
    print(df.nlargest(5, 'Size (MB)')[['Filename', 'Size (MB)', 'Category']])
    
    print("\n--- Oldest Files ---")
    print(df.nlargest(5, 'Age (Days)')[['Filename', 'Age (Days)', 'Category']])
    
    # Save report to Excel
    report_name = f"file_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    report_path = os.path.join(downloads_folder, report_name)
    
    with pd.ExcelWriter(report_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='All Files', index=False)
        category_summary.to_excel(writer, sheet_name='Summary')
    
    print(f"\nDetailed report saved: {report_name}")
    
    # Now organize files
    organize_choice = input("\nDo you want to organize these files into folders? (yes/no): ")
    
    if organize_choice.lower() == 'yes':
        files_moved = 0
        for _, row in df.iterrows():
            if row['Category'] != 'Other':
                old_path = os.path.join(downloads_folder, row['Filename'])
                
                # Create category folder
                category_folder = os.path.join(downloads_folder, row['Category'])
                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)
                
                # Move file
                new_path = os.path.join(category_folder, row['Filename'])
                if os.path.exists(old_path) and not os.path.exists(new_path):
                    shutil.move(old_path, new_path)
                    files_moved += 1
        
        print(f"\nOrganized {files_moved} files!")


# ==========================================
# PART 2: EXPENSE TRACKER AUTOMATION
# ==========================================

def create_expense_tracker():
    """
    Creates and manages a simple expense tracker with automatic calculations
    """
    
    print("\n--- Expense Tracker ---")
    
    # Sample data or load existing
    expenses_file = "expenses.csv"
    
    if os.path.exists(expenses_file):
        df = pd.read_csv(expenses_file)
        print(f"Loaded {len(df)} existing expenses.")
    else:
        df = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount'])
        print("Created new expense tracker.")
    
    while True:
        print("\n1. Add expense")
        print("2. View summary")
        print("3. View monthly report")
        print("4. Export to Excel")
        print("5. Back to main menu")
        
        choice = input("\nChoice: ")
        
        if choice == '1':
            # Add new expense
            date = input("Date (YYYY-MM-DD) or press Enter for today: ")
            if not date:
                date = datetime.now().strftime('%Y-%m-%d')
            
            category = input("Category (Food/Transport/Bills/Shopping/Other): ")
            description = input("Description: ")
            amount = float(input("Amount: $"))
            
            new_expense = pd.DataFrame([{
                'Date': date,
                'Category': category,
                'Description': description,
                'Amount': amount
            }])
            
            df = pd.concat([df, new_expense], ignore_index=True)
            df.to_csv(expenses_file, index=False)
            print("✓ Expense added!")
        
        elif choice == '2':
            if df.empty:
                print("No expenses yet!")
                continue
            
            print("\n--- Expense Summary ---")
            print(f"Total Expenses: ${df['Amount'].sum():.2f}")
            print(f"Average Expense: ${df['Amount'].mean():.2f}")
            print(f"Number of Transactions: {len(df)}")
            
            print("\n--- By Category ---")
            category_totals = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
            for cat, amount in category_totals.items():
                percentage = (amount / df['Amount'].sum()) * 100
                print(f"{cat}: ${amount:.2f} ({percentage:.1f}%)")
        
        elif choice == '3':
            if df.empty:
                print("No expenses yet!")
                continue
            
            df['Date'] = pd.to_datetime(df['Date'])
            df['Month'] = df['Date'].dt.to_period('M')
            
            print("\n--- Monthly Report ---")
            monthly = df.groupby('Month')['Amount'].sum()
            
            for month, total in monthly.items():
                print(f"{month}: ${total:.2f}")
            
            # Calculate trend using numpy
            if len(monthly) >= 2:
                trend = np.polyfit(range(len(monthly)), monthly.values, 1)[0]
                if trend > 0:
                    print(f"\n📈 Spending is increasing by ${trend:.2f}/month")
                else:
                    print(f"\n📉 Spending is decreasing by ${abs(trend):.2f}/month")
        
        elif choice == '4':
            excel_name = f"expenses_report_{datetime.now().strftime('%Y%m%d')}.xlsx"
            
            with pd.ExcelWriter(excel_name, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='All Expenses', index=False)
                
                # Category summary
                category_summary = df.groupby('Category')['Amount'].agg(['sum', 'count', 'mean'])
                category_summary.to_excel(writer, sheet_name='Category Summary')
            
            print(f"✓ Exported to {excel_name}")
        
        elif choice == '5':
            break


# ==========================================
# PART 3: DUPLICATE FILE FINDER (Enhanced)
# ==========================================

def find_duplicates_advanced(folder_path):
    """
    Advanced duplicate finder using pandas for better analysis
    """
    
    if not os.path.exists(folder_path):
        print(f"Error: {folder_path} does not exist!")
        return
    
    print("Scanning for duplicates...")
    
    file_info = []
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            file_info.append({
                'Filename': filename,
                'Size (MB)': round(file_size / (1024*1024), 2),
                'Size (bytes)': file_size
            })
    
    df = pd.DataFrame(file_info)
    
    if df.empty:
        print("No files found!")
        return
    
    # Find duplicates by size
    duplicates = df[df.duplicated(subset=['Size (bytes)'], keep=False)]
    
    if duplicates.empty:
        print("No duplicate files found!")
    else:
        print(f"\nFound {len(duplicates)} potential duplicate files:")
        print(duplicates[['Filename', 'Size (MB)']].to_string(index=False))
        
        # Calculate wasted space
        duplicate_groups = duplicates.groupby('Size (bytes)')
        wasted_space = 0
        
        for size, group in duplicate_groups:
            if len(group) > 1:
                wasted_space += size * (len(group) - 1)
        
        print(f"\n💾 Wasted space: {wasted_space / (1024*1024):.2f} MB")


# ==========================================
# PART 4: FILE AGE ANALYZER
# ==========================================

def analyze_file_age(folder_path):
    """
    Analyze files by age and suggest cleanup
    """
    
    if not os.path.exists(folder_path):
        print(f"Error: {folder_path} does not exist!")
        return
    
    print("Analyzing file ages...")
    
    file_data = []
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            modified_time = os.path.getmtime(file_path)
            modified_date = datetime.fromtimestamp(modified_time)
            age_days = (datetime.now() - modified_date).days
            file_size = os.path.getsize(file_path)
            
            file_data.append({
                'Filename': filename,
                'Age (Days)': age_days,
                'Size (MB)': round(file_size / (1024*1024), 2),
                'Modified': modified_date.strftime('%Y-%m-%d')
            })
    
    df = pd.DataFrame(file_data)
    
    if df.empty:
        print("No files found!")
        return
    
    # Statistics using numpy
    print(f"\nTotal files: {len(df)}")
    print(f"Average age: {np.mean(df['Age (Days)']):.1f} days")
    print(f"Oldest file: {np.max(df['Age (Days)'])} days")
    print(f"Newest file: {np.min(df['Age (Days)'])} days")
    
    # Categorize by age
    df['Age Category'] = pd.cut(df['Age (Days)'], 
                                 bins=[0, 7, 30, 90, 365, np.inf],
                                 labels=['< 1 week', '1-4 weeks', '1-3 months', '3-12 months', '> 1 year'])
    
    print("\n--- Files by Age ---")
    age_summary = df.groupby('Age Category').agg({
        'Filename': 'count',
        'Size (MB)': 'sum'
    }).rename(columns={'Filename': 'Count'})
    print(age_summary)
    
    # Suggest cleanup
    old_files = df[df['Age (Days)'] > 90]
    if not old_files.empty:
        old_size = old_files['Size (MB)'].sum()
        print(f"\n💡 Suggestion: You have {len(old_files)} files older than 90 days")
        print(f"   Total size: {old_size:.2f} MB")
        print(f"   These could be archived or deleted to free up space.")


# ==========================================
# PART 5: BATCH FILE RENAMER (Enhanced)
# ==========================================

def smart_batch_rename(folder_path):
    """
    Smart file renaming with preview using pandas
    """
    
    if not os.path.exists(folder_path):
        print(f"Error: {folder_path} does not exist!")
        return
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    if not files:
        print("No files found!")
        return
    
    print(f"\nFound {len(files)} files.")
    print("\nRenaming options:")
    print("1. Add prefix to all files")
    print("2. Add suffix to all files")
    print("3. Replace text in filenames")
    print("4. Add sequential numbers")
    
    choice = input("\nChoice: ")
    
    df = pd.DataFrame({'Original': files})
    
    if choice == '1':
        prefix = input("Enter prefix: ")
        df['New Name'] = prefix + df['Original']
    
    elif choice == '2':
        suffix = input("Enter suffix (before extension): ")
        df['New Name'] = df['Original'].apply(lambda x: 
            os.path.splitext(x)[0] + suffix + os.path.splitext(x)[1])
    
    elif choice == '3':
        old_text = input("Text to replace: ")
        new_text = input("Replace with: ")
        df['New Name'] = df['Original'].str.replace(old_text, new_text)
    
    elif choice == '4':
        base_name = input("Enter base name: ")
        df['New Name'] = [f"{base_name}_{i+1:03d}{os.path.splitext(f)[1]}" 
                         for i, f in enumerate(files)]
    
    else:
        print("Invalid choice!")
        return
    
    # Show preview
    print("\n--- Preview (first 10) ---")
    print(df.head(10).to_string(index=False))
    
    confirm = input(f"\nRename {len(df)} files? (yes/no): ")
    
    if confirm.lower() == 'yes':
        for _, row in df.iterrows():
            old_path = os.path.join(folder_path, row['Original'])
            new_path = os.path.join(folder_path, row['New Name'])
            
            if not os.path.exists(new_path):
                os.rename(old_path, new_path)
        
        print(f"✓ Renamed {len(df)} files!")


# ==========================================
# MAIN MENU
# ==========================================

def show_menu():
    print("\n" + "="*60)
    print("     ENHANCED PYTHON AUTOMATION TOOL")
    print("     (with pandas & numpy)")
    print("="*60)
    print("1. Smart File Organizer (with Excel report)")
    print("2. Expense Tracker")
    print("3. Find Duplicate Files (Advanced)")
    print("4. Analyze File Ages")
    print("5. Smart Batch Rename")
    print("6. Exit")
    print("="*60)


def main():
    print("Welcome to Enhanced Python Automation!")
    print("This tool uses pandas and numpy for powerful automation.\n")
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            organize_and_analyze_files()
        
        elif choice == '2':
            create_expense_tracker()
        
        elif choice == '3':
            folder = input("Enter folder path: ")
            find_duplicates_advanced(folder)
        
        elif choice == '4':
            folder = input("Enter folder path: ")
            analyze_file_age(folder)
        
        elif choice == '5':
            folder = input("Enter folder path: ")
            smart_batch_rename(folder)
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
