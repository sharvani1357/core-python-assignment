menu = list(map(str.strip, input("initial_menu=").split(',')))
add= input("add_item= ").strip()
remove= input("remove_item= ").strip()
check= input("check_item= ").strip()
def add_item(item):
    menu.append(item)
def remove_item(item):
    if item in menu:
        menu.remove(item)
    else:
        print("not found")
def check_item(item):
    if item in menu:
        print(f"Availability: '{item}' is available")
    else:
        print(f"Availability: '{item}' is not available")
add_item(add)
remove_item(remove)
print("Updated menu:", menu)
check_item(check)
