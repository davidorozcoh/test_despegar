from utils.browser import Browser
from utils.functions import *
from utils.log import logger
import os


def before_all(context):
    context.environment = get_config("behave", "environment")
    context.browser_name = context.config.userdata['browser']
    context.status = 'unknown'
    info = "** Environment: {}, Browser: {} **".format(context.environment,
                                                       context.browser_name)
    if context.browser_name == 'safari' and "Windows" in os.getenv('PLATFORM'):
        exit(" \n Safari in not available for Windows Platforms")
    print(info)
    logger.info("", info)


def before_scenario(context, scenario):
    if context.browser_name in Browser.drivers.keys():
        context.browser = Browser.set_up(context.browser_name, scenario.name)
        # context.browser.maximize_window()
    else:
        exit("\n Invalid browser")


def after_step(context, step):
    try:
        context.failed_steps = []
        if step.status == 'failed':
            context.failed_steps.append(step.name)
            capture(context, step.name)
        # if hasattr(context, "section"):
        #     print("section", context.section)
    except Exception as e:
        print("error:", e)


def after_scenario(context, scenario):
    logger.info(scenario.name, scenario.__dict__)
    scenario.failed_steps = context.failed_steps
    context.status = object_value(str(scenario.status))
    if os.getenv('UPDATE_TEST_RAIL'):
        test_rail_update_state(scenario)
    if os.getenv('EXECUTION') == 'remote':
        context.browser.execute_script("lambda-status=" + str(context.status))
    browser_quit(context)


def after_all(context):
    if hasattr(context, 'browser'):
        context.browser.manage().deleteAllCookies()
        browser_quit(context)


def browser_quit(context):
    if hasattr(context, 'browser'):
        context.browser.close()
        context.browser.quit()





