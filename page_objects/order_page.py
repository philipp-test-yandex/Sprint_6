import allure
from page_objects.base_page import BasePage
from helpers.constants.constans_base import BASE_URL
from helpers.locators.locators_scooter_order import *

class ScooterOrder(BasePage):

    @allure.step("Открываем страницу заказа")
    def open_browser(self):
        self.open(BASE_URL)

    @allure.step("Кликаем по кнопке Заказать")
    def click_button_order_scooter(self, order_button):
        self.scroll_to_element(order_button)
        self.click_js(order_button)

    @allure.step("Заполняем форму заказа")
    def filling_form_fields(self, name, surname, address, station, phone):
        self.wait_and_send_keys(NAME_FIELD, name)
        self.wait_and_send_keys(SURNAME_FIELD, surname)
        self.wait_and_send_keys(ADDRESS_FIELD, address)
        self.wait_and_send_keys(STATION_FIELD, station)
        self.click(STATION_SUGGESTION)
        self.wait_and_send_keys(PHONE_NUMBER_FIELD, phone)
        self.click(NEXT_BUTTON)

    @allure.step("Заполняем данные аренды")
    def about_rent(self, what_time, rent_time, scooter_colour, comment):
        self.wait_and_send_keys(WHAT_TIME_FIELD, what_time)
        self.driver.find_element(By.TAG_NAME, "body").click()  # клик вне поля
        self.click(TIME_RENT_FIELD)

        rent_option = (By.XPATH, TIME_RENT_OPTION.format(rent_time))
        self.click(rent_option)

        self.click(scooter_colour)
        self.wait_and_send_keys(COMMENT_FIELD, comment)
        self.click(ORDER_CONFIRM_BUTTON)

    @allure.step("Подтверждаем заказ")
    def confirm_yes_in_modal_window(self):
        self.wait_for_visibility(ORDER_MODAL_HEADER)
        self.click(BUTTON_YES_CONFIRM_ORDER)

    @allure.step("Проверяем, что заказ оформлен")
    def check_confirm_modal_window(self):
        header = self.get_text(ORDER_MODAL_HEADER)
        assert "Заказ оформлен" in header

    @allure.step("Открываем статус заказа")
    def view_status_order(self):
        self.click(ORDER_STATUS_BUTTON)

    @allure.step("Переход по логотипу Самоката")
    def check_logo_scooter(self):
        self.click(LOGO_SCOOTER)
        self.wait.until(lambda d: d.current_url == BASE_URL)
        assert self.driver.current_url == BASE_URL

    @allure.step("Проверяем редирект на Яндекс.Дзен через логотип Yandex")
    def check_logo_yandex(self):
        self.click(LOGO_YANDEX)
        self.switch_to_new_tab()
        self.wait_for_url_contains("dzen.ru")
        assert "dzen.ru" in self.driver.current_url

