from selenium.common.exceptions import NoSuchElementException # Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать: 
#from selenium.common.exceptions import NoAlertPresentException # в начале файла
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=7): # В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url) #Теперь добавим еще один метод open. Он должен открывать нужную страницу в браузере, используя метод get()
    
    # Теперь в этом же классе реализуем метод is_element_present, в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).     
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException): # except (имя исключения):
            return False
        return True
    
        
    # Можно добавить в BasePage абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    # Если же мы хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с функцией until_not, в зависимости от того, какой результат мы ожидаем: 
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
    
    # Проверка на присутствие кнопок (ссылок)
    def should_be_css_selector_infotera_info(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_COMPANY), "BUTTON_COMPANY is not presented,"
        assert self.is_element_present(*BasePageLocators.BUTTON_SERVICES), "BUTTON_SERVICES is not presented,"
        assert self.is_element_present(*BasePageLocators.BUTTON_EXPERIENCE), "BUTTON_EXPERIENCE is not presented,"
        assert self.is_element_present(*BasePageLocators.BUTTON_ADVANTAGES), "BUTTON_ADVANTAGES is not presented,"
        assert self.is_element_present(*BasePageLocators.BUTTON_CAREER), "BUTTON_CAREER is not presented,"
        assert self.is_element_present(*BasePageLocators.BUTTON_VACANCY), "BUTTON_VACANCY is not presented,"
        assert self.is_element_present(*BasePageLocators.BUTTON_CONTACT), "BUTTON_CONTACT is not presented,"
    
    # проверка перехода по страницам    
    def go_to_be_css_selector_infotera_info(self):
        delay = 1 # Задержка в секундах
        self.browser.find_element(*BasePageLocators.BUTTON_COMPANY).click() # перехода на страницу
        self.browser.back() # возврат на начальную страницу
        self.browser.find_element(*BasePageLocators.BUTTON_SERVICES).click()
        self.browser.back()
        self.browser.find_element(*BasePageLocators.BUTTON_EXPERIENCE).click()
        self.browser.back()
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll вниз
        time.sleep(delay) # Задержка для прокрутки
        self.browser.find_element(*BasePageLocators.BUTTON_ADVANTAGES).click()
        self.browser.back()
        self.browser.find_element(*BasePageLocators.BUTTON_CAREER).click()
        self.browser.back()
        self.browser.find_element(*BasePageLocators.BUTTON_VACANCY).click()
        self.browser.back()
        self.browser.find_element(*BasePageLocators.BUTTON_CONTACT).click()
        self.browser.back()
    
    # прокрутка вниз и на верх
    def scroll_infotera_info(self):
        delay = 1 # Задержка в секундах
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") # scroll вниз
        self.browser.find_element(*BasePageLocators.SCROLL_TOP).click() # подъем на верх
        time.sleep(delay)