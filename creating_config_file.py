import configparser
def create_config_ini():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'path_to_save_files': "/Users/kpodlaska/PycharmProjects/pythonProject/Capstone",
                         'files_count': '1',
                         'file_name': 'fake_data_file',
                         'file_prefix': 'count',
                         'data_schema': '"{\"date\": \"timestamp:\",\"name\": \"str:rand\",\"type\": \"['client', 'partner', 'government']\"," \
                      "\"animal_type\": \"['cat', 'dog', 'monkey','tiger']\",\"age\": \"int:rand(1, 90)\",\"kids_number\": " \
                      "\"int:rand(1, 6)\"} "',
                         'data_lines': '100'}
    config['bitbucket.org'] = {}
    config['bitbucket.org']['User'] = 'hg'
    config['topsecret.server.com'] = {}
    topsecret = config['topsecret.server.com']
    topsecret['Port'] = '50022'     # mutates the parser
    topsecret['ForwardX11'] = 'no'  # same here
    config['DEFAULT']['ForwardX11'] = 'yes'
    with open('example.ini', 'w') as configfile:
       config.write(configfile)

if __name__ == '__main__':
    create_config_ini()
