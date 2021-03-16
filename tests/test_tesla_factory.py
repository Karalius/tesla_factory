from tesla_factory import Tesla


def test_battery_charge():
    tesla = Tesla('S', 'red')
    assert tesla.battery_charge == 99.9


def test_autopilot():
    tesla = Tesla('S', 'red', True)
    result = tesla.autopilot('tree')
    assert result == "Tesla model S avoids tree"


def test_charge_battery():
    tesla = Tesla('S', 'red')
    tesla.charge_battery()
    assert tesla.battery_charge == 100
