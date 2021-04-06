from datetime import datetime
import pandas as pd


class Dataframe:
    @staticmethod
    def transform_nodes_to_csv(nodes_array):
        df = None
        print(nodes_array)
        for node in nodes_array:
            values, timestamps = [], []
            for item in range(len(node['states'])):
                timestamps.append(datetime.fromtimestamp(node['states'][item]['stamp']))
                value = list(node['states'][item]['values'])
                if len(value) == 1:
                    values.append(value[0])
                else:
                    values.append(value)
            if len(list(filter(lambda x: x is not None, values))) > 0:
                if df is None:
                    df = pd.DataFrame({node['node']['tagname']: values}, index=timestamps)
                else:
                    df.insert(0, node['node']['tagname'], values, allow_duplicates=True)
        return df

