import json

def load_json():
    with open('config\config1.json','r') as f:
        config_data=json.load(f)
    return config_data
def get_directory_path(directory_name):
    config_data=load_json()
    directory_path_object=config_data.get("directory_path",{})
    directory_path=directory_path_object.get(directory_name)
    return directory_path