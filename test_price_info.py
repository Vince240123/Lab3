import price_info 

def test_total_cost_shopping():

    result = price_info.total_cost_shopping()
    expected = 46.75
    assert result == expected

def test_cost_fruits():

    result = price_info.cost_of_fruits('apple', 10)
    expected = 12.0
    assert result == expected

    


