import datetime
import os
import csv

from entry import Entry

with open('prompt.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile, delimiter=',')
    txt = list(data)

ENTRY = Entry()


def clear():
    """Clear the screen"""
    return os.system('cls' if os.name == 'nt' else 'clear')


def add_date(prompt):
    """Date input with ValueError exception
    Makes sure that there is an input."""
    while True:
        clear()
        try:
            date_in = input(prompt)
            if date_in.lower() == 'q':
                break
            d, m, y = tuple(date_in.split('/'))
            out = datetime.date(year=int(y), month=int(m), day=int(d))
            if not out:
                clear()
                print(txt[0]['must'])
                break
            else:
                return out
        except ValueError:
            clear()
            print(txt[0]['error'])


def add_title():
    """Task name input
    Makes sure that there is an input."""
    while True:
        clear()
        data_in = input(txt[0]['title']).strip()
        if not data_in:
            clear()
            print(txt[0]['must'])
            continue
        else:
            return data_in


def add_time():
    """Time spent input with ValueError exception
    Makes sure that there is an input."""
    while True:
        try:
            clear()
            data_in = int(input(txt[0]['time']).strip())
            if not data_in:
                clear()
                print(txt[0]['must'])
                continue
            else:
                return data_in
        except ValueError:
            clear()
            print("JUST NUMBERS!")


def add_entry():
    """Add new task to the csv file """
    clear()
    date_in = add_date(txt[0]['date'])
    title_in = add_title()
    time_spent_in = add_time()
    clear()
    notes_in = input(txt[0]['notes'])
    if not notes_in:
        notes_in = ' '
    # Creates a list of fields for the new entry
    rows = [date_in, title_in, time_spent_in, notes_in],
    ENTRY.new_entry(rows, 0)
    clear()
    print(txt[0]['saved'])


def get_option(poz, entry):
    """The result menu options, removes the not wanted option """
    prompt = ['[P]revious', '[N]ext', '[E]dit', '[D]elete', '[R]eturn to menu']
    if poz == 0:
        prompt.remove('[P]revious')
    if poz == len(entry) - 1:
        prompt.remove('[N]ext')
    return prompt


def edit_task(entry_data, poz):
    """Edit an existing task.
    Makes sure to catch the date error and unwanted inputs.
    Replace the old data with the new input or old data"""
    clear()
    print(txt[0]['edit'].format('Date', entry_data[poz][0]))
    new_date = add_date(txt[0]['date'])
    clear()
    print(txt[0]['edit'].format('Task name', entry_data[poz][1]))
    new_title = add_title()
    clear()
    print(txt[0]['edit'].format('Time spent', entry_data[poz][2]))
    new_time = add_time()
    clear()
    print(txt[0]['edit_notes'].format('Notes', entry_data[poz][3]))
    new_notes = input(txt[0]['notes'])
    if not new_notes:
        new_notes = ' '
    print(txt[0]['saved'])
    new = [new_date, new_title, new_time, new_notes]
    ENTRY.edit(new, entry_data[poz])
    entry_data.pop(poz)
    entry_data.insert(poz, new)


def get_range(items):
    """Organize the date list"""
    date_list = []
    for a in items:
        for item in a:
            date_list.append(item)
    return date_list


def search_entry(action):
    """Searches entries by exact date, range of dates,
    exact search and regex pattern
    Catches the date errors"""
    clear()
    while True:
        if action == 'a':
            date_in = add_date(txt[0]['date'])
            date_data = ENTRY.search(str(date_in), 'date')
            if not date_data:
                clear()
                print(txt[0]['no_task'])
                break
            else:
                return result_menu(date_data)
        if action == 'b':
            clear()
            start = add_date(txt[0]['start'])
            clear()
            end = add_date(txt[0]['end'])
            day = datetime.timedelta(days=1)
            days = end - start + day
            date_list = []
            while days:
                date_list.append(ENTRY.search(str(start), 'date'))
                start += day
                days -= day
            if not date_list:
                clear()
                print(txt[0]['no_task'])
                break
            else:
                return result_menu(get_range(date_list))
        if action == 'c':
            clear()
            entry = input(txt[0]['title']).strip()
            title_data = ENTRY.search(entry, 'title')
            if not title_data:
                clear()
                print(txt[0]['no_task'])
                break
            else:
                return result_menu(title_data)
        if action == 'd':
            clear()
            entry = input(txt[0]['regex']).strip()
            pattern_data = ENTRY.search(entry, 'regex')
            if not pattern_data:
                clear()
                print(txt[0]['no_task'])
                break
            else:
                return result_menu(pattern_data)


def search_menu():
    """Search menu"""
    clear()
    while True:
        action = input(txt[0]['sub_menu']).lower().strip()
        if action in ['e', 'q']:
            clear()
            break
        elif action == 'a':
            search_entry(action)
        elif action == 'b':
            search_entry(action)
        elif action == 'c':
            search_entry(action)
        elif action == 'd':
            search_entry(action)
        else:
            clear()
            print("Choose from the available letters!\n")
            continue


def result_menu(entry):
    """Result list with the result menu"""
    index = 0
    clear()
    while True:
        print(txt[0]['entries'].format(entry[index][0],
                                       entry[index][1],
                                       entry[index][2],
                                       entry[index][3]))
        print(txt[0]['result'].format(index + 1, len(entry)))
        print('  '.join(get_option(index, entry)))
        action = input('>').lower().strip()
        if action not in ['p', 'n', 'e', 'd', 'r']:
            print(txt[0]['choose'])
            continue
        if (index + 1) == 1 and action == 'p':
            clear()
            print(txt[0]['choose'])
            continue
        if (index + 1) == len(entry) and action == 'n':
            clear()
            print(txt[0]['choose'])
            continue
        if action == 'r':
            clear()
            break
        if action == 'n':
            clear()
            index += 1
        if action == 'p':
            clear()
            index -= 1
        if action == 'd':
            answer = input("Are you sure?\n> [Y]es [N]o")
            if answer.lower() == 'y':
                ENTRY.delete(entry[index])
                entry.pop(index)
                if index == len(entry):
                    index -= 1
                clear()
                print(txt[0]['deleted'])
        if action == 'e':
            clear()
            edit_task(entry, index)
            continue


def menu():
    """Main loop"""
    while True:
        main_menu = input(txt[0]['menu'])
        if menu in ['c', 'q']:
            print('Session finished!')
            break
        if main_menu == 'a':
            clear()
            add_entry()
        elif main_menu == 'b':
            clear()
            search_menu()
        else:
            print(txt[0]['choose'])
            continue


if __name__ == "__main__":
    clear()
    menu()
