import argparse
import xlsxwriter

def parse_people(file_path):
    people = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            parts = lines[i].strip().split()
            if len(parts) == 4:
                name = parts[0]
                surname = parts[1]
                age = int(parts[2])
                profession = parts[3]
                person = {
                    'name': name,
                    'surname': surname,
                    'age': age,
                    'profession': profession
                }
                people.append(person)
            i += 1
    return people

def write_to_excel(people, output_file, sort=False, profession_filter=None):
    if sort:
        people.sort(key=lambda x: x['name'])

    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet('All People')

    bold_yellow = workbook.add_format({'bold': True, 'bg_color': '#FFFF00'})
    green_bg = workbook.add_format({'bg_color': '#C6EFCE'})
    headers = ['Name', 'Surname', 'Age', 'Profession']

    col = 0
    while col < len(headers):
        worksheet.write(0, col, headers[col], bold_yellow)
        col += 1

    row = 1
    i = 0
    while i < len(people):
        person = people[i]
        fmt = green_bg if person['age'] > 25 else None
        worksheet.write(row, 0, person['name'], fmt)
        worksheet.write(row, 1, person['surname'], fmt)
        worksheet.write(row, 2, person['age'], fmt)
        worksheet.write(row, 3, person['profession'], fmt)
        row += 1
        i += 1

    if profession_filter:
        sheet_name = profession_filter.capitalize()
        prof_ws = workbook.add_worksheet(sheet_name)

        col = 0
        while col < len(headers):
            prof_ws.write(0, col, headers[col], bold_yellow)
            col += 1

        row = 1
        i = 0
        while i < len(people):
            person = people[i]
            if person['profession'].lower() == profession_filter.lower():
                fmt = green_bg if person['age'] > 25 else None
                prof_ws.write(row, 0, person['name'], fmt)
                prof_ws.write(row, 1, person['surname'], fmt)
                prof_ws.write(row, 2, person['age'], fmt)
                prof_ws.write(row, 3, person['profession'], fmt)
                row += 1
            i += 1

    workbook.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='path to db.txt')
    parser.add_argument('-x', '--xlsx', required=True, help='output excel file name')
    parser.add_argument('-a', '--alphabet', default='no', help='sort by name: yes/no')
    parser.add_argument('-p', '--profession', help='filter by profession to a second sheet')

    args = parser.parse_args()
    sort = args.alphabet.lower() in ['yes', 'true']
    people = parse_people(args.file)
    write_to_excel(people, args.xlsx, sort=sort, profession_filter=args.profession)

if __name__ == '__main__':
    main()
