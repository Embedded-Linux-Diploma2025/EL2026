"""Dictionary Problems - Testing student capability with dictionary operations."""
import collections

def dictionary_operations(dict1:dict, dict2:dict):
    """Perform basic operations on two dictionaries.

    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: Dictionary with merged, common_keys, and unique_keys
    """
    # Write your solution here
    set1 = set(dict1)
    set2 = set(dict2)
    common = set1.intersection(set2)
    unique_1 = set1.difference(set2)
    unique_2 = set2.difference(set1)
    unique = unique_1.union(unique_2)
    dict1.update(dict2)
    return {'merged':dict1, 'common_keys':common, 'unique_keys':unique}


def count_word_frequency(text):
    """Count the frequency of each word in a text string.

    Args:
        text (str): Input text

    Returns:
        dict: Dictionary with word frequencies
    """
    # Write your solution here
    # word_dict = {}
    # for word in text.split():
    #     if(word in word_dict):
    #         word_dict[word]+=1
    #     else:
    #         word_dict[word] = 1
    return collections.Counter(text.split())



def dictionary_filtering(students_grades:dict):
    """Filter students based on their grades.

    Args:
        students_grades (dict): Dictionary with student names as keys and grades as values

    Returns:
        dict: Dictionary with students who have grades >= 70
    """
    # Write your solution here
    # filtered_students = {}
    # for key,value in students_grades.items():
    #     if(value >=70):
    #         filtered_students[key] = value
    # return filtered_students
    return {name:grade for name,grade in students_grades.items() if grade>=70}


def nested_dictionary_access(nested_dict:dict, keys_path):
    """Access value in nested dictionary using a list of keys.

    Args:
        nested_dict (dict): Nested dictionary
        keys_path (list): List of keys to traverse

    Returns:
        any: Value at the specified path, or None if path doesn't exist
    """
    # Write your solution here
    traverse_dict = nested_dict
    value = -1
    for key in keys_path:
        if not isinstance(traverse_dict,dict):
            return None
        value = traverse_dict.get(key)
        if value is not None:
            traverse_dict = traverse_dict[key]
        else:
            return None
    return value


if __name__ == "__main__":
    # Test cases
    print("Testing dictionary_operations...")
    result = dictionary_operations({"a": 1, "b": 2}, {"b": 3, "c": 4})
    expected = {"merged": {"a": 1, "b": 3, "c": 4}, "common_keys": {"b"}, "unique_keys": {"a", "c"}}
    assert result == expected, f"Expected {expected}, got {result}"
    assert result["merged"] == {"a": 1, "b": 3, "c": 4}, "Merged dictionary incorrect"
    assert result["common_keys"] == {"b"}, "Common keys incorrect"
    assert result["unique_keys"] == {"a", "c"}, "Unique keys incorrect"

    print("Testing count_word_frequency...")
    result = count_word_frequency("hello world hello python world")
    expected = {"hello": 2, "world": 2, "python": 1}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing dictionary_filtering...")
    result = dictionary_filtering({"Alice": 85, "Bob": 65, "Charlie": 90, "Diana": 45})
    expected = {"Alice": 85, "Charlie": 90}
    assert result == expected, f"Expected {expected}, got {result}"

    print("Testing nested_dictionary_access...")
    nested = {"level1": {"level2": {"level3": "found"}}}
    result = nested_dictionary_access(nested, ["level1", "level2", "level3"])
    assert result == "found", f"Expected 'found', got {result}"

    result = nested_dictionary_access(nested, ["level1", "nonexistent"])
    assert result is None, f"Expected None, got {result}"

    print("All tests passed!")
