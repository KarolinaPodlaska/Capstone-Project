"""Hope for the best but plan for the worst"""
import logging
import argparse
import configparser
import uuid
import os
import creating_fake_data
import json
from faker import Faker
import creating_fake_data
import random




def init_arg_parser():
    parser = argparse.ArgumentParser(prog='magicgenerator')

    parser.add_argument('--path_to_save_files',
                        help="Define a path to output file. For current path use '.', As deflaut is ./Capstone",
                        type=str,
                        default="/Users/kpodlaska/PycharmProjects/pythonProject/Capstone")
    parser.add_argument('--files_count', help="Define how many json file do you want to generate", type=int)
    parser.add_argument('--file_name', help="Choose name to your file", type=str)
    parser.add_argument('--file_prefix', help="If you chose more than 1 output file please choose prefix", type=str,
                        choices=['count', 'random', 'uuid'])
    parser.add_argument('--data_schema', help='Provide data Schema for your output files')
    parser.add_argument('--data_lines', help='How many lines your output file has')
    parser.add_argument('--clear_path',
                        help='If this flag is on, before the script starts creating new data files, all files in '
                             'path_to_save_files that match file_name will be deleted.')
    parser.add_argument('--multiprocessing', help='The number of processes used to create files')

    args = parser.parse_args()

    return args

def existing_dir(prospective_dir):
    isdir = os.path.isdir(prospective_dir)
    try:
        isdir is True
        return prospective_dir
    except TypeError:
        logging.critical("DIR is not exist!")

print(existing_dir(os.getcwd()))
"""
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                      'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}

topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)

print('If you read this line it means that you have provided '
      'all the parameters')"""


def init_logger():
    """
    Here we will put potential
    settings for the parser
    :return:
    """
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(pathname)s | %(message)s')
    logging.getLogger('faker').setLevel(logging.ERROR)
    return None

def construct_files(file_name, prefix, how_many_files):
    ext="json"
    prefixes = []
    if prefix == "count":
        for n in range(how_many_files):
            prefixes.append(str(n+1))
    elif prefix == "random":
        for n in range(how_many_files):
            number=random.randint(1,1_000_000_000_000)
            prefixes.append(number)
    elif prefix == "uuid":
        for n in range(how_many_files):
            x_n = uuid.uuid4()
            prefixes.append(x_n)

    full_filenames = []
    for prefix_ in prefixes:
        full_filename = file_name+"_" + str(prefix_) + "."+ext
        full_filenames.append(full_filename)

    return full_filenames

def creating_name_from_numbers_and_lowercase():
    numbers='0123456789'
    symbol='-'
    all =  ascii_lowercase + numbers
    lenght_1 = 8
    lenght_2 = 4
    lenght_3 = 12
    mid_lenght_part ="".join(random.sample(all, lenght_1))
    short_lenght_part = "".join(random.sample(all, lenght_2))
    long_lenght_part = "".join(random.sample(all, lenght_3))
    name =mid_lenght_part+symbol+(short_lenght_part+symbol)*3+long_lenght_part
    return name
def create_data_without_output_file(lines, d_schema):
    if lines > 0:
        for i in range(lines):
            data = creating_fake_data.create_fake_dict(d_schema)
            print(f"{data}")
    else:
        logging.critical("You can't proccess with {} number of lines".format(lines))
def create_output_file(f_line, d_schema, path, f_name, f_prefix, f_number):
    new_files = construct_files(f_name, f_prefix, f_number)
    lines = int(f_line)
    for new_file in new_files:
        path_to_file = existing_dir(path)
        new_file_with_dir = os.path.join(path_to_file, new_file)
        with open(new_file_with_dir, "w") as f:
            for i in range(lines):
                data = creating_fake_data.create_fake_dict(d_schema)
                json.dump(data, f)

def main():
    """
    Having main helps organize code,
    we can see where main routine happens
    We can clearly see the steps
    :return:
    """
    print("Hello from main!")
    init_logger()
    parsed_args = init_arg_parser()
    logging.info(parsed_args)
    if existing_dir(parsed_args.path_to_save_files):
        pass
    else:
        logging.info("Directory doesn't exist!")

    logging.info(f'Current path : {parsed_args.path_to_save_files}')
    logging.info(f'You choose to generate {parsed_args.files_count} files')
    logging.debug(f'Name of your files is {parsed_args.file_name} with prefixes {parsed_args.file_prefix}. '
                  f'Every file have {parsed_args.data_lines} lines')

    if parsed_args.path_to_save_files == ".":
        path = os.getcwd()
        logging.debug(f"You are in current directory. Path : {path}")
    else:
        path = existing_dir(parsed_args.path_to_save_files)
        logging.debug(f"Path : {path}")

    if parsed_args.path_to_save_files is None and parsed_args.files_count is not None:
        logging.info("You didn't choose the path dir, so path is current file ")

    if int(parsed_args.files_count) > 0 and (parsed_args.file_name, parsed_args.file_prefix, parsed_args.path_to_save_files, parsed_args.data_lines, parsed_args.data_schema) is not None:
        new_files=construct_files(parsed_args.file_name, parsed_args.file_prefix, parsed_args.files_count)
        lines = int(parsed_args.data_lines)
        for new_file in new_files:
            path_to_file = existing_dir(parsed_args.path_to_save_files)
            new_file_with_dir = os.path.join(path_to_file, new_file)
            with open(new_file_with_dir, "w") as f:
                for i in range(lines):
                    data = creating_fake_data.create_fake_dict(parsed_args.data_schema)
                    json.dump(data, f)
    if int(parsed_args.files_count) == 0 and (parsed_args.data_lines, parsed_args.data_schema) is not None:
        logging.info("You choose to generate 0 files, so result is printed without output file, nor file_name, file_prefix or path_to_save_files won't needed")
        lines = int(parsed_args.data_lines)
        create_data_without_output_file(lines,parsed_args.data_schema)
            #TODO: I used print in create_data_without_output_file, can stay that way?
    if int(parsed_args.files_count) < 0:
        logging.error("Incorrect value!!! There is no possibility to genereate {}. Put positive number or zero to "
                      "generate answer without output files".format(parsed_args.files_count))

    if parsed_args.file_name is not None and parsed_args.file_prefix is not None and int(parsed_args.files_count) > 0 and int(parsed_args.data_lines) > 0 and parsed_args.data_schema is not None:
        logging.info(f"You choose to generate {parsed_args.files_count} file with {parsed_args.data_lines} lines named: {parsed_args.file_name} with prefix {parsed_args.file_prefix} method")

    if parsed_args.files_count and parsed_args.file_name and parsed_args.file_prefix and parsed_args.path_to_save_files and parsed_args.data_lines and parsed_args.data_schema:
        new_files=construct_files(parsed_args.file_name, parsed_args.file_prefix, parsed_args.files_count)
        lines = int(parsed_args.data_lines)
        for new_file in new_files:
            path_to_file = existing_dir(parsed_args.path_to_save_files)
           # data = creating_fake_data.create_fake_dict(parsed_args.data_schema)
            new_file_with_dir = os.path.join(path_to_file, new_file)
            with open(new_file_with_dir, "w") as f:
                for i in range(lines):
                    data = creating_fake_data.create_fake_dict(parsed_args.data_schema)
                    json.dump(data, f)




if __name__ == '__main__':
    main()
