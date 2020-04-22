import csv
import os
from math import ceil
from os import listdir
from datetime import datetime, time, timedelta

from str_datetime import str_time

list_files = listdir("roll_list/")

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
LIST_DIR = os.path.join(BASE_DIR, "roll_list/")

for f in list_files:
    file_csv = os.path.join(LIST_DIR, f)
    new_rows = []
    students = set()
    # 기존의 파일 읽기
    with open(file_csv, newline='', encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            if row and row[4] != '':
                if row[5] != '출결' and row[5] != '결석':
                    timestamp = str_time(row[5]).strftime("%H:%M:%S")
                else:
                    timestamp = row[5]
                new_line = [row[4], row[0][2:4], timestamp]
                new_rows.append(new_line)
                students.add(row[4])

    students.remove('이름')
    s_num = len(students)
    # count about subjects
    subjects_count = ceil(len(new_rows) // s_num)
    new_rows[0] = ['이름', '차시', '출결']

    # 학생 이름으로 과목 모으기
    # 1번 부터 번호순으로
    order_by_timetable = []
    for i in range(s_num + 1):
        # 한 과목씩
        for s in range(subjects_count):
            subject_index = s_num + 1
            order_by_timetable.append(new_rows[i + subject_index * s])
            # header는 한 번만
            if i == 0:
                break

    # 이수 시간을 기준으로 과목 재정렬하기
    reordered = []
    temp = []
    for i in range(len(order_by_timetable)):
        if i == (s_num + 1) * i:
            order_by_timetable[i].append('소요시간')
            reordered.append(order_by_timetable[i])
            continue
        if not i % 5 == 0:
            temp.append(order_by_timetable[i])
        else:
            temp.append(order_by_timetable[i])
            # print(temp)
            temp.sort(key=lambda temp: temp[2])
            # 소요시간 계산을 위한 temp2
            temp2 = [temp[0]] + temp[:-1]

            for i in range(len(temp)):

                if temp[i][2] != '결석':
                    elapsed = datetime.strptime(
                        temp[i][2], "%H:%M:%S") - datetime.strptime(temp2[i][2], "%H:%M:%S")
                    if elapsed < timedelta(seconds=1):
                        temp[i].append('시작')
                        continue
                    dt = datetime(2020, 1, 1, 0, 0, 0) + elapsed
                    temp[i].append(f'({dt.time()})')
                else:
                    temp[i].append('-')
            for item in temp:
                reordered.append(item)
            temp = []

    # 새로운 파일에 쓰기
    file_name = '(이름순)' + f
    RESULT_DIR = os.path.join(BASE_DIR, 'results/')
    result_file = os.path.join(RESULT_DIR, file_name)

    # window에서는 encoding ='cp949'
    with open(result_file, 'w', newline='', encoding='cp949') as csvfile:
    # with open(result_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in reordered:
            writer.writerow(row)

    # # window에서는 encoding ='cp949'
    # with open(result_file, 'w', newline='', encoding='utf-8') as csvfile:
    #     writer = csv.writer(csvfile)
    #     # 1번 부터 번호순으로
    #     for i in range(s_num + 1):
    #         # 한 과목씩
    #         for s in range(subjects_count):
    #             subject_index = s_num + 1
    #             writer.writerow(new_rows[i + subject_index * s])
    #             if i == 0:
    #                 break
