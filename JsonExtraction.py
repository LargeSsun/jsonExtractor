# -*- coding: utf-8 -*-
# do not touch upper part!!

# json extractor

import json
import os

#(edit here) set your json file folder path
path = "E:/DataSet/videos/1.Training/[label]01_crowd_morpheme/morpheme/02"

file_list = os.listdir(path)

json_file_list = [file for file in file_list if file.endswith('.json')]

def json_extractor(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        contents = f.read()
        json_data = json.loads(contents)

    # (edit here) set your class name (main part) in json file
    class_name = json_data["data"][0]["attributes"][0]["name"]

    if os.path.isfile("data2.json"):
        with open("data2.json", "r", encoding="utf8") as f:
            contents = f.read()
            json_save_data = json.loads(contents)
        if class_name not in json_save_data:
            json_save_data[class_name] = []
        json_save_data[class_name].append({
            # (edit here) set your sub parts in json file
            "fileName": json_data["metaData"]["name"],
            "start" : json_data["data"][0]["start"],
            "end" : json_data["data"][0]["end"]
        })
    else:
        json_save_data = {}
        json_save_data[class_name] = []
        json_save_data[class_name].append({
            # (edit here) set your sub parts in json file
            "fileName": json_data["metaData"]["name"],
            "start" : json_data["data"][0]["start"],
            "end" : json_data["data"][0]["end"]
        })


    with open("data2.json", "w", encoding="utf8") as f:
        json.dump(json_save_data, f, ensure_ascii=False, indent=4)

print("working")
for file in json_file_list:
    json_extractor(path + "/" + file)

print ("done")