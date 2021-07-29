from tag_manipulator import TagManipulator


def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","
    regex = ","
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult


def test_split_one_string_result_array_of_one():
    # arrange
    stringToSplit = "java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult


def test_split_one_string_result_array_of_one_remove_whitespace():
    # arrange
    stringToSplit = " java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult


def test_split_two_string_result_array_of_two():
    # arrange
    stringToSplit = "java, python"
    regex = ","
    expResult = ["java", "python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult


def test_split_one_string_result_array_of_one_remove_trailing_comma():
    # arrange
    stringToSplit = ",java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult
