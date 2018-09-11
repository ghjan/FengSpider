# _*_ coding: utf-8 _*_
import csv
import json
import os
import time

from project.lagou.get_files import get_filelist
from project.lagou.lagou_mobile import write_to


def json2csv(json_string, position, directory='csv'):
    try:
        city = json_string['content']['positionResult']['locationInfo']['city']
    except:
        city = "上海"

    # try:
    #     positionName = json_string['content']['positionResult']['queryAnalysisInfo']['positionName']
    # except:
    positionName = position

    filename = directory + '/' + city + '_' + positionName + '.csv'
    is_existed = os.path.exists(filename)
    with open(filename, 'a', encoding='utf-8') as f:
        fieldnames = ['city', 'companyFullName', 'companyName', 'positionName', 'salary']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not is_existed:
            writer.writeheader()
        result = json_string['content']['positionResult']['result']
        time.sleep(2)
        write_to(result, writer)


if __name__ == "__main__":
    exts = ("json",
            )
    fileList = get_filelist(1, 'json_files', exts=exts)
    filters = ('blockchain',)
    for file_name in fileList:
        position = file_name.split('.')[0].split('_')[0]
        if position not in filters:
            continue
        file_path = 'json_files/' + file_name
        with open(file_path, 'r', encoding='utf-8') as jsonfile:
            try:
                json_string = json.load(jsonfile, encoding='utf-8')
                json2csv(json_string, position, directory='csv')
            except Exception as e:
                print(e)
                print(file_path)
                continue
