# csv 파일 전처리 - 잘못된 row 제거
import csv
import os

from str_datetime import str_time


class proc_csv:
    def __init__(self, reader):
        self.reader = reader
        self.new_rows = []
        self.students = set()
        self.remove_issue()

    def remove_issue(self):
        for row in self.reader:
            # print(row)
            # 문제 있는 row 패스
            if len(row) < 3:
                # print(row)
                # print('lower than 3')
                continue
            if row[5] != '출결' and row[5] != '결석':
                timestamp = str_time(row[5]).strftime("%H:%M:%S")
            else:
                timestamp = row[5]
            new_line = [row[4], row[0][2:4], timestamp]
            self.new_rows.append(new_line)
            self.students.add(row[4])
        self.students.remove('이름')

    def write_post_csv(self, file, dir):
        # 새로운 파일에 쓰기
        file_name = '(post)' + file
        result_file = os.path.join(dir, file_name)
        with open(result_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in self.new_rows:
                writer.writerow(row)
