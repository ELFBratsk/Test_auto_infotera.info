

from pages.main_page import MainPage

link = "https://infotera.info/"


def test_checking_the_presence_of_buttons_on_the_main_page(browser):
    # заходим на страницу и проверяем основные 6 кнопок    
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_css_selector_infotera_info()  # проверяем что все кнопки на месте


# переходов по ссылкам (кнопкам)
# @pytest.mark.xfail()
def test_on_the_main_page_go_to_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_be_css_selector_infotera_info()  # работу кнопок с возвратом на начальную страницу


# проверка скроллинга

def test_main_page_scroll(browser):
    page = MainPage(browser, link)
    page.open()
    page.scroll_infotera_info()
