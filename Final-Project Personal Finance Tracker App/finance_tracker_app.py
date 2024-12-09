import os, json
from datetime import datetime

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

from input_validation import InputValidation


class FinanceTrackerApp():
    def __init__(self) -> None:
        self.data = pd.DataFrame()
        self.monthly_income = 0.0
        self.category_budget = dict()
    
    def import_csv(self) -> None:
        while True:
            file_name = InputValidation.str_input("Enter the file name to import (e.g., 'transactions.csv')")
            if '.csv' in file_name:
                file_name = file_name.replace('.csv', '')
            if not (os.path.exists(file_name + '.csv') or os.path.exists(file_name + '.json')):
                print('File not found')
                continue
            break
        
        # read transaction data
        if os.path.exists(file_name + '.csv'):
            self.data = pd.read_csv(file_name + '.csv')
            self.data['Date'] = pd.to_datetime(self.data['Date'])
        
        # read budget settings
        if os.path.exists(file_name + '.json'):
            with open(file_name + '.json', 'r') as f:
                json_data = json.load(f)
                self.monthly_income = json_data['monthly_income']
                self.category_budget = json_data['category_budget']
            
    def view_all_transactions(self) -> None:
        if not self.data.shape[0]:
            print('No transactions to display')
        else:
            print(self.data)
            
    def view_transactions_by_date(self) -> None:
        if not self.data.shape[0]:
            print('No transactions to display')
        else:
            start_date = InputValidation.date_input('Enter start date (YYYY-MM-DD)')
            end_date = InputValidation.date_input('Enter end date (YYYY-MM-DD)')
            print(f'\n--- Transactions from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')} ---')
            print(self.data[(self.data['Date'] >= start_date) & (self.data['Date'] <= end_date)])
            
    def add_transaction(self) -> None:
        date = InputValidation.date_input('Enter date')
        category = InputValidation.str_input('Enter category (e.g., Food, Rent, )').capitalize()
        description = InputValidation.str_input('Enter a description')
        amount = InputValidation.float_input('Enter the amount', accept_zero=False)
        _type = 'Expense'
        if category == 'Income':
            _type = 'Income'
        
        new_data = pd.DataFrame({
                'Date': date,
                'Category': category,
                'Description': description,
                'Amount': amount,
                'Type': _type
            }, 
            index=[len(self.data)]
            )
        self.data = pd.concat([self.data, new_data])
        
        print('Transaction added successfully!')
        
    def edit_transaction(self) -> None:
        if not self.data.shape[0]:
            print('No transactions to edit')
            return
        
        index = InputValidation.int_input('Enter the index of the transaction you want to edit')
        print('\nCurrent Transaction Details:')
        print(self.data.loc[index], '\n')
        
        date = InputValidation.date_input('Enter new date (YYYY-MM-DD) or press Enter to keep current', accept_none=True)
        category = InputValidation.str_input('Enter new category or press Enter to keep current', accept_none=True).capitalize()
        description = InputValidation.str_input('Enter new description or press Enter to keep current', accept_none=True)
        amount = InputValidation.float_input('Enter new amount or press Enter to keep current', accept_none=True)

        if date is None and category is None and description is None and amount is None:
            print('No changes made')
            return

        if date:
            self.data.at[index, 'Date'] = date
        if category:
            self.data.at[index, 'Category'] = category
        if description:
            self.data.at[index, 'Description'] = description
        if amount:
            self.data.at[index, 'Amount'] = amount
        
        print('\nTransaction updated successfully!')
    
    def delete_transaction(self) -> None:
        if not self.data.shape[0]:
            print('No transactions to delete')
            return
        
        index = InputValidation.int_input('Enter the index of the transaction you want to delete')
        self.data.drop(index, inplace=True)
        
        print('Transaction deleted successfully!')
    
    def analyze_spending_by_category(self) -> None:
        if not self.data.shape[0]:
            print('No transactions to analyze')
            return
        
        print('--- Total Spending by Category ---')
        print(self.data[self.data['Category']!='Income'].groupby('Category')['Amount'].sum())
    
    def calculate_average_monthly_spending(self) -> None:
        if not self.data.shape[0]:
            print('No transactions to analyze')
            return
        
        print('--- Average Monthly Spending ---')
        print(self.data.groupby(self.data['Date'].dt.to_period('M'))['Amount'].sum())
        
    
    def show_top_spending_category(self) -> None:
        if not self.data.shape[0]:
            print('No transactions to analyze')
            return
        
        print('--- Top Spending Category ---')
        top_spending = self.data[self.data['Category']!='Income'].groupby('Category')['Amount'].sum()
        print(f'{top_spending.idxmax()} with {top_spending.max()} total spending.')
        
    def set_monthly_income(self) -> None:
        self.monthly_income = InputValidation.float_input('Enter your monthly income', accept_zero=True)
        print(f'Your monthly income is set to: {self.monthly_income}')
    
    def set_category_budget(self) -> None:
        categories = np.array([])
        if self.data.shape[0]:
            categories = self.data[self.data['Category']!='Income']['Category'].unique()
            for category in categories:
                _budget = InputValidation.float_input(f'Enter your budget for {category}')
                self.category_budget[category] = _budget
        
        while True:
            _new_category = InputValidation.str_input(
                'If you want to add new category, type category name, Press Enter to Finish',
                accept_none=True
                )
            
            if not _new_category:
                break

            if _new_category in categories:
                print(f'{_new_category} is already exist!')
                continue
            
            self.category_budget[_new_category] = InputValidation.float_input(f'Enter your budget for {_new_category}')
            categories = np.append(categories, _new_category)
     
    def check_budget_status(self) -> None:
        if not self.category_budget:
            print("Budget hasn't been set.")
            return
        
        if not self.data.shape[0]:
            print('No transactions to analyze')
            return
        
        print('--- Budget Status ---')
        this_month = datetime.now().month
        this_year = datetime.now().year
        _filtered_data = self.data[
            (self.data['Type']=='Expense')
            & (self.data['Date'].dt.year==this_year)
            & (self.data['Date'].dt.month==this_month)
            ]
        if not _filtered_data.shape[0]:
            print('No transactions this month')
            return
        
        spent_amounts = _filtered_data.groupby('Category')['Amount'].sum()
        suggestions = list()
        no_warning = list()
        for category, budget in self.category_budget.items():
            if category not in spent_amounts:
                spent_amounts[category] = 0.0
            
            _text = str()
            if budget == spent_amounts[category]:
                _text = '(Warning: Finish budget!)'
                suggestions.append(f'Stop {category} spending to avoid exceeding the budget.')
            elif spent_amounts[category] > budget:
                _text = '(Alert: Exceeded budget!)'
                suggestions.append(f'Consider reducing {category} spending or adjusting the budget.')
            elif spent_amounts[category] > budget*0.8:
                _text = '(Warning: Close to budget!)'
                suggestions.append(f'Monitor {category} spending closely to avoid exceeding the budget.')
            else:
                no_warning.append(category)
            
            print(f'- {category}: ${spent_amounts.loc[category]} / ${budget} {_text}')
        
        print('\nSuggestions:')
        for suggestion in suggestions:
            print('-', suggestion)
            
        if len(no_warning) > 1:
            print('- You are within budget for other categories. Keep up the good work!')
        elif len(no_warning) == 1:
            print(f'- You are within budget for {no_warning[0]}. Keep up the good work!')
    
    def visualize_monthly_spending(self) -> None:
        if not self.data.shape[0]:
            print('No transactions to visualize')
            return
        
        # Line chart
        _income = self.data[self.data['Category']=='Income']
        _spending = self.data[self.data['Category']!='Income']
        
        monthly_income = _income.groupby(_income['Date'].dt.to_period('M'))['Amount'].sum()
        monthly_spending = _spending.groupby(_spending['Date'].dt.to_period('M'))['Amount'].sum()
        
        plt.figure(figsize=(12, 10))
        plt.subplot(2, 2, 1)
        plt.title('Monthly Income vs Spending')
        plt.plot(monthly_income.index.astype(str), monthly_income.values, label='Income', marker='o')
        plt.plot(monthly_spending.index.astype(str), monthly_spending.values, label='Spending', marker='o')
        plt.legend()
        
        if self.category_budget:
            this_month = datetime.now().month
            this_year = datetime.now().year
            filtered_data = self.data[
                (self.data['Type']=='Expense')
                & (self.data['Date'].dt.year==this_year)
                & (self.data['Date'].dt.month==this_month)
                ]
            
            if filtered_data.shape[0]:
                # Bar chart
                expense_data_by_category = filtered_data.groupby('Category')['Amount'].sum()
                category_budget = pd.DataFrame(
                    list(self.category_budget.items()),
                    columns=['Category', 'Amount']
                    ).groupby('Category')['Amount'].sum()
                
                concat_data = pd.concat([category_budget, expense_data_by_category], axis=1)
                concat_data.columns = ['Budget', 'Spending']
                concat_data.plot(kind='bar', title='Budget vs Spending by Category', ax=plt.subplot(2, 2, 2))
        
                # Pie chart
                print(expense_data_by_category)
                expense_data_by_category.plot(kind='pie', title='Spending by Category', ax=plt.subplot(2, 2, 3))
                
        plt.tight_layout()
        plt.show()
    
    def save_transactions(self) -> None:
        file_name = InputValidation.str_input("Enter the file name to save (e.g., 'transactions.csv')")
        if '.csv' in file_name:
            file_name = file_name.replace('.csv', '')
        
        if self.data.shape[0]:
            self.data.to_csv(file_name + '.csv')
        
        if self.monthly_income or self.category_budget:
            with open(file_name + '.json', 'w') as f:
                json.dump({
                    'monthly_income': self.monthly_income,
                    'category_budget': self.category_budget
                    }, f)
        
        print(f'\nTransactions saved to {file_name} successfully!')
    
    def run(self) -> None:
        while True:
            print('\n=== Personal Finance Tracker ===')
            print('0. Import a CSV file')
            print('1. View all transactions')
            print('2. View transactions by date')
            print('3. Add a transaction')
            print('4. Edit a transaction')
            print('5. Delete a transaction')
            print('6. Analyze spending by category')
            print('7. Calculate average monthly spending')
            print('8. Show top spending category')
            print('9. Set monthly income')
            print('10. Set category budget')
            print('11. Check budget status')
            print('12. Visualize monthly spending')
            print('13. Save transactions')
            print('14. Exit')
            
            match InputValidation.int_input('Choose an option (0-14)', accept_zero=True):
                case 0:
                    self.import_csv()
                case 1:
                    self.view_all_transactions()
                case 2:
                    self.view_transactions_by_date()
                case 3:
                    self.add_transaction()
                case 4:
                    self.edit_transaction()
                case 5:
                    self.delete_transaction()
                case 6:
                    self.analyze_spending_by_category()
                case 7:
                    self.calculate_average_monthly_spending()
                case 8:
                    self.show_top_spending_category()
                case 9:
                    self.set_monthly_income()
                case 10:
                    self.set_category_budget()
                case 11:
                    self.check_budget_status()                                                                                                                                              
                case 12:
                    self.visualize_monthly_spending()
                case 13:
                    self.save_transactions()
                case 14:
                    print('Exiting the Personal Finance Tracker. Goodbye!')
                    break
                case _:
                    print('Invalid choice')
                    

def main() -> None:
    app = FinanceTrackerApp()
    app.run()
    
if __name__ == '__main__':
    main()
