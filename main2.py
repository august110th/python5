import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
# with open("phonebook_raw.csv", encoding='utf-8') as f:
#   rows = csv.reader(f, delimiter=",")
#   contacts_list = list(rows)
# # pprint(contacts_list)
#
pattern = r'(\+7|8)\s*\(*(495)\)*\s*\-*(\d{3})\-*(\d{2})\-*(\d+)(\s*\(*(доб.)\s*(\d+)\)*)*'
substitution = r'+7(\2)\3-\4-\5 \7\8'
# for i in contacts_list:
#   for v in i:
#     result = re.sub(pattern, substitution, v)
#     print(result)
# # result = [re.sub(pattern, substitution,i) for i in contacts_list]
# # print(result)
#
# with open("phonebook.csv", "w", newline='') as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)


