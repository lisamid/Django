# # ������� �1
# # print("������� 1")
# x_str = input("������ ����� ������ ")
# x = list()
# x = x_str.split()
# x_x = input("������� = ")

# for i in range(len(x)):
#     try:
#         x[i] = float(x[i])**int(x_x)
#     except:
#         x[i] = x[i]*int(x_x)

# print(x)

# # ������� �2
# # print("������� 2")
# x_str = input("������� ������ ").lower()
# d = {}
# for i in range(len(x_str)):
#     if x_str[i] != " ":
#         d.update({ x_str[i] : x_str.count(x_str[i]) })
# print(d)

# # ������� �3
# # print("������� 3")
# dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
# k = set()
# v = set()
# for key, value in dct.items():
#     k.add(key)
#     v.add(value)
# print(k)
# print(v)
# print(k | v)

# # ������� �*"
# # print("������� *")
# dictionary = {
#     "���":                  ["������", "������",    "����",     "�������",      "�������",      "���������", "�������",  "�������", "�����", "������"],
#      "�������":             ["������", "�������",   "�������",  "����������",   "�������",      "������",    "��������", "�������", "�������", "�������"],
#      "����� ����������":    ["������", "����",      "�����",    "�����",        "������",       "�����",     "������",   "����",    "�����", "������"],
#      "��� ��������":        [2000,      1987,    2003, 1993, 2001, 2001, 1976, 1957, 1969, 1999],
#      "����� ��������":      [6, 4, 11, 12, 9, 9, 5, 2, 3, 6],
#      "����� ��������":      [11, 25, 5, 3, 27, 31, 13, 12, 28, 24],
#      "������": ["�������", "��������", "���������", "��������", "�������", "�������", "��������", "������", "��������", "�������"]
# }
# # ����� ���� ����������, ������� �������� ����� ������� �������� ��� ���� �� (�������)
# # ����� ���������, ������� � ������, ��������� � ���������
# # ������ ��������� �������� ����� � ������ ��������, � ������� ������� ���� (������ �� �������). ���������, ��� ����� ���� �� ����� ���������� �� ����� ������� � �������.
# ln = len(dictionary.get("���")) - 1
# i = 0

# while i <= ln:
#     if dictionary["���"][i] == "������": dictionary["���"][i] = "�������"
#     if dictionary["�������"][i].find("�������") >= 0 and dictionary["����� ����������"][i] == "������": dictionary["����� ����������"][i] = "���������"
#     if dictionary["���"][i] == "���������" and dictionary["�������"][i] == "������": dictionary["������"][i] = "��������"
#     if dictionary["���"][i] == "�������" and dictionary["�������"][i] == "�������":
#         for dp in (dictionary): dictionary[dp].remove(dictionary[dp][i])
#         ln -= 1
#         i -= 1
#     i += 1

# d = dict()
# d.update({ "������� ���" : [dictionary["�������"][i] + " " + dictionary["���"][i] for i in range(len(dictionary["���"]))]})
# d.update({ "���� ��������" : [str(dictionary["��� ��������"][i]) + "-" + str(dictionary["����� ��������"][i]) + "-" + str(dictionary["����� ��������"][i]) for i in range(len(dictionary["���"]))]})
# d.update({ "����� ����������" : [dictionary["����� ����������"][i] for i in range(len(dictionary["����� ����������"]))]})
# d.update({ "������" : [dictionary["������"][i] for i in range(len(dictionary["������"]))]})

# for dp in (d): print(d[dp])

# # ������� �*2"
# # print("������� *2")

# set1 = {6, 31, 14, 25, 19, 3, 55}
# set2 = {30, 22, 6, 79, 25}
# set3 = {9, 1, 22, 19, 30}

# set0 = set(zip(set1, set2))
# set0 = set(zip(set0, set3))

# print(set0)

# n2, n3 = zip(*set0)
# n1, n2 = zip(*n2)

# set1.symmetric_difference_update(n1)
# set2.symmetric_difference_update(n2)
# set3.symmetric_difference_update(n3)

# set_ = set1
# set_.update(set2)
# set_.update(set3)
# list_ = set_
# print(list_)