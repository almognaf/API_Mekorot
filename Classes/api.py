import requests
import json
from datetime import datetime as date_lib
from Classes.config import Config


class Api:
    config = None
    datetime_format = '%d/%m/%Y %H:%M:%S'

    def __init__(self):
        self.config = Config.load_config_file()
        if self.config['lastUpdate'] == 'None':
            update_time = date_lib.now().timestamp() - float(self.config['periodInSec'])
            self.config['lastUpdate'] = date_lib.fromtimestamp(update_time).strftime(self.datetime_format)

    @staticmethod
    def send_get_request(url):
        response = requests.get(url)
        return response

    @property
    def get_data(self, mechine, curret, len_mechine):
        start_time = date_lib.strptime(self.config['lastUpdate'], self.datetime_format).timestamp()
        end_time = start_time + (int(self.config['periodInSec']) * 0.0833333)  # will run every 30 mins
        if end_time > date_lib.now().timestamp():
            return []
        url = self.config['mekorotUrl'] + '?q=browse&subnodes=' + self.config['subnodesDepth'] + '&at=' \
              + self.config['key']
        response = self.send_get_request(url)
        response_json = json.loads(response.text)
        print(response.text)
        subnodes = list(response_json["subnodes"])
        print(len(subnodes))
        subnodes = list(
            filter(lambda x: x['kind'] == 2 and x['tagname'] and x['path'].startswith('/mekorot0002/drv1/' + mechine),
                   subnodes))
        print(len(subnodes))
        history_string = 'q=history&t1=' + str(start_time) + '&t2=' + str(end_time) \
                         + '&interpolate=1&interval=' \
                         + self.config['intervalOfSamplesInSec']
        responses_for_sub_nodes = []
        i = 1
        for node in subnodes:
            node_name = node["path"]
            url = self.config['mekorotUrl'] + '?' + history_string + '&table=1&at=' + self.config[
                'key'] + '&nodes=' + node_name
            print(url)
            response = self.send_get_request(url)
            response_json = json.loads(response.text)
            temp_dict = {
                "node": node,
                "states": response_json["states"]
            }
            i += 1
            with open("node", "w") as sub:
                json.dump(subnodes, sub)
            # print(subnodes)
            with open("subnode", "w") as nod:
                json.dump(node, nod)
            responses_for_sub_nodes.append(temp_dict)
            break
        if curret == len_mechine:
            with open('config.json', 'w') as outfile:
                self.config['lastUpdate'] = date_lib.fromtimestamp(end_time).strftime(self.datetime_format)
                obj = json.dumps(self.config)
                outfile.write(obj)
        return responses_for_sub_nodes
