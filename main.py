import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

pattern = r'(\+7|8)\s*\(*(495)\)*\s*\-*(\d{3})\-*(\d{2})\-*(\d+)(\s*\(*(доб.)\s*(\d+)\)*)*'
substitution = r'+7(\2)\3-\4-\5 \7\8'

def new_phone(lines: str):
    new_phone = re.sub(pattern, substitution, lines)
    # print(new_phone)
    return new_phone

new_contact_list = list()
new_contact_list.append(contacts_list[0])
new_name = []
surname_list = list()
# print(new_contact_list)
for line in contacts_list[1:]:
    surname = line[0].split()[0]
    if surname not in surname_list:
        surname_list.append(surname)
        phone = new_phone(line[5])
        new_name = line[0].split() + line[1].split() + line[2].split()
        organization = line[3]
        position = line[4]
        email = line[6]
        new_name.extend([organization, position, phone, email])
        new_contact_list.append(new_name)
    else:
        organization = line[3]
        position = line[4]
        email = line[6]
        phone = new_phone(line[5])
        number = surname_list.index(surname)
        if organization:
            new_contact_list[number + 1][3] = organization
        if position:
            new_contact_list[number + 1][4] = position
        if phone:
            new_contact_list[number + 1][5] = phone
        if email:
            new_contact_list[number + 1][6] = email
# print(new_contact_list)
with open("phonebook.csv", "w", newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contact_list)


