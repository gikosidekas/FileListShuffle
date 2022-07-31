# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import os
from os import listdir
from os.path import isfile, join


def print_shuffled_file_list():
    current_file_list_path = os.getcwd()
    onlyfiles = [f for f in listdir(current_file_list_path + "/putFileHere") if
                 isfile(join(current_file_list_path + "/putFileHere", f))]
    onlyfiles = strip_txt_postfix(onlyfiles)
    shuffle_and_save_files(current_file_list_path, onlyfiles)


def shuffle_list_times(times, words):
    while times > 0:
        random.shuffle(words)
        times -= 1
    return words


def strip_txt_postfix(files):
    filtered = []

    for file in files:
        filtered.append(file.strip(".txt"))

    return filtered


def shuffle_and_save_files(current_file_list_path, onlyfiles):
    for file in onlyfiles:
        with open(current_file_list_path + "/putFileHere/" + file + ".txt", 'r') as f:
            words = [line.strip() for line in f]
            shuffle_list_times(24, words)

        with open(current_file_list_path + "/getFileHere/" + file + "_shuffled.txt", 'w') as w:
            for word in words:
                w.write(word + "\n")


if __name__ == '__main__':
    print_shuffled_file_list()
