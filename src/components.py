from src.component_class import Component

class Bell(Component):
    def __init__(self, state, max_uses):
        super().__init__(state, max_uses)
        
    def ring_bell(self):
        if self.current_state > 0:
            print('Ring! Ring!')
            self.current_state -= 2
            return 'Ring! Ring!'
        else:
            print('This bell is broken and cannot be used')
            return 'This bell is broken and cannot be used'

class Brakes(Component):
    def __init__(self, state, max_uses):
        super().__init__(state, max_uses)
    
    def press_brakes(self):
        if self.current_state > 0:
            print('Squeak!')
            self.current_state -= 3
            return 'Squeak!'
        else:
            print("The brakes are broken and won't work")
            return "The brakes are broken and won't work"