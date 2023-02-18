from src.components import *

def test_Bell_has_a_ring_bell_method_that_returns_a_string():
    new_bell = Bell(100, 4)
    assert new_bell.ring_bell() == 'Ring! Ring!'

def test_Bell_ring_method_reduces_component_state():
    new_bell = Bell(100, 4)
    new_bell.ring_bell()
    assert new_bell.current_state == 98

def test_If_bell_state_is_broken_does_not_reduce_state_and_returns_a_string():
    new_bell = Bell(0, 3)
    assert new_bell.ring_bell() == 'This bell is broken and cannot be used'
    assert new_bell.current_state == 0

def test_brakes_have_a_use_brakes_method_that_returns_a_string():
    brakes = Brakes(100, 2)
    assert brakes.press_brakes() == 'Squeak!'

