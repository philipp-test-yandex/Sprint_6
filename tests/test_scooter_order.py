import allure
from conftest import driver
import pytest
from page_objects.order_page import ScooterOrder
from helpers.locators.locators_scooter_order import BUTTON_ORDER_UP, BUTTON_ORDER_DOWN, COLOR_BLACK, COLOR_GREY

order_buttons = [BUTTON_ORDER_UP, BUTTON_ORDER_DOWN]
order_buttons_ids = ["BUTTON_ORDER_UP", "BUTTON_ORDER_DOWN"]

user_data = [
    ("Петя", "Тестов", "ул Марс", "Парк Победы", "+71111111111"),
    ("Маша", "Тестова", "ул Земля", "Сокольники", "80000000000")
            ]
user_ids = ["Petr", "Mary"]

rent_data = [
    ("25.03.2025", "сутки",  COLOR_BLACK, "тест цвет черный"),
    ("26.03.2025", "двое суток", COLOR_GREY, "тест цвет серый")]
rent_ids = ["Time Rent - one day; scooter - black ", "Time Rent - two day; Scooter - grey"]


class TestScooterOrder:
    @pytest.mark.parametrize("order_button", order_buttons, ids=order_buttons_ids)
    @pytest.mark.parametrize("name, surname, address, station, phone", user_data, ids=user_ids)
    @pytest.mark.parametrize("what_time, rent_time, scooter_colour, comment", rent_data, ids=rent_ids)
    @allure.title("Создание заказа — {name} {surname}, {rent_time}, {scooter_colour}")
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