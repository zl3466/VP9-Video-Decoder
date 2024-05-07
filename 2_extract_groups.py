import json
import os
import shutil


''' copy multi agent log to decoder dir '''
json_list = []
root_dir = "C:/Users/ROG_ZL/Documents/github/mmobility"
date = "2024_03_08"
agent_json_dir = f"{root_dir}/multi_groups/{date}/{date}_multi.json"
scene_dict = json.load(open(agent_json_dir))
scene_list = scene_dict.keys()

for scene in scene_list:
    item = scene_dict[scene]
    json_list.append({
        "scene_idx": scene,
        "utime_start": item[0][0],
        "utime_end"  : item[0][1],
        "cars"       : item[1]
    })

if not os.path.exists(f"src/encoded_data/_{date}"):
    os.makedirs(f"src/encoded_data/_{date}")
with open(f"src/encoded_data/_{date}/_{date}_groups.json", 'w') as json_file:
    json.dump(json_list, json_file, indent=4)

''' copy multi traversal log to decoder dir '''
traversal_json_dir = f"{root_dir}/traversal_groups/{date}/{date}_traversal.json"
shutil.copyfile(traversal_json_dir, f"src/encoded_data/_{date}/_{date}_traversal.json")
