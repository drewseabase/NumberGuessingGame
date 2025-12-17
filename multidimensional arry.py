multi_array = ['a', 'b', ['c', 'd', ['e']]]
picked_string = 'e'

def find_path(item, target, path=None):
    if path is None:
        path = []

    if isinstance(item, list):
        for i, thing in enumerate(item):
            result = find_path(thing, target, path + [i])
            if result is not None:
                return result
        return None
    else:
        if item == target:
            return path
        return None

path = find_path(multi_array, picked_string)

if path is None:
    print(f"'{picked_string}' was not found.")
else:
    print(f"Found '{picked_string}' at path: {path}")

    # Show how you'd index it like multi_array[2][2][0]
    temp = multi_array
    for idx in path:
        temp = temp[idx]
    print("Value at that path:", temp)


