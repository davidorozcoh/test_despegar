from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *

from utils.locator import Locator
from utils.functions import *
from hamcrest import assert_that, equal_to
from selenium.webdriver.common.by import By


class Page(object):

    def __init__(self, context):
        self.browser = context.browser
        self.config = context.config
        self.timeout = 30

    def open(self, path):
        self.browser.get(path)

    def close(self):
        self.browser.quit()

    def update(self):
        self.browser.refresh()

    def set_atribute(self, action):
        setattr(self.browser, action[0], action[1])

    """ Find """

    def find(self, selector, element):
        self.selector = selector
        self.element = element
        try:
            if selector == 'id':
                return self.browser.find_element(By.ID, self.element)
            if selector == 'name':
                return self.browser.find_element(By.NAME, self.element)
            if selector == 'xpath':
                return self.browser.find_element(By.XPATH, self.element)
            if selector == 'class_name':
                return self.browser.find_element(By.CLASS_NAME, self.element)
            if selector == 'css':
                return self.browser.find_element(By.CSS_SELECTOR, self.element)
            if selector == 'tag_name':
                return self.browser.find_element(By.TAG_NAME, self.element)
            if selector == 'partial_linkText':
                return self.browser.find_element(By.PARTIAL_LINK_TEXT, self.element)
            if selector == 'link_text':
                return self.browser.find_element(By.LINK_TEXT, self.element)
        except NoSuchElementException as e:
            print('This Exception has occurred, ' + str(e))
            return e

    def findElements(self, selector, element):
        self.selector = selector
        self.element = element
        try:
            if selector == 'id':
                return self.browser.find_elements(By.ID, self.element)
            if selector == 'name':
                return self.browser.find_elements(By.NAME, self.element)
            if selector == 'xpath':
                return self.browser.find_elements(By.XPATH, self.element)
            if selector == 'class_name':
                return self.browser.find_elements(By.CLASS_NAME, self.element)
            if selector == 'css':
                return self.browser.find_elements(By.CSS_SELECTOR, self.element)
            if selector == 'tag_name':
                return self.browser.find_elements(By.TAG_NAME, self.element)
            if selector == 'partial_linkText':
                return self.browser.find_elements(By.PARTIAL_LINK_TEXT, self.element)
            if selector == 'link_text':
                return self.browser.find_elements(By.LINK_TEXT, self.element)
        except NoSuchElementException as e:
            print('This Exception has occurred, ' + str(e))
            return e

    ''' Get text '''

    def getText(self, selector, element):
        element = Page.find(self, selector, element)
        return element.text

    def getAttribute_text(self, selector, element):
        element = Page.find(self, selector, element)
        return element.get_attribute("text")

    def getAttribute(self, selector, element, attribute):
        element = Page.find(self, selector, element)
        return element.get_attribute(attribute)

    '''Click '''

    def click(self, selector, element):
        try:
            element = Page.find(self, selector, element)
            return element.click()
        except Exception as e:
            print('This Exception has occurred, ' + str(e))
            return e

    ''' Fill '''

    def fill(self, selector, element, text=''):
        element = Page.find(self, selector, element)
        return element.send_keys(text)

    def fill2(self, locator, text=''):
        element = self.browser.find_element(*locator)
        return element.send_keys(text)

    def fill_id(self, Id, text=''):
        return self.fill(Locator.byId(Id), text)

    def fill_name(self, name, text=''):
        return self.fill(Locator.byName(name), text)

    def fill_xpath(self, xpath, text=''):
        return self.fill(Locator.byXPath(xpath), text)

    def fill_class_name(self, name, text=''):
        return self.fill(Locator.byClassName(name), text)

    def fill_css(self, css, text=''):
        return self.fill(Locator.byCssSelector(css), text)

    '''Select'''

    def select(self, selector, element, text):
        element = Page(self).find(selector, element)
        select = Select(element)
        select.select_by_visible_text(text)

    ''' Shadow root '''

    def get_child_element_text(self, parent):
        shadow_root = self.browser.find_element_by_css_selector(parent)
        script = "return arguments[0].firstChild.shadowRoot"
        return self.execute_script_dom(script, shadow_root)

    def get_child_element_input(self, parent):
        shadow_root = self.browser.find_element_by_css_selector(parent)
        script = "return arguments[0].shadowRoot.querySelector('input')"
        return self.execute_script_dom(script, shadow_root)

    def fill_by_shadow_root(self, parent, value):
        element = self.get_child_element_input(parent)
        if self.config.userdata['browser'] == 'safari':
            self.put_value_script(element, value)
            self.focus_script(element)
        else:
            ActionChains(self.browser).click(element).send_keys(value).perform()
        return element

    '''Execute script'''

    def execute_script_dom(self, script, element):
        return self.browser.execute_script(script, element)

    def put_value_script(self, element, value):
        script = f""" arguments[0].value='{value}' """
        return self.execute_script_dom(script, element)

    def click_script(self, element):
        script = f""" arguments[0].click() """
        return self.execute_script_dom(script, element)

    def focus_script(self, element):
        script = f""" arguments[0].focus() """
        return self.execute_script_dom(script, element)

    def click_by_script(self, selector, element):
        web_element = Page(self).find(selector, element)
        return self.browser.execute_script("arguments[0].click();", web_element)

    def return_scroll_position_script(self):
        return self.browser.execute_script("return window.pageYOffset;")

    '''Action Chains'''

    def actions_click(self, element, selector):
        object = Page.find(self, element, selector)
        ActionChains(self.browser).click(object).perform()

    def actions_doubleclick(self, selector, element):
        web_element = Page.find(self, selector, element)
        ActionChains(self.browser).double_click(web_element).perform()

    def action_keydown(self, number):
        for elements in range(number):
            ActionChains(self.browser).send_keys(Keys.DOWN).perform()
        ActionChains(self.browser).send_keys(Keys.ENTER).perform()

    def action_enter(self):
        ActionChains(self.browser).send_keys(Keys.ENTER).perform()

    def action_tab(self):
        ActionChains(self.browser).send_keys(Keys.TAB).perform()

    def action_drag_and_drop(self, source, target):
        ActionChains(self.browser).drag_and_drop(target, source).perform()

    def action_slide_element(self, selector, element, x_offset):
        web_element = Page.find(self, selector, element)
        ActionChains(self.browser).click_and_hold(web_element).move_by_offset(int(x_offset), 0).release().perform()

    def action_slide_y_axis_element(self, selector, element, y_offset):
        web_element = Page.find(self, selector, element)
        ActionChains(self.browser).click_and_hold(web_element).move_by_offset(0, int(y_offset)).release().perform()

    '''Wait'''

    def wait(self, seconds):
        WebDriverWait(self.browser, seconds)

    def webdriver_wait(self, seconds):
        return WebDriverWait(self.browser, int(seconds))

    def wait_until_element_located(self, seconds, element):
        wait = self.browser.webdriver_wait(seconds)
        return wait.until(EC.presence_of_element_located(element))

    def wait_until_element_clickable(self, seconds, element):
        wait = self.browser.webdriver_wait(seconds)
        return wait.until(EC.element_to_be_clickable(element))

    def explicitWait(self, selector, element, time):
        self.selector = selector
        try:
            local_byBy = Locator.byBy(self, self.selector)
            WebDriverWait(self.browser, time).until(
                EC.presence_of_element_located((local_byBy, element))
            )
        except TimeoutException as e:
            print("TimeoutException, the element was not found: " + str(e))
            return e

    def fluent_wait(self, selector, element, timer=10):
        by_selector = Locator.byBy(self, selector)
        try:
            wait = WebDriverWait(self.browser, timer, poll_frequency=5,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
            wait.until(EC.element_to_be_clickable((by_selector, element)))
        except TimeoutException as e:
            print("TimeoutException, the element was not found: " + str(e))
            return e

    '''Select'''

    def fill2(self, selector, element, text):
        element = Page.find(self, selector, element)
        element.select_by_visible_text(text)
        return element

    def select_text(self, locator, text):
        select = Select(self.browser.find_element(*locator))
        select.select_by_visible_text(text)
        return select

    '''Attach'''

    def attach_file(self, locator, file_name=''):
        element = self.browser.find_element(*locator)
        element.send_keys(file_path(file_name))
        return element

    def select_value(self, locator, value):
        select = Select(self.browser.find_element(*locator))
        select.select_by_value(value)
        return select

    '''Clear'''

    def clear_txt2(self, selector, element):
        element = Page.find(self, selector, element)
        element.clear()

    def clear_txt(self, locator):
        a = self.browser.find_element(*locator)
        a.clear()

    '''Validations'''

    def verify_url(self, url):
        return self.browser.current_url == url

    def contain_in_url(self, path):
        currentUrl = str(self.browser.current_url)
        return path in currentUrl

    def get_actual_url(self):
        return str(self.browser.current_url)

    def is_visible(self, id):
        return self.browser.find_element_by_id(id).is_displayed()

    def is_element_visible_by_css(self, css):
        return self.browser.find_element_by_css_selector(css).is_displayed()

    def is_element_visible_by_xpath(self, xpath):
        return self.browser.find_element_by_xpath(xpath).is_displayed()

    def is_element_visible_by_id(self, id_):
        return self.browser.find_element_by_id(id_).is_displayed()

    def is_element_selected(self, selector, element):
        element = Page.find(self, selector, element)
        return element.is_selected()

    def is_disabled_example(self, id):
        return self.browser.find_element_by_id(id).get_attribute("disabled")

    def title_is(self, text):
        return EC.title_is(text)

    def should_have_content(self, content):
        has_content = False
        if self.browser.has_title(content):
            has_content = True
        if self.browser.has_text(content):
            has_content = True
        return has_content

    def get_element_value(self, element):
        return element.get_attribute('value')

    def assert_that_element_has_value(self, element, value):
        return assert_that(self.get_element_value(element), equal_to(value))

    def element_is_present(self, selector, element):
        return Page.find(self, selector, element).is_displayed()

    def is_disable(self, selector, element):
        return Page.find(self, selector, element).get_attribute('disabled')

    ''' Scroll '''

    def scroll_up(self):
        self.browser.execute_script("window.scrollTo(1000, 0)")

    def small_scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, 500)")

    def medium_scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, 650)")

    def variable_scroll_down(self, value):
        self.browser.execute_script(f"window.scrollTo(0, {value})")

    def smaller_scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, 400)")

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, 2000)")

    def scroll_horizontally_right_direction(self):
        return self.browser.execute_script("window.scrollTo(2000, 0)")

    def scroll_vertical_down(self):
        return self.browser.execute_script("window.scrollTo(500, 2000)")

    def scroll_horizontally_right_medium(self):
        return self.browser.execute_script("window.scrollTo(1000, 0)")

    def scroll_vertical_down_medium(self):
        return self.browser.execute_script("window.scrollTo(500, 1000)")

    ''' resize'''

    def resize(self):
        return self.browser.set_window_size(1920, 1080)

    '''alert'''

    def close_alert_and_get_its_text(self):
        try:
            alert = self.browser.switch_to_alert()
            print("Alert text:" + alert.text)
            alert.accept()
            print("Alert detected, accept it")
            return True
        except UnexpectedAlertPresentException:
            print("Hum... some was worng, this is a  continue?")
            return False
        except NoAlertPresentException:
            print("No alert here")
            return False

    def is_alert_present(self):
        try:
            self.browser.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True
