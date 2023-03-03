from selenium.webdriver.common.by import By


class Locator(object):

    @staticmethod
    def byId(element):
        return (By.ID, element)

    @staticmethod
    def byName(element):
        return (By.NAME, element)

    @staticmethod
    def byXPath(element):
        return (By.XPATH, element)

    @staticmethod
    def byLinkText(element):
        return (By.LINK_TEXT, element)

    @staticmethod
    def byPartialLinkText(element):
        return (By.PARTIAL_LINK_TEXT, element)

    @staticmethod
    def byTagName(element):
        return (By.TAG_NAME, element)

    @staticmethod
    def byClassName(element):
        return (By.CLASS_NAME, element)

    @staticmethod
    def byCssSelector(element):
        return (By.CSS_SELECTOR, element)

    def selectTypeLocator(context, selector, element):
        if selector == 'id':
            return Locator.byId(element)
        if selector == 'name':
            return Locator.byName(element)
        if selector == 'xpath':
            return Locator.byXPath(element)
        if selector == 'class_name':
            return Locator.byClassName(element)
        if selector == 'css':
            return Locator.byCssSelector(element)
        if selector == 'tag_name':
            return Locator.byTagName(element)
        if selector == 'partial_linkText':
            return Locator.byPartialLinkText(element)
        if selector == 'link_text':
            return Locator.byLinkText(element)

    @staticmethod
    def byBy(self, selector):
        if selector == 'id':
            return By.ID
        if selector == 'name':
            return By.NAME
        if selector == 'xpath':
            return By.XPATH
        if selector == 'class_name':
            return By.CLASS_NAME
        if selector == 'css':
            return By.CSS_SELECTOR
        if selector == 'tag_name':
            return By.TAG_NAME
        if selector == 'partial_linkText':
            return By.PARTIAL_LINK_TEXT
        if selector == 'link_text':
            return By.LINK_TEXT
