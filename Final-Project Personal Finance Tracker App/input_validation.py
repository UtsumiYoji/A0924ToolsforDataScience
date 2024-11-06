from datetime import datetime

class InputValidation:
    @classmethod
    def int_input(
        cls,
        text:str='Enter a number', 
        accept_zero=True, 
        accept_negative=False,
        accept_none=False
        ) -> int:
        
        while True:
            value = input(text + ': ')
            if not value.isnumeric():
                print('Invalid input')
                continue
        
            value = int(value)
            if value == 0 and not accept_zero:
                print('Cannot be zero')
                continue
            
            if value < 0 and not accept_negative:
                print('Cannot be negative')
                continue
            
            if value is None and not accept_none:
                print('Cannot be None')
                continue
            
            break
        
        return value
    
    @classmethod
    def float_input(
        cls,
        text:str='Enter a number',
        accept_zero=True,
        accept_negative=False,
        accept_none=False
        ) -> float:
        
        while True:
            value = input(text + ': ')
            
            if not value:
                if accept_none:
                    break
                else:
                    print('Cannot be None')
                    continue
            
            try:
                value = float(value)
            except ValueError:
                print('Invalid input')
                continue
        
            if value == 0 and not accept_zero:
                print('Cannot be zero')
                continue
            
            if value < 0 and not accept_negative:
                print('Cannot be negative')
                continue
            break
        
        return value
    
    @classmethod
    def str_input(
        cls, 
        text:str='Enter a string', 
        accept_none=False
        ) -> str:
        
        while True:
            value = input(text + ': ')
            
            if not value:
                if accept_none:
                    break
                else:
                    print('Cannot be empty')
                    continue
            break

        return value
    
    @classmethod
    def date_input(
        cls, 
        text:str='Enter a date (YYYY-MM-DD)', 
        accept_none=False
        ) -> datetime:
        
        while True:
            value = input(text + ': ')
            
            if not value:
                if accept_none:
                    break
                else:
                    print('Cannot be None')
                    continue
            
            try:
                value = datetime.strptime(value, '%Y-%m-%d')
                break
            except:
                print('Invalid date format')
                continue

        return value
