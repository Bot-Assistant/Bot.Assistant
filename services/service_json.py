import json
import os

from services.service_logger import Logger


def create_json(path, data):
    with open(path, 'w') as outfile:
        Logger.debug(f"[SERVICE][JSON]Create {path}", False)
        json.dump(data, outfile, indent=4)


def read_json(path):
    with open(path) as json_file:
        Logger.debug(f"[SERVICE][JSON]Read {path}", False)
        data = json.load(json_file)
    return data


def update_json(path, data):
    with open(path, 'w') as outfile:
        Logger.debug(f"[SERVICE][JSON]Update {path}", False)
        json.dump(data, outfile, indent=4)


def delete_json(path):
    Logger.debug(f"[SERVICE][JSON]Delete {path}", False)
    os.remove(path)
