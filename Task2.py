import re

def get_cats_info(path: str) -> list[dict[str, str]] | None :
    cats_info = []
    regex_pattern = r".+,.+,\d+"  # Entry pattern
    cats_entries = list[str]()

    try:
        with open(path) as file:
            file_content = file.read()
            cats_entries = re.findall(regex_pattern, file_content)
    except FileNotFoundError:
        print("File not found!")
        return None

    if len(cats_entries) == 0:
        print("No Cats entries found in file! Check file format and try again.")
        return None

    for entry in cats_entries:
        cat_info_values = entry.split(",")
        cat_formatted = {
            "id": cat_info_values[0],
            "name": cat_info_values[1],
            "age": int(cat_info_values[2]),
        }
        cats_info.append(cat_formatted)

    return cats_info

