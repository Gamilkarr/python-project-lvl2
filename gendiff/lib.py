import json

NEW = "+"
OLD = "-"
CUR = " "


def convert(element):
    if element is True:
        return "true"
    elif element is False:
        return "false"
    elif element is None:
        return "null"
    return element


def render(diff):
    result = []

    for key in sorted(diff.keys()):
        if isinstance(diff[key], dict):
            if CUR in diff[key]:
                result.append(f"  {CUR} {key}: {convert(diff[key][CUR])}")
            if OLD in diff[key]:
                result.append(f"  {OLD} {key}: {convert(diff[key][OLD])}")
            if NEW in diff[key]:
                result.append(f"  {NEW} {key}: {convert(diff[key][NEW])}")
        else:
            result.append(f"  {OLD} {key}: {convert(diff[key])}")

    return "{\n" + "\n".join(result) + "\n}"


def diff(object, new_object):

    for key in new_object:
        if key in object and object[key] != new_object[key]:
            object[key] = {OLD: object[key], NEW: new_object[key]}
        elif key in object and object[key] == new_object[key]:
            object[key] = {CUR: object[key]}
        elif key not in object:
            object[key] = {NEW: new_object[key]}

    return object


def generate_diff(file_path_1, file_path_2):

    with open(file_path_1) as f1, open(file_path_2) as f2:
        file_1 = json.load(f1)
        file_2 = json.load(f2)

    return render(diff(file_1, file_2))
