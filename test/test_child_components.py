from src.components import Bell

def test_Bell_has_a_ring_bell_method_that_returns_a_string():
    new_bell = Bell(100, 4)
    assert new_bell.ring_bell() == 'Ring! Ring!'