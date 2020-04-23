# csv 파일 전처리 - 잘못된 row 제거
import csv
import os

from str_datetime import str_time


class proc_csv:
    def __init__(self, reader):
        self.reader = reader
        self.preprocessed = []
        self.new_rows = []
        self.students = set()
        self.preprocess()
        self.deal_csv()

    def deal_csv(self):
        for row in self.preprocessed:
            new_line = [row[4], row[0][2:4], row[5]]
            self.new_rows.append(new_line)
            self.students.add(row[4])
        self.students.remove('이름')

    def preprocess(self):
        for row in self.reader:
            if len(row) < 3:
                if len(row) > 1:
                    self.preprocessed[-1].extend(row[1:])
                continue
            if row[5] != '출결' and row[5] != '결석':
                timestamp = str_time(row[5]).strftime("%H:%M:%S")
            else:
                timestamp = row[5]
            row[5] = timestamp
            self.preprocessed.append(row)

    def write_post_csv(self, file, dir):
        # 새로운 파일에 쓰기
        file_name = '(post)' + file
        result_file = os.path.join(dir, file_name)
        with open(result_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in self.preprocessed:
                writer.writerow(row)
