from os import path
import csv
import logging
import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

# all_data = {}
last_id = 0
name_db = "telephone_book.csv"


def read_all():
    global all_data, last_id

    print(name_db)
    if path.exists(name_db):
        with open(name_db, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            all_data = [i for i in csv_reader]
            last_id = all_data[-1]["id"]
            return all_data
    else:
        logging.warning(f"The database is not connected! Missing database file.")
        print("The database is not connected!")


def print_all():
    for_output = [" ".join(k.values()) for k in all_data]
    print(*for_output, sep="\n", end=f"\n{'-' * 20}\n\n")


def add_entry(data):
    global last_id

    logging.info(f"Adding a new entry: {data}")

    if all(data.values()) and matching_rec(data, all_data):
        last_id = int(last_id) + 1
        data["id"] = last_id

        with open(name_db, "a", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "name", "surname", "phone", "description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)
            logging.warning(f"Data added to the notebook: {data.values()}")
            print("Data added to the notebook")
    else:
        logging.warning(f"The data is already present in the database")
        print("The data is already present in the database")



def find_entry(data_find, all_info):
    logging.info(f"Search for an entry: {data_find}")
    candidates = [" ".join(i.values()) for i in all_info if data_find in i.values()]
    if candidates:
        logging.info(f"Search result: {candidates}")
        print(*candidates, sep="\n", end="\n\n")
        return [n[0] for n in candidates]
    else:
        logging.warning(f"No data found: {data_find}")
        print("Name or phone number not found.\n")
        return 0

def matching_rec(new_entry: dict, all_info):
    value = list(new_entry.values())[1:]
    all_values = [list(k.values())[1:] for k in all_info]
    return value not in all_values


def check_new_data(num):
    answer = input(f"Enter a {num}: ")
    while True:
        if num in "name surname description":
            if answer.isalpha():
                break
        if num == "phone":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" of the number is 11 digits\n"
                       f"Enter a {num}: ")
    return answer


def del_entry(data_del):
    global all_data

    logging.info(f"Deleting an entry: {data_del}")
    id_cand = find_entry(data_del, all_data)
    if id_cand:
        id_del = input(f"Enter the id: ")
        logging.info(f"Id selected: {id_del}")

        if id_del in id_cand:
            all_data = [k for k in all_data if k["id"] != id_del]
            with open(name_db, "w", encoding="utf-8", newline="") as file:
                fieldnames = ["id", "name", "surname", "phone", "description"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_data)
                logging.info(f"Data deleted")
                print("Data deleted\n")
        else:
            logging.warning(f"No data found: {data_del}")
            print("Id not found.\n")
    else:
        logging.warning(f"No data found: {data_del}")


def edit_entry(data_change, id_change):
    global all_data
    key, value = data_change

    logging.info(f"Data changes: {data_change}")
    if find_entry(id_change, all_data):
        for i, v in enumerate(all_data):
            if v["id"] == id_change:
                logging.info(f"Current value: {v[key]}")
                v[key] = value
                logging.info(f"New value: {v[key]}")
                all_data[i] = v

        with open(name_db, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "name", "surname", "phone", "description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_data)
            logging.info(f"Data changed")
            print("Data changed\n")
    else:
        logging.warning(f"No data found: {data_change}")
        print("Id not found.\n")


def file_import(name):
    global name_db

    logging.info(f"Changing the database file: {name}")
    if path.exists(name):
        name_db = name
        print(name_db)
    else:
        logging.warning(f"The database was not found: {name}")
        print("The database was not found.\n")


def save_csv(file_name):
    logging.info(f"Export in csv format: {file_name}.csv")

    with open(f'{file_name}.csv', 'w', encoding="utf-8", newline="") as file_w, \
            open('telephone_book.csv', encoding="utf-8") as file_r:
        all_data = csv.DictReader(file_r)
        fieldnames = ["id", "name", "surname", "phone", "description"]
        writer = csv.DictWriter(file_w, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)
        print(f"{file_name}.csv file saved\n")


def save_json(file_name):
    logging.info(f"Export in json format: {file_name}.json")

    with open(f'{file_name}.json', 'w', encoding="utf-8", newline="") as file_w, \
            open('telephone_book.csv', encoding="utf-8") as file_r:
        all_data = csv.DictReader(file_r)
        data_dict = {rows['id']: rows for rows in all_data}
        file_w.write(json.dumps(data_dict, indent=4, ensure_ascii=False))


def save_xml(file_name):
    logging.info(f"Export in xml format: {file_name}.xml")

    with open(f'{file_name}.xml', 'w', encoding="utf-8", newline="") as file_w, \
            open('telephone_book.csv', encoding="utf-8") as file_r:
        all_data = csv.DictReader(file_r)
        data_dict = {rows['id']: rows for rows in all_data}
        xml_data = dicttoxml(data_dict, attr_type=False).decode()
        dom = parseString(xml_data)
        file_w.write(dom.toprettyxml())


def menu():
    read_all()
    while True:
        print(f"Telephone book\n{'*' * 20}")
        actions = input("1. Show all entries\n"
                        "2. Find an entry\n"
                        "3. Add an entry\n"
                        "4. Edit an entry\n"
                        "5. Delete an entry\n"
                        "6. Import/Export\n"
                        "7. Exit\n")
        match actions:
            case "1":
                print_all()
            case "2":
                find_entry(input("Enter surname or phone number: "), read_all())
            case "3":
                add_entry(add_menu())
            case "4":
                print_all()
                id_change = input(f"Enter the id: ")
                if find_entry(id_change, read_all()) and (answer := edit_menu()):
                    edit_entry(answer, id_change)
            case "5":
                del_entry(input("Enter surname or phone number: "))
            case "6":
                import_export_menu()
            case "7":
                logging.info("Stop program.\n")
                print("Goodbye! Thank you for using our product!")
                break
            case _:
                logging.warning(f"Main menu, wrong item selected.")
                print("The data is not recognized, repeat the input.")


def add_menu():
    logging.info('Start add menu')
    add_dict = {"id": "1", "name": "", "surname": "", "phone": "", "description": ""}
    for i in add_dict:
        if i != "id":
            add_dict[i] = check_new_data(i)
    logging.info('Stop edit menu')
    return add_dict


def edit_menu():
    add_dict = {"1": "name", "2": "surname", "3": "phone", "4": "description"}
    logging.info('Start edit menu')
    while True:
        print("\nChanging:")
        change = input("1. name\n"
                       "2. surname\n"
                       "3. phone\n"
                       "4. description\n"
                       "5. exit\n")

        match change:
            case "1" | "2" | "3" | "4":
                type_date = add_dict[change]
                return type_date, check_new_data(type_date)
            case "5":
                logging.info('Exited the edit menu')
                return 0
            case _:
                logging.warning(f"Edit menu, wrong item selected.")
                print("The data is not recognized, repeat the input.")


def import_export_menu():
    logging.info('Start import/export menu')
    while True:
        print("\nImport\\Export:")
        change = input("1. import file\n"
                       "2. export file\n"
                       "3. exit\n")
        match change:
            case "1":
                file_import(input(f"Enter the database name: "))
                return
            case "2":
                while True:
                    logging.info('Start choose a format menu')
                    format_type = input(f"Choose a format:\n"
                                        f"1. CSV\n"
                                        f"2. JSON\n"
                                        f"3. XML\n"
                                        f"4. exit\n")
                    match format_type:
                        case "1":
                            save_csv(input("Enter the name of the file: "))
                            return
                        case "2":
                            save_json(input("Enter the name of the file: "))
                            return
                        case "3":
                            save_xml(input("Enter the name of the file: "))
                            return
                        case "4":
                            logging.info('Exited the choose a format menu')
                            return
                        case _:
                            logging.warning(f"Choose a format menu, wrong item selected.")
                            print("The data is not recognized, repeat the input.")

            case "3":
                logging.info('Exited the import/export menu')
                break
            case _:
                logging.warning(f"Import/export menu, wrong item selected.")
                print("The data is not recognized, repeat the input.")
menu()