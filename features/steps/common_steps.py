from behave import step
from hamcrest import *
import time
from utils.data_objects import *
from utils.page import Page


@step("The user is on the {page} Page")
def web_site(context, page):
    context.section = page
    Page(context).open(dataElements[context.section]['url'])


@step("The user writes {input} as {destination}")
def write_box(context, input, destination):
    selector = dataElements[context.section][destination]['selector']
    element = dataElements[context.section][destination][selector]
    Page(context).explicitWait(selector, element, 6)
    Page(context).fill(selector, element, input)
    time.sleep(3)
    Page(context).action_enter()


@step('The user clicks the {web_element} button')
def click_on(context, web_element):
    selector = dataElements[context.section][web_element]['selector']
    element = dataElements[context.section][web_element][selector]
    Page.explicitWait(context, selector, element, 5)
    Page(context).click(selector, element)
    time.sleep(3)


