import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.constants.constans_base import BASE_URL
from helpers.locators.locators_faq_page import FAQ_SECTION



class FaqPage:
    def __init__(self, driver, timeout=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открываем главную страницу")
    def open_browser(self):
        self.driver.get(BASE_URL)

    @allure.step("Скроллим до секции FAQ")
    def scroll_to_faq_section(self):
        element = self.wait.until(EC.visibility_of_element_located(FAQ_SECTION))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликаем по вопросу: {question_locator}")
    def click_question(self, question_locator):
        self.wait.until(EC.element_to_be_clickable(question_locator)).click()

    @allure.step("Проверяем ответ для {answer_locator}, ожидаемый текст: '{expected_text}'")
    def check_answer_text(self, answer_locator, expected_text):
        actual_text = self.wait.until(EC.visibility_of_element_located(answer_locator)).text
        assert actual_text == expected_text

