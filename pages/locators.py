from selenium.webdriver.common.by import By

# Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject: 
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # теперь каждый селектор — это пара: как искать и что искать.
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    ID_REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email") # Регистрация Адрес электронной почты
    ID_REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1") # Регистрация Пароль
    ID_REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2") # Регистрация Повторите пароль 
    REGISTER_FORM_BUTTON = (By.CSS_SELECTOR, "#register_form > button") # Регистрация button (click)
    
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button") # кнопка Добавить в корзину
    CONTENT_INNER = (By.CSS_SELECTOR, "#content_inner .product_main > h1") # Название книги
    BASKET_ITEMS = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong") # название в корзине
    MESSAGES_ITEMS = (By.CSS_SELECTOR, "#messages .alertinner > strong") # был добавлен в вашу корзину.
    PRICE_ITEMS = (By.CSS_SELECTOR, "#content_inner .product_main .price_color") # цена книги
    PRICE_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert .alertinner  > p > strong") # цена в корзине
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alert-success") # сообщение об успешном добавлении в корзину (по селектору их 3)

# В файле locators.py создаем новый класс BasePageLocators и переносим туда соответствующие элементы:

class BasePageLocators():
    BUTTON_COMPANY = (By.CSS_SELECTOR, 'div.features-section.pb-80 div >a[href^="?page=about"]') # кнопка - локатор О КОМПАНИИ
    BUTTON_SERVICES = (By.CSS_SELECTOR, 'div.features-section.pb-80 div >a[href^="?page=services"]') # кнопка - локатор УСЛУГИ
    BUTTON_EXPERIENCE = (By.CSS_SELECTOR, 'div.features-section.pb-80 div >a[href^="?page=experience"]') # кнопка - локатор ОПЫТ
    BUTTON_ADVANTAGES = (By.CSS_SELECTOR, 'div.features-section.pb-80 div >a[href^="?page=advantages"]') # кнопка - локатор НАШИ ПРЕИМУЩЕСТВА
    BUTTON_CAREER = (By.CSS_SELECTOR, 'div.features-section.pb-80 div >a[href="?page=career"]') # кнопка - локатор КАРЬЕРА У НАС
    BUTTON_VACANCY = (By.CSS_SELECTOR, 'div.features-section.pb-80 div >a[href="?page=vacancy"]') # кнопка - локатор ВАКАНСИИ
    SCROLL_TOP = (By.CSS_SELECTOR, '.scroll-top') # кнопка подъема на верх
    BUTTON_CONTACT = (By.CSS_SELECTOR, '.nav-link[href="?page=contact"]') # кнопка - локатор ВАКАНСИИ
    
    
# Локаторы BasketPageLocators для страницы корзины    
class BasketPageLocators():
    MESSAGES_ITEMS = (By.CSS_SELECTOR, "#messages .alertinner > strong") # Информация о товаре если в корзине присутствует товар.
    CONTENT_BASKET = (By.CSS_SELECTOR, "#content_inner > p > a") # Ваша корзина пуста
    