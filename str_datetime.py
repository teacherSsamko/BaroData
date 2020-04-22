import datetime


def str_time(str_for_date):
    # str_for_date = '2020. 4. 20. 오전 10:39:58'
    str_split = str_for_date.split(" ")
    str_split = str_split[3:]
    # print(str_split)

    if str_split[0] == "오전":
        str_split[0] = "AM"
    else:
        str_split[0] = "PM"

    str_for_date = "".join(str_split)
    # print(str_for_date)
    return datetime.datetime.strptime(str_for_date, "%p%H:%M:%S")
