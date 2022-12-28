from random import choices

# name1='poly.txt'
# name2='poly1.txt'

# with open(name1, 'r', encoding='utf-8') as m_file1, \
#             open(name2, 'r', encoding='utf-8') as m_file2:
#         for line in m_file1:
#             print(line)
#         str1 = m_file1.readlines()
#         str2 = m_file2.readlines()

# print(str1)
# print(str2)

def poly_sum(name1: str, name2: str):
    with open(name1, 'r', encoding='utf-8') as m_file1, \
            open(name2, 'r', encoding='utf-8') as m_file2:
        str1 = m_file1.readlines()
        str2 = m_file2.readlines()

        if len(str1) == len(str2):
            with open('sum_poly.txt', 'a', encoding='utf-8') as m_file3:
                for i, v in enumerate(str1):
                    m_file3.write(f'{v[:-5]}+{str2[i]}')
        else:
            print('нет фалов для суммирования')

poly_sum('poly.txt', 'poly1.txt')            