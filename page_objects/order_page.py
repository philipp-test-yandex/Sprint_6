import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.constants.constans_base import BASE_URL
from helpers.locators.locators_scooter_order import NAME_FIELD, SURNAME_FIELD, ADDRESS_FIELD, STATION_FIELD, PHONE_NUMBER_FIELD, STATION_SUGGESTION, NEXT_BUTTON, WHAT_TIME_FIELD, TIME_RENT_FIELD, TIME_RENT_OPTION, COMMENT_FIELD,BUTTON_YES_CONFIRM_ORDER, ORDER_CONFIRM_BUTTON, ORDER_MODAL_HEADER, ORDER_MODAL_TEXT, ORDER_STATUS_BUTTON, LOGO_SCOOTER, LOGO_YANDEX

class ScooterOrder:
    def __init__(self, driver, timeout=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открываем главную страницу Scooter")
    def open_browser(self):
        self.driver.get(BASE_URL)

    @allure.step("Нажимаем кнопку заказа (locator: {order_button})")
    def click_button_order_scooter(self, order_button):
        element = self.wait.until(EC.visibility_of_element_located(order_button))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(EC.visibility_of(element))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполняем форму заказчика: {name} {surname}, {address}, {station}, {phone}")
    def filling_form_fields(self, name, surname, address, station, phone):
        self.wait.until(EC.visibility_of_element_located(NAME_FIELD)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(SURNAME_FIELD)).send_keys(surname)
        self.wait.until(EC.visibility_of_element_located(ADDRESS_FIELD)).send_keys(address)

        self.wait.until(EC.element_to_be_clickable(STATION_FIELD)).send_keys(station)
        self.wait.until(EC.element_to_be_clickable(STATION_SUGGESTION)).click()

        self.wait.until(EC.visibility_of_element_located(PHONE_NUMBER_FIELD)).send_keys(phone)

        self.wait.until(EC.element_to_be_clickable(NEXT_BUTTON)).click()

    @allure.step("Указываем детали аренды: date={what_time}, term={rent_time}, color={scooter_colour}, comment={comment}")
    def about_rent(self, what_time, rent_time, scooter_colour, comment):
        self.wait.until(EC.element_to_be_clickable(WHAT_TIME_FIELD)).send_keys(what_time)
        self.driver.find_element(By.TAG_NAME, "body").click()
        self.wait.until(EC.element_to_be_clickable(TIME_RENT_FIELD)).click()

        rent_option = (By.XPATH, TIME_RENT_OPTION.format(rent_time))
        self.wait.until(EC.element_to_be_clickable(rent_option)).click()

        self.wait.until(EC.element_to_be_clickable(scooter_colour)).click()

        self.wait.until(EC.visibility_of_element_located(COMMENT_FIELD)).send_keys(comment)

        self.wait.until(EC.element_to_be_clickable(ORDER_CONFIRM_BUTTON)).click()

    @allure.step("Подтверждаем заказ в модальном окне")
    def confirm_yes_in_modal_window(self):
        self.wait.until(EC.visibility_of_element_located(ORDER_MODAL_HEADER))
        self.wait.until(EC.element_to_be_clickable(BUTTON_YES_CONFIRM_ORDER)).click()

    @allure.step("Проверяем что  заказ оформлен")
    def check_confirm_modal_window(self):
        header = self.wait.until(EC.visibility_of_element_located(ORDER_MODAL_HEADER)).text
        assert "Заказ оформлен" in header, f"Ожидался заголовок «Заказ оформлен», но получили: {header}"
        time.sleep(1)

    @allure.step("Кликаем по кнопке 'Статус заказа'")
    def view_status_order(self):
        self.wait.until(EC.visibility_of_element_located(ORDER_STATUS_BUTTON)).click()

    @allure.step("Проверяем переход на главную через логотип Самокат")
    def check_logo_scooter(self):
        self.wait.until(EC.element_to_be_clickable(LOGO_SCOOTER)).click()
        self.wait.until(lambda d: d.current_url == BASE_URL)
        assert self.driver.current_url == BASE_URL

    @allure.step("Проверяем редирект на Яндекс.Дзен через логотип Yandex")
    def check_logo_yandex(self):
        self.wait.until(EC.element_to_be_clickable(LOGO_YANDEX)).click()

        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru/?yredirect=true"))
        assert "dzen.ru" in self.driver.current_url