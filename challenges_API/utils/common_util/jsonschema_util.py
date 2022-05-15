import json, os, logging
from jsonschema import validate


def check_schema_file_exist(file_path):
    if not os.path.exists(file_path):
        logging.error(
            f"The schema file is not found, please check it again, path: {file_path}"
        )
        raise


def get_schema_file_path(file_name):
    cwd_path = os.getcwd()
    return f"{cwd_path}/schemas/{file_name}.json"


def get_schema(file_name, api_name):
    schema_file_path = get_schema_file_path(file_name)
    check_schema_file_exist(schema_file_path)
    with open(schema_file_path, "r") as file:
        schema = json.load(file)
    return schema[api_name]


def validate_json_schema(json_data, file_name, api_name):
    schema_data = get_schema(file_name, api_name)
    validate(instance=json_data, schema=schema_data)
