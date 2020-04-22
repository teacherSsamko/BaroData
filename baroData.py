import csv
import os
from math import ceil
from os import listdir

list_files = listdir("roll_list/")
print(list_files)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
LIST_DIR = os.path.join(BASE_DIR, "roll_list/")

for f in list_files:
    file_csv = os.path.join(LIST_DIR, f)
    new_rows = []
    students = set()
    # 기존의 파일 읽기
    with open(file_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        # next(reader)
        for row in reader:
            # print(' '.join(row))
            if row and row[4] != '':
                # new_line = ','.join([row[4], row[0], row[5]])
                new_line = [row[4], row[0], row[5]]
                new_rows.append(new_line)
                students.add(row[4])

    students.remove('이름')
    s_num = len(students)
    # count about subjects
    subjects_count = ceil(len(new_rows) // s_num)
    # 새로운 파일에 쓰기
    file_name = '(이름순)' + f
    RESULT_DIR = os.path.join(BASE_DIR, 'results/')
    result_file = os.path.join(RESULT_DIR, file_name)
    new_rows[0] = ['이름', '차시', '출결']
    # window에서는 encoding ='cp949'
    with open(result_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 1번 부터 번호순으로
        for i in range(s_num + 1):
            # 한 과목씩
            for s in range(subjects_count):
                subject_index = s_num + 1
                writer.writerow(new_rows[i + subject_index * s])
                if i == 0:
                    break

                # writer.writerow(new_rows[i + s_num + 1])
