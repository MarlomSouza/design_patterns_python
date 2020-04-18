from Strategy.After.order import Order
from Strategy.After.postal_strategy import PostalStrategy
from Strategy.After.shipping_cost import ShippingCost


def test_should_ship_postal():
    expected_cost = 5.00
    order = Order()
    strategy = PostalStrategy()
    shipping_cost = ShippingCost(strategy)

    cost = shipping_cost.calculate(order)

    assert expected_cost == cost
