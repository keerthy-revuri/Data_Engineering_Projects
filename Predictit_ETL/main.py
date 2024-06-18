from Predictit_ETL import Predict
import configparser

def load_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

if __name__ == "__main__":
    #specify the path
    config_file_path = "configs/sample.config"

    if not config_file_path:
        raise Exception(" provide config file path")

    #load the config
    config = load_config(config_file_path)

    pred = Predict(config)
    pred.extract()
    pred.transform()
    pred.load()

