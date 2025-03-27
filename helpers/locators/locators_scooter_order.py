from selenium.webdriver.common.by import By

BUTTON_ORDER_UP = (By.CLASS_NAME, 'Button_Button__ra12g')
BUTTON_ORDER_DOWN = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM')

NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
SURNAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
STATION_FIELD = (By.CSS_SELECTOR, 'input.select-search__input[placeholder="* Станция метро"]')
STATION_SUGGESTION = (By.CSS_SELECTOR, '.select-search__option')
NEXT_BUTTON = (By.CSS_SELECTOR, 'button.Button_Middle__1CSJM')

WHAT_TIME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
TIME_RENT_FIELD = (By.CSS_SELECTOR, '.Dropdown-root .Dropdown-control')
TIME_RENT_OPTION = "//div[contains(@class,'Dropdown-menu')]//div[normalize-space()='{0}']"
COLOR_BLACK = (By.ID, "black")
COLOR_GREY  = (By.ID, "grey")
COMMENT_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')

ORDER_CONFIRM_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM:not(.Button_Inverted__3IF-i)")
BUTTON_YES_CONFIRM_ORDER = (By.XPATH, "//button[normalize-space()='Да']")

ORDER_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
ORDER_MODAL_HEADER = (By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ")

LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")

ORDER_MODAL_TEXT = (By.CSS_SELECTOR, ".Order_Text__2broi")
ORDER_STATUS_BUTTON = (By.XPATH, "//button[normalize-space()='Посмотреть статус']")

LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")






