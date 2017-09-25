import csv


menu = 'WORK LOG\n' \
       '\n' \
       'Choose your action!\n' \
       '[a] Add new task\n' \
       '[b] Search\n' \
       '[c] Quit program\n' \
       '>\n' \
       '\n'
sub_menu = 'Choose your search option!\n' \
           '[a] Exact date\n' \
           '[b] Range of dates\n' \
           '[c] Exact search\n' \
           '[d] Regex pattern\n' \
           '[e] Return to menu\n' \
           '>'
choose = "Choose from the available letters!\n"
exact = 'Enter text\n' \
        '>'
start = 'Enter start date (use DD/MM/YYYY format!)\n' \
        '>'
end = 'Enter end date (use DD/MM/YYYY format!)\n' \
      '>'
regex = 'Enter pattern\n' \
        '>'
entries = 'Date: {}\n' \
          'Title: {}\n' \
          'Time spent: {}\n' \
          'Notes: {}\n'
result = 'Result {} of {}\n'
error = 'Enter a valid date!\n'
must = 'You must fill this field!\n'
date = 'Enter date (use DD/MM/YYYY format!)[Q]\n' \
       '>'
time = 'Enter time spent (use just integers!)\n' \
       '>'
title = 'Enter task name\n' \
        '>'
notes = 'Enter additional notes (Optional!)\n' \
        '>'
deleted = 'Task successfully deleted!\n''
saved = 'The new task was successfully saved!\n'
edit = "You can't let this field empty!\n" \
       "Old {}\n" \
       "{}\n"
edit_notes = 'If you let the field empty it will save it EMPTY!\n' \
             'Old {}\n' \
             '{}\n'
no_task = 'Task not found! Please try again.\n'
no_pattern = "Pattern doesn't exist! Please try again.\n"


with open('prompt.csv', 'w') as csvfile:
    fieldnames = ['menu', 'sub_menu', 'entries', 'must', 'date', 'error',
                  'title', 'time', 'notes', 'saved', 'edit', 'no_task',
                  'exact', 'start', 'no_pattern', 'end', 'result', 'regex',
                  'edit_notes', 'choose', 'deleted']
    txt = csv.DictWriter(csvfile, fieldnames=fieldnames)

    txt.writeheader()
    txt.writerow({
        'menu': menu,
        'sub_menu': sub_menu,
        'entries': entries,
        'error': error,
        'date': date,
        'title': title,
        'must': must,
        'no_task': no_task,
        'no_pattern': no_pattern,
        'edit_notes': edit_notes,
        'result': result,
        'notes': notes,
        'choose': choose,
        'time': time,
        'deleted': deleted,
        'saved': saved,
        'edit': edit,
        'exact': exact,
        'start': start,
        'end': end,
        'regex': regex
    })
