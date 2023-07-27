# -*- coding: utf-8 -*-
# do not touch upper part!!

# json extractor

import json
import os

#(edit here) set your json file folder path
path = ""

file_list = os.listdir(path)

json_file_list = [file for file in file_list if file.endswith('.json')]

def json_extractor(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        contents = f.read()
        json_data = json.loads(contents)
    if os.path.isfile("data.json"):
        with open("data.json", "r", encoding="utf8") as f:
            contents = f.read()
            json_add_data = json.loads(contents)
        for idx in range(len(json_data["data"])):        
            if "attribute" in json_data["data"][idx]["attributes"][0]:
                # (edit here) set your class name (main part) in json file
                class_name = json_data["data"][idx]["attributes"][0]["name"]
                if class_name not in json_add_data:
                    json_add_data[class_name] = []
                json_add_data[class_name].append({
                    # (edit here) set your sub parts in json file
                    "fileName": json_data["metaData"]["name"],
                    "start" : json_data["data"][idx]["start"],
                    "end" : json_data["data"][idx]["end"],
                    "attribute" : json_data["data"][idx]["attributes"][0]["attribute"]
                })
        with open("data.json", "w", encoding="utf8") as f:
            json.dump(json_add_data, f, ensure_ascii=False, indent=4)
    else:
        json_save_data = {}
        for idx in range(len(json_data["data"])):
            if "attribute" in json_data["data"][idx]["attributes"][0]:
                # (edit here) set your class name (main part) in json file
                class_name = json_data["data"][idx]["attributes"][0]["name"]
                json_save_data[class_name] = []
                json_save_data[class_name].append({
                    # (edit here) set your sub parts in json file
                    "fileName": json_data["metaData"]["name"],
                    "start" : json_data["data"][idx]["start"],
                    "end" : json_data["data"][idx]["end"],
                    "attribute" : json_data["data"][idx]["attributes"][0]["attribute"]
                })
        with open("data.json", "w", encoding="utf8") as f:
            json.dump(json_save_data, f, ensure_ascii=False, indent=4)

    

print("working")
for file in json_file_list:
    json_extractor(path + "/" + file)

print ("done")
