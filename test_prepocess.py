import os
import csv
from os import listdir


from preprocess_csv import proc_csv

list_files = listdir("roll_list")

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
LIST_DIR = os.path.join(BASE_DIR, "roll_list/")

for f in list_files:
    print(f)
    file_csv = os.path.join(LIST_DIR, f)
    new_rows = []
    students = set()
    # 기존의 파일 읽기
    with open(file_csv, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        post_reader = proc_csv(reader)

    # 전처리 데이터 출력 - 확인용
    post_reader.write_post_csv(f, os.path.join(BASE_DIR, 'results/'))
