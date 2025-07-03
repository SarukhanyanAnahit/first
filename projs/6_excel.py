import argparse
import xlsxwriter

def read(fname):
    try:
        with open(fname, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print("file doesn't exist")

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='Path to db.txt')
    parser.add_argument('-x', '--xlsx', required=True, help='Output Excel file name')
    parser.add_argument('-a', '--alphabet', default='no', help='Sort by name: yes/no')
    parser.add_argument('-p', '--profession', help='Filter by profession to a second sheet')
    return parser.parse_args()

def parse_people(lines):
    people = []
    i = 0
    while i < len(lines):
        parts = lines[i].strip().split()
        if len(parts) == 4:
            try:
                person = {
                    'name': parts[0],
                    'surname': parts[1],
                    'age': int(parts[2]),
                    'profession': parts[3]
                }
                people.append(person)
            except ValueError:
                print(f"invalid")
        i += 1
    return people

def write_headers(worksheet, headers, h_fmt):
    col = 0
    while col < len(headers):
        worksheet.write(0, col, headers[col].capitalize(), h_fmt)
        col += 1

def write_people(worksheet, people, headers, green):
    row = 1
    i = 0
    while i < len(people):
        person = people[i]
        if person['age'] > 25:
            fmt = green
        else:
            fmt=None

        col = 0
        while col < len(headers):
            worksheet.write(row, col, person[headers[col]], fmt)
            col += 1

        row += 1
        i += 1

def write_to_excel(people, output_file, sort=False, profession_filter=None):
    if sort:
        people.sort(key=lambda x: x['name'])

    try:
        workbook = xlsxwriter.Workbook(output_file)
        bold_yellow = workbook.add_format({'bold': True, 'bg_color': '#FFFF00'})
        green_bg = workbook.add_format({'bg_color': '#C6EFCE'})
        headers = ['name', 'surname', 'age', 'profession']
        worksheet = workbook.add_worksheet("All People")
        write_headers(worksheet, headers, bold_yellow)
        write_people(worksheet, people, headers, green_bg)

        if profession_filter:
            filtered = []
            i = 0
            while i < len(people):
                if people[i]['profession'].lower() == profession_filter.lower():
                    filtered.append(people[i])
                i += 1

            if filtered:
                prof_ws = workbook.add_worksheet(profession_filter.capitalize())
                write_headers(prof_ws, headers, bold_yellow)
                write_people(prof_ws, filtered, headers, green_bg)

        workbook.close()

    except:
        print(f"error writing to excel")

def main():
    args = arguments()
    sort = args.alphabet.lower() in ['yes', 'true']
    lines = read(args.file)
    people = parse_people(lines)
    if people:
        write_to_excel(people, args.xlsx, sort=sort, profession_filter=args.profession)

if __name__ == '__main__':
    main()
