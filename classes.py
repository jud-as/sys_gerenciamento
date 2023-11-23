
class SwitchCase:
    def __init__(self):
        self._cases = {}
        
    def add_case(self, case, function):
        """Adiciona um caso e a função correspondente"""
        self._cases[case] = function
    
    def execute(self, case):
        
        selected_function = self._cases.get(case)
        if selected_function:
            selected_function()
        
        
        