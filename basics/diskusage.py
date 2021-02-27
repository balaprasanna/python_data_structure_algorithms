import os
import pathlib


def get_file_info(path, result):
    # check if it reaches the leaf node.
    if os.path.exists(path) and os.path.isfile(path):
        return {path: os.path.getsize(path)}

    if os.path.isdir(path):
        for files_and_folders in os.listdir(path):
            p = os.path.join(path, files_and_folders)
            result_dct.update(get_file_info(p, result))
    return result_dct


if __name__ == '__main__':
    result_dct = {}
    result = get_file_info("/home/prasanna/", result_dct)
    for k, v in result.items():
        print(f"result {k} : {v}")