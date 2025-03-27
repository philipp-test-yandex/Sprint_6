import allure
import pytest
from conftest import driver
from page_objects.faq_page import FaqPage
from helpers.locators.locators_faq_page import (ACCORDION_QUESTION_COST, ANSWER_QUESTION_COST,
                                                ACCORDION_QUESTION_SEVERAL_SCOOTER, ANSWER_QUESTION_SEVERAL_SCOOTER,
                                                ACCORDION_QUESTION_RENTAL_TIME, ANSWER_QUESTION_RENTAL_TIME,
                                                ACCORDION_QUESTION_ORDER_TODAY, ANSWER_QUESTION_ORDER_TODAY,
                                                ACCORDION_QUESTION_EXTEND_OR_RETURN, ANSWER_QUESTION_EXTEND_OR_RETURN,
                                                ACCORDION_QUESTION_CHARGER_INCLUDED, ANSWER_QUESTION_CHARGER_INCLUDED,
                                                ACCORDION_QUESTION_CANCEL_ORDER, ANSWER_QUESTION_CANCEL_ORDER,
                                                ACCORDION_QUESTION_OUTSIDE_MKAD, ANSWER_QUESTION_OUTSIDE_MKAD)
from helpers.constants.constants_faq_page import (EXPECTED_RESULT_QUESTION_CANCEL_ORDER, EXPECTED_RESULT_QUESTION_OUTSIDE_MKAD,
                                                  EXPECTED_RESULT_QUESTION_COST, EXPECTED_RESULT_QUESTION_RENTAL_TIME,
                                                  EXPECTED_RESULT_QUESTION_ORDER_TODAY, EXPECTED_RESULT_QUESTION_CHARGER_INCLUDED,
                                                  EXPECTED_RESULT_QUESTION_EXTEND_OR_RETURN, EXPECTED_RESULT_QUESTION_SEVERAL_SCOOTERS)

faq_test_data = [(ACCORDION_QUESTION_COST, ANSWER_QUESTION_COST,EXPECTED_RESULT_QUESTION_COST),
                 (ACCORDION_QUESTION_SEVERAL_SCOOTER, ANSWER_QUESTION_SEVERAL_SCOOTER, EXPECTED_RESULT_QUESTION_SEVERAL_SCOOTERS),
                 (ACCORDION_QUESTION_RENTAL_TIME, ANSWER_QUESTION_RENTAL_TIME, EXPECTED_RESULT_QUESTION_RENTAL_TIME),
                 (ACCORDION_QUESTION_ORDER_TODAY, ANSWER_QUESTION_ORDER_TODAY, EXPECTED_RESULT_QUESTION_ORDER_TODAY),
                 (ACCORDION_QUESTION_EXTEND_OR_RETURN, ANSWER_QUESTION_EXTEND_OR_RETURN, EXPECTED_RESULT_QUESTION_EXTEND_OR_RETURN),
                 (ACCORDION_QUESTION_CHARGER_INCLUDED, ANSWER_QUESTION_CHARGER_INCLUDED, EXPECTED_RESULT_QUESTION_CHARGER_INCLUDED),
                 (ACCORDION_QUESTION_CANCEL_ORDER, ANSWER_QUESTION_CANCEL_ORDER, EXPECTED_RESULT_QUESTION_CANCEL_ORDER),
                 (ACCORDION_QUESTION_OUTSIDE_MKAD, ANSWER_QUESTION_OUTSIDE_MKAD, EXPECTED_RESULT_QUESTION_OUTSIDE_MKAD)
                 ]

faq_test_ids = [
    "accordion_with_question_cost",
    "accordion_with_question_several_scooters",
    "accordion_with_question_rental_time",
    "accordion_with_question_order_today",
    "accordion_with_question_extend_or_return",
    "accordion_with_question_charger_included",
    "accordion_with_question_cancel_order",
    "accordion_with_question_outside_mkad"
]

class TestFaqSection:
    @allure.title("Проверка FAQ — {id}")
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", faq_test_data, ids=faq_test_ids)
    @allure.step("Тест FAQ — проверяем вопрос из аккардиона и ответ")
    def test_faq_section(self, driver, question_locator, answer_locator, expected_text):
        faq_page = FaqPage(driver)
        faq_page.open_browser()
        faq_page.scroll_to_faq_section()

        faq_page.click_question(question_locator)
        faq_page.check_answer_text(answer_locator, expected_text)