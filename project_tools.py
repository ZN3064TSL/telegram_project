import json

#with open('config.json', 'w') as file:
#    json.dump({'TOKEN': '6937851636:AAGtUV9SBER9Zgb-dgg4knKh0BstpVULRkM'}, file)
def get_config(file):
    with open(file, 'r') as json_file:
        config = json.load(json_file)
        return config