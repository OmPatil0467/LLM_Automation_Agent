import json
import re
from src.llm_handler import call_llm
from src.file_handler import read_file, write_file
from src.utils import count_weekdays, sort_contacts
from src.tasks import execute_data_generation, execute_prettier_format

def execute_task(task: str):
    task = task.lower()

    if "install uv" in task and "run" in task and "datagen.py" in task:
        return execute_data_generation()

    elif "format" in task and "prettier" in task:
        return execute_prettier_format()

    elif "wednesdays" in task:
        return count_weekdays("/data/dates.txt", "Wednesday", "/data/dates-wednesdays.txt")

    elif "sort contacts" in task:
        return sort_contacts("/data/contacts.json", "/data/contacts-sorted.json")

    elif "extract email" in task:
        content = read_file("/data/email.txt")
        email = call_llm(f"Extract email from text: {content}")
        return write_file("/data/email-sender.txt", email)

    else:
        raise ValueError("Task not recognized.")