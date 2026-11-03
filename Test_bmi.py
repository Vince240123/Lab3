import Lab2.bmi as bmi

def test_bmi_normal_weight():

    result = bmi.calculate_bmi(1.75, 70)
    test_arr = 0

    assert (result == test_arr)

def test_bmi_over_weight():

    result = bmi.calculate_bmi(1.75, 90)
    test_arr = 1
    
    assert (result == test_arr)

def test_bmi_under_weight():

    result = bmi.calculate_bmi(1.75, 50)
    test_arr = -1
    
    assert (result == test_arr)
