import webview
class CalculatorAPI:
    def __init__(self):
        # storage for calculator state
        self.current_value = "0"    # what see user on screen
        self.stored_value = None    # save number for next operation
        self.operator = None        # current operator
        self.reset_next = False     # flag to reset current_value on next input

    # --- math functions ---
    def add(self, a, b): 
        return a + b
    
    def subtract(self, a, b): 
        return a - b
    
    def multiply(self, a, b): 
        return a * b
    def divide(self, a, b): 
        if b == 0:
            return "Error: Division by 0"
        else:
            return a / b

    # --- main function called from JS ---
    def button_pressed(self, char):
        # 1. if pressed "C" to clear everything
        if char == 'C':
            self.current_value = "0"
            self.stored_value = None
            self.operator = None
            return self.current_value

        # 2. if pressed number or dot
        if char in '0123456789.':
            if self.reset_next or self.current_value == "0":
                self.current_value = ""
                self.reset_next = False
            self.current_value += char
            return self.current_value

        # 3. if pressed operator
        if char in '+-*/':
            if self.stored_value is not None and self.operator and not self.reset_next:
                # if we already have a stored value and operator -> calculate result before storing new operator
                self.calculate_result()
            else:
                self.stored_value = float(self.current_value)
            
            self.operator = char
            self.reset_next = True
            return self.current_value

        # 4. if pressed "=" -> calculate result
        if char == '=':
            self.calculate_result()
            self.stored_value = None
            self.operator = None
            self.reset_next = True
            return self.current_value

        return self.current_value

    # --- function to calculate result based on stored value, current value and operator ---
    def calculate_result(self):
        if not self.operator or self.stored_value is None or not self.current_value:
            return

        a = self.stored_value
        try:
            b = float(self.current_value)
        except ValueError:
            return

        # call function based on operator
        if self.operator == '+': result = self.add(a, b)
        elif self.operator == '-': result = self.subtract(a, b)
        elif self.operator == '*': result = self.multiply(a, b)
        elif self.operator == '/': result = self.divide(a, b)

        # format result for better display
        if isinstance(result, str):
            self.current_value = result
        else:
            if result.is_integer():
                self.current_value = str(int(result)) # 5.0 -> 5
            else:
                self.current_value = str(result)
        
        # store result for next operation (if user continues without pressing "C")
        if not isinstance(result, str):
            self.stored_value = float(self.current_value)

if __name__ == '__main__':
    api = CalculatorAPI()
    webview.create_window(
        title='Calculus', 
        url='index.html', 
        js_api=api, 
        width=300, 
        height=450, 
        resizable=False
    )
    webview.start()