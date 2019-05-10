#!/usr/bin/python3

import json
import os


class ReadHelper:
    def __init__(self, path):
        self.path = path
        self.content = []
        self.value_list = []
        self.key_list = []
        try:
            with open(self.path, 'r') as load_f:
                self.content = json.load(load_f)
        except FileNotFoundError:
            print("No such file or directory in " + path)
        except json.decoder.JSONDecodeError:
            print("Json Format Error")
        _, self.name = os.path.split(path)

        for i in self.content:
            for k, v in i.items():
                self.key_list.append(k)
                self.value_list.append(v)
                # print(k)
                # print(v)

    def print_all(self):
        print("print all!!!!!!!!!!!!!!")
        print("These are content:")
        for i in self.content:
            for k, v in i.items():
                print("key:" + k)
                print("value:")
                print(v)
        print("These are key_list:")
        for i in self.key_list:
            print(i)
        print("print all!!!!! END")


    def get_value(self, key):
        print("now parameter is:" + key)
        n = 0
        for i in self.key_list:
            if i == key:
                print("found!")
                n = self.key_list.index(i)
                print("n:")
                print(n)
        return self.value_list[n]

    def get_picUrl(self, key):
        return self.get_value(key)['url']









