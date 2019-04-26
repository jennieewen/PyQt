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

    def get_value(self, key):
        for i in self.key_list:
            if i == key:
                n = self.key_list.index(i)
        return self.value_list[n]

    def get_picUrl(self, key):
        return self.get_value(key)['url']







