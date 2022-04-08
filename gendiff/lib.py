from . import parse


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


def format(diff):
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

    data_1 = parse.open_file(file_path_1)
    data_2 = parse.open_file(file_path_2)
    data_diff = diff(data_1, data_2)

    return format(data_diff)
