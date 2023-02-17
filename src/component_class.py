class Component:
    def __init__(self, state, max_uses):
        self.current_state = state
        self.max_lifespan = max_uses
    
    
    def check_condition(self):
        if self.current_state > 90:
            return 'Pristine'
        if self.current_state < 89 and self.current_state > 70:
            return 'Good'
        if self.current_state < 69 and self.current_state > 30:
            return 'OK'
        if self.current_state < 29 and self.current_state > 0:
            return 'Fragile'
        else:
            return 'Broken'