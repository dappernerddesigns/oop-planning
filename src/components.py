from src.component_class import Component

class Bell(Component):
    def __init__(self, state, max_uses):
        super().__init__(state, max_uses)
        
    def ring_bell(self):
        return 'Ring! Ring!'