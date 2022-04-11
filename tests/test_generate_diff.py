from gendiff import generate_diff


def test_generate_diff_flat_json():
    with open("tests/fixtures/flat_result.txt") as file:
        result = file.read()
    assert generate_diff("tests/fixtures/flat_file1.json",
                         "tests/fixtures/flat_file2.json") == result


def test_generate_diff_flat_yaml():
    with open("tests/fixtures/flat_result.txt") as file:
        result = file.read()
    assert generate_diff("tests/fixtures/flat_file1.yaml",
                         "tests/fixtures/flat_file2.yaml") == result


def test_generate_diff_yaml():
    with open("tests/fixtures/result.txt") as file:
        result = file.read()
    assert generate_diff("tests/fixtures/file_1.yaml",
                         "tests/fixtures/file_2.yaml") == result


def test_generate_diff_json():
    with open("tests/fixtures/result.txt") as file:
        result = file.read()
    assert generate_diff("tests/fixtures/file_1.json",
                         "tests/fixtures/file_2.json") == result
