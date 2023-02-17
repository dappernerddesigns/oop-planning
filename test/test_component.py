from component_class import Component

def test_component_should_have_current_state_property():
    part = Component(100, 20)
    assert part.current_state == 100

def test_component_should_have_max_use_property():
    part = Component(100, 5)
    assert part.max_lifespan == 5

    
def test_component_has_a_check_condition_method_that_returns_the_state_of_the_component():
    great_part = Component(100,12)
    good_part = Component(80,12)
    ok_part = Component(50,12)
    fragile_part = Component(10,12)
    broken_part = Component(0,2)
    
    assert great_part.check_condition() == 'Pristine'
    assert good_part.check_condition() == 'Good'
    assert ok_part.check_condition() == 'OK'
    assert fragile_part.check_condition() == 'Fragile'
    assert broken_part.check_condition() == 'Broken'