from utils.testrail import *
import configparser
import os
import names
import json
from dotenv import load_dotenv
from datetime import date
import datetime
import pandas as pd
from pathlib import Path
import requests

load_dotenv()
import re
from pprint import pprint
import pprint as pretty
import random
from datetime import datetime

'''Config'''


def get_config(section="driver", key=""):
    config = configparser.RawConfigParser()
    config.read("setup.cfg")
    return config.get(section, key)


'''Date'''


def get_actual_date(format_output):
    today = date.today()
    dates_list = []
    if format_output == "%m/%d/%Y":
        actual_date = datetime.strptime(str(today), "%Y-%m-%d").strftime(format_output)
    elif format_output == "%m/%d/%y":
        actual_date = datetime.strptime(str(today), "%Y-%m-%d").strftime(format_output)
    elif format_output == "d-m-h-y":
        today = today.ctime()
        dates_list.append(split_string(today, " ", 1))
        dates_list.append(split_string(today, " ", 3))
        dates_list.append(split_string(today, " ", 5))
        if dates_list[0] == "Jan":
            actual_date = f"January {dates_list[1]}, {dates_list[2]}"
        elif dates_list[0] == "Feb":
            actual_date = f"February {dates_list[1]}, {dates_list[2]}"
        elif dates_list[0] == "Mar":
            actual_date = f"March {dates_list[1]}, {dates_list[2]}"
        elif dates_list[0] == "Apr":
            actual_date = f"April {dates_list[1]}, {dates_list[2]}"
        elif dates_list[0] == "May":
            actual_date = f"May {dates_list[1]}, {dates_list[2]}"
        elif dates_list[0] == "Jun":
            actual_date = f"June {dates_list[1]}, {dates_list[2]}"
        elif dates_list[0] == "Jul":
            actual_date = f"July {dates_list[1]}, {dates_list[2]}"
        elif dates_list[0] == "Aug":
            actual_date = f"August {dates_list[1]}, {dates_list[2]}"
        elif dates_list[0] == "Sep":
            actual_date = f"September {dates_list[1]}, {dates_list[2]}"
        elif dates_list[0] == "Oct":
            actual_date = f"October {dates_list[1]}, {dates_list[2]}"
        elif dates_list[0] == "Nov":
            actual_date = f"November {dates_list[1]}, {dates_list[2]}"
        elif dates_list[0] == "Dec":
            actual_date = f"December {dates_list[1]}, {dates_list[2]}"
    else:
        actual_date = today
    return actual_date


'''Json handle'''


def update_json(json_name, field, value):
    with open("utils/json/" + json_name, 'r+') as f:
        json_data = json.load(f)
        json_data[field] = value
        f.seek(0)
        f.write(json.dumps(json_data))
        f.truncate()


def clean_data(json_name):
    with open("utils/json/" + json_name, 'r+') as f:
        json_data = json.load(f)
        for val in json_data:
            json_data[val] = ""
        f.seek(0)
        f.write(json.dumps(json_data))
        f.truncate()


def read_from_json(json_name, field):
    with open("utils/json/" + json_name) as f:
        json_data = json.load(f)
        data = json_data[field]
        f.close()
    return data


def log_file(name, value):
    f = open("utils/" + replace_spaces(name) + ".json", "a+")
    f.write(str(value))
    f.close()


'''Sort items'''


def validate_sorted_elements(elements_list, order):
    flag = False
    if order == 'ASC':
        print('entre a ASC')
        if (all(int(elements_list[i]) <= int(elements_list[i + 1]) for i in range(len(elements_list) - 1))):
            flag = True
        else:
            flag = False
    elif order == 'DESC':
        if (all(int(elements_list[i]) >= int(elements_list[i + 1]) for i in range(len(elements_list) - 1))):
            flag = True
    return flag


def validate_string_sorted_elements(elements_list, order):
    flag = False
    if order == 'ASC':
        if (all(elements_list[i] <= elements_list[i + 1] for i in range(len(elements_list) - 1))):
            flag = True
        else:
            flag = False
    elif order == 'DESC':
        if (all(elements_list[i] >= elements_list[i + 1] for i in range(len(elements_list) - 1))):
            flag = True
    return flag


def validate_dates_sorted_elements(elements_list, order):
    flag = False
    new_list = elements_list
    if order == 'ASC':
        new_list.sort(key=lambda date: datetime.strptime(date, "%M/%d/%Y"))
    elif order == 'DESC':
        new_list.sort(reverse=True, key=lambda date: datetime.strptime(date, "%M/%d/%Y"))
    if new_list == elements_list:
        flag = True
    return flag


'''String handle'''


def replace_spaces(text):
    return text.replace(" ", "_")


def split_string(text, separator, position):
    splitted_text = text.split(separator)
    return splitted_text[position]


def full_splited_string(text, separator):
    splitted_text = text.split(separator)
    return splitted_text


def check_string_contains(input_text, text):
    return input_text in text


def format_to_search(chain):
    list_to_manage = chain.split()
    new_list_part1 = list_to_manage[3:5]
    new_list_part2 = list_to_manage[0:3]
    str_one = concatenate(new_list_part1)
    str_tow = concatenate(new_list_part2)
    str_one = str_one.strip()
    str_tow = str_tow.rstrip()
    return str_one + ", " + str_tow


def modify_chain(chain, start_point, end_point):
    original = chain
    final_chain = original[int(start_point):int(end_point)]
    return final_chain


def concatenate(element_list):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in element_list:
        str1 += ele + " "
    # return string
    return str1


'''Generators'''


def name_generator(text, gender):
    return text + " " + names.get_first_name(gender=gender) + " " + names.get_first_name(gender=gender)


def random_name(text):
    return text + " " + names.get_first_name()


def last_name_generator(text):
    return text + " " + names.get_last_name()


def number_generator(text):
    number = str(random.random())
    return text + number[0:10]


def random_number_generator(size):
    generated_numbers = []
    for element in range(size):
        generated_numbers.append(str(random.randint(1, 9)))
    return ''.join(generated_numbers)


'''File'''


def file_path(file_name):
    return os.getcwd() + "./resources/" + file_name


def file_exists(name):
    home = str(os.path.join(Path.home(), "Downloads"))
    return os.path.isfile(home + '/' + name)


def read_csv(file_name):
    if file_exists(file_name):
        fullpath = str(os.path.join(Path.home(), "Downloads")) + '/' + file_name
        readed_file = pd.read_csv(fullpath, sep=',')
        return readed_file


'''Capture images'''


def capture(context, name):
    return context.browser.save_screenshot("screenshots/" + replace_spaces(name) + '.png')


"""Testrail Integration"""


def test_rail_connection():
    client = APIClient(os.getenv('TEST_RAIL_URL'))
    client.user = os.getenv('TEST_RAIL_USER')
    client.password = os.getenv('TEST_RAIL_SECRET_KEY')
    return client


def message(scenario):
    array_steps = text_between_qoutes(str(scenario.steps))
    formatted_steps = ""
    passed = 0
    failed = 0
    for step in array_steps:
        if step in scenario.failed_steps:
            status_step = ' `(failed)`'
            failed += 1
        else:
            status_step = ' `(passed)`'
            passed += 1
        formatted_steps += f" \n * {step} {status_step} "
    content = f"""
      **Feature**: {text_between_qoutes(str(scenario.feature))[0]}
      **Scenario**:  {str(scenario.name)}
      **Steps**: {formatted_steps}
      **Final status**: passed:{passed}, failed:{failed}
    """
    return str(content)


def test_rail_update_state(scenario):
    try:
        if len(scenario.tags) > 1:
            client = test_rail_connection()
            test_run = scenario.tags[0]
            test_case = scenario.tags[1]
            status = object_value(str(scenario.status))
            result = client.send_post(
                "add_result_for_case/{}/{}".format(test_run, test_case),
                {
                    'status_id': test_rails_status[status],
                    'comment': message(scenario)
                }
            )
            result_id = get_results(test_run, test_case)
            for step in scenario.failed_steps:
                file = replace_spaces(step)
                send_attachment(str(result_id), file)
            return result
    except Exception as e:
        print("error:", e)


test_rails_status = {
    "passed": 1,
    "blocked": 2,
    "retest": 4,
    "failed": 5,
}


def send_attachment(result_id, file_name):
    client = test_rail_connection()
    result = client.send_post("add_attachment_to_result/{}".format(result_id),
                              "screenshots/{}.png".format(replace_spaces(file_name)))


def get_results(test_run, test_case):
    client = test_rail_connection()
    result = client.send_get("get_results_for_case/{}/{}".format(test_run, test_case))
    return result[0]['id']


def text_between_qoutes(string):
    return re.findall(r'"(.*?)"', string)
    # return string.split('"')[1::2]


def text_outside_qoutes(string):
    return string.split('"')[0::2]


def keys_in_object(string):
    return re.findall(r"[.*?](.*?)>,", string)


def object_value(value):
    if not value.isalpha():
        value = value.split(".")[1]
    return value


'''HTTP Requests'''


def execute_request(method, path, xapiKey, xapiHost, params, token, body=None):
    url = "https://admin.secure.thoroughcare.us"
    if path == '/automation/create_patient.json' or path == '/automation/enroll_patient.json' or path == '/automation/log_time.json' or path == '/automation/schedule_a_call.json':
        content_type = "application/json"
    elif path == '/automation/delete_patient.json':
        content_type = "application/x-www-form-urlencoded"
    full_url = url + path
    headers = {'Content-Type': content_type}
    response = requests.request(method=method, url=full_url, headers=headers, params=params, verify=True, json=body)
    response.encoding = 'utf-8'
    data_obtained = response.json()
    print(data_obtained)
    return response


'''List operations'''


def get_list_average(passed_list):
    passed_values_int = [int(item) for item in passed_list]
    avg = sum(passed_values_int) / len(passed_values_int)
    avg_ordered = "{:.1f}".format(avg)
    if avg_ordered[3] == '0':
        changed_avg = avg_ordered[0:2]
        return changed_avg
    else:
        return "{:.1f}".format(avg)
