import allure
from page_objects.base_page import BasePage
from helpers.constants.constans_base import BASE_URL
from helpers.locators.locators_faq_page import FAQ_SECTION

class FaqPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open_browser(self):
        self.open(BASE_URL)

    @allure.step("Скрол к разделу FAQ")
    def scroll_to_faq_section(self):
        self.scroll_to_element(FAQ_SECTION)

    @allure.step("Кликаем по вопросу в FAQ")
    def click_question(self, question_locator):
        self.click(question_locator)

    @allure.step("Проверяем текст ответа")
    def check_answer_text(self, answer_locator, expected_text):
        actual_text = self.get_text(answer_locator)
        assert actual_text == expected_text




