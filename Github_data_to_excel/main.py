from Github_ETL import SQL_Leetcode_repo
import configparser

def load_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

if __name__ == "__main__":
    #specify the path
    config_file_path = "configs/connect.config"

    if not config_file_path:
        raise Exception(" provide config file path")

    #load the config
    config = load_config(config_file_path)

    ltcode = SQL_Leetcode_repo(config)
    git_contents_json_data = ltcode.extract()
    ltcode.transform(git_contents_json_data )
    #ltcode.xcel_otpt(list_of_dicts)
    ltcode.load()

