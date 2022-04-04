from gendiff import generate_diff


def test_generate_diff_json():
    with open("tests/fixtures/result.txt") as file:
        result = file.read()
    assert generate_diff("tests/fixtures/file1.json",
                         "tests/fixtures/file2.json") == result


def test_generate_diff_yaml():
    with open("tests/fixtures/result.txt") as file:
        result = file.read()
    assert generate_diff("tests/fixtures/file1.yaml",
                         "tests/fixtures/file2.yaml") == result
