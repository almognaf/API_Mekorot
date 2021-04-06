from Classes.api import Api
from Classes.config import Config
from Classes.dataframe import Dataframe
from datetime import datetime
import time

if __name__ == "__main__":
    while True:
        apiClass = Api()
        i = 0
        mechine = ["st3", "st7"]
        len_mechine = len(mechine)
        for i in range(len_mechine):
            nodes_array = apiClass.get_data(mechine[i], i, len_mechine-1)
            config = Config.load_config_file()
            data = Dataframe.transform_nodes_to_csv(nodes_array)
            print("!!!!!!!!!!!!!!!time runing: ")
            print(i + 1)
            if data.all:
                data.to_csv(config['dataFolderPath'] + '//data-' + str(datetime.now().timestamp()) + '.csv', index=True)
                print("done")
        time.sleep(300)