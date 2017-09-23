import csv
import re


class Entry:
    """Entry class for creating new entry,
    searching entries,editing entries,deleting entries."""
    def __init__(self):
        """Constructor."""
        self.flag = 'a'

    def new_entry(self, rows, action):
        """New entry, self.flag determinate to add or to write."""
        if action:
            self.flag = 'w'
        with open('record.csv', self.flag, newline='') as csvfile:
            txt = csv.writer(csvfile, delimiter=',')
            for row in rows:
                txt.writerow([row[0], row[1], row[2], row[3]])

    @staticmethod
    def search(word, field):
        """Search by date, date range, exact search and regex pattern."""
        with open('record.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            txt = list(data)
        if field != 'regex':
            return [row for row in txt if word in row]
        else:
            return [row for row in txt
                    if re.search(r'{}'.format(word), str(row), re.I | re.X)]

    def edit(self, new, old):
        """Edit, rewrite the csv file including the changed row
        using the new_entry() method."""
        with open('record.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            txt = list(data)
            rows = []
            for row in txt:
                if row == old:
                    rows.append(new)
                else:
                    rows.append(row)
            self.new_entry(rows, 1)

    def delete(self, old):
        """Delete, rewrite the csv file excluding the changed row
        using new_entry() method."""
        with open('record.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            txt = list(data)
            rows = []
            for row in txt:
                if row == old:
                    continue
                else:
                    rows.append(row)
            self.new_entry(rows, 1)
