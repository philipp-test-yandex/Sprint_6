import allure
import pytest
from conftest import driver
from page_objects.order_page import ScooterOrder
from helpers.locators.locators_scooter_order import BUTTON_ORDER_UP, BUTTON_ORDER_DOWN, COLOR_BLACK, COLOR_GREY

order_buttons = [
    pytest.param(BUTTON_ORDER_UP, id="Button UP "),
    pytest.param(BUTTON_ORDER_DOWN, id="Button DOWN")
]

user_data = [
    pytest.param("Петя", "Тестов", "ул Марс", "Парк Победы", "+71111111111", id="Pety"),
    pytest.param("Маша", "Тестова", "ул Земля", "Сокольники", "80000000000", id="Mary")
]

rent_data = [
    pytest.param("25.03.2025", "сутки", COLOR_BLACK, "цвет черный", id="Colour Black; Rent Time 1 Day"),
    pytest.param("26.03.2025", "двое суток", COLOR_GREY, "цвет серый", id="Colour Grey; Rent Time 2 Day")
]

class TestScooterOrder:
    @pytest.mark.parametrize("order_button", order_buttons)
    @pytest.mark.parametrize("name, surname, address, station, phone", user_data)
    @pytest.mark.parametrize("what_time, rent_time, scooter_colour, comment", rent_data)
    def test_order_button_click(self, driver, order_button, name, surname, address, station, phone, what_time, rent_time, scooter_colour, comment):
        scooter_order = ScooterOrder(driver)

        scooter_order.open_browser()
        scooter_order.click_button_order_scooter(order_button)
        scooter_order.filling_form_fields(name, surname, address, station, phone)
        scooter_order.about_rent(what_time, rent_time, scooter_colour, comment)
        scooter_order.confirm_yes_in_modal_window()
        scooter_order.check_confirm_modal_window()
        scooter_order.view_status_order()
        scooter_order.check_logo_scooter()
        scooter_order.check_logo_yandex()
