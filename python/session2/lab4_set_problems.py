"""Set Problems - Testing student capability with set operations."""


def set_operations(set1: set, set2: set):
    """Perform basic set operations on two sets.

    Args:
        set1 (set): First set
        set2 (set): Second set

    Returns:
        dict: Dictionary with union, intersection, difference
    """
    # Write your solution here
    return {'union':set1.union(set2),'intersection':set1.intersection(set2),
            'difference':set1.difference(set2)}


def find_unique_elements(list1, list2):
    """Find elements that are unique to each list using sets.

    Args:
        list1 (list): First list
        list2 (list): Second list

    Returns:
        tuple: (unique_to_list1, unique_to_list2)
    """
    # Write your solution here
    set1 = set(list1)
    set2 = set(list2)
    return (set1.difference(set2), set2.difference(set1))


def remove_vowels_set(text:str):
    """Remove vowels from text using set operations.

    Args:
        text (str): Input text

    Returns:
        str: Text with vowels removed
    """
    # Write your solution here
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    set1 = set(text)

    #DISCUSS: risk of scrambling the original text, since set is unordered
    return str(set1.difference(vowels))

def find_common_friends(friend_list:dict):
    """Find common friends between all given friends in the dictionary.
    
    Args:
        friend_list (dict): Keys has the name of the account, the values is a set of friends
        
    Returns:
        dictionary with the same Keys, but the value another dict with the key as the other person
        and the value is a set of mutual friends
    """
    all_mutual_friends = {}
    for person1 in friend_list:
        all_mutual_friends[person1] = {}
        for person2 in friend_list:
            if person1 != person2:
                mutual_friends = friend_list[person1].intersection(friend_list[person2])
                all_mutual_friends[person1][person2] = mutual_friends
    return all_mutual_friends

if __name__ == "__main__":
    # Test cases
    print("Testing set_operations...")
    result = set_operations({1, 2, 3, 4}, {3, 4, 5, 6})
    assert result["union"] == {1, 2, 3, 4, 5, 6}, "Union test failed"
    assert result["intersection"] == {3, 4}, "Intersection test failed"

    print("Testing find_unique_elements...")
    result = find_unique_elements([1, 2, 3, 4], [3, 4, 5, 6])
    assert result[0] == {1, 2}, f"Expected {{1, 2}}, got {result[0]}"
    assert result[1] == {5, 6}, f"Expected {{5, 6}}, got {result[1]}"

    print("Testing remove_vowels_set...")
    RESULT = remove_vowels_set("Hello World")
    assert "a" not in RESULT.lower(), "Vowels should be removed"
    assert "H" in RESULT and "l" in RESULT, "Consonants should remain"

    print("Testing find_common_friends...")
    friends = {
        "Alice": {"Bob", "Charlie", "David"},
        "Bob": {"Alice", "Charlie", "Eve"},
        "Charlie": {"Alice", "Bob", "Frank"},
    }

    result = find_common_friends(friends)
    expected = {
    "Alice": {
        "Bob": {"Charlie"},
        "Charlie": {"Bob"}
    },
    "Bob": {
        "Alice": {"Charlie"},
        "Charlie": {"Alice"}
    },
    "Charlie": {
        "Alice": {"Bob"},
        "Bob":{"Alice"}
    }
    }

    assert result == expected

    print("All tests passed!")
