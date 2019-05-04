#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
new UI
Author: wmxl
Last edited: April 30 2019
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
import os
from ReadHelper import ReadHelper


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)  # prevents starttimer error
        self.setFixedSize(1200, 800)

        self.button_open = QPushButton("打开FBX模型文件")
        self.path_edit = QLineEdit()
        # self.path_edit.setDisabled(True) # 无法选中和编辑

        self.b3 = QPushButton("保存并退出")

        self.h_box1 = QHBoxLayout()
        # self.h_box1.addStretch(1)
        self.h_box1.addWidget(self.button_open)
        self.h_box1.addStretch(1)
        self.h_box1.addWidget(self.path_edit, 8)
        self.h_box1.addStretch(1)
        self.h_box1.addWidget(self.b3)
        # self.h_box1.addStretch(1)

        self.h_box2 = QHBoxLayout()
        self.g_tree = QtWidgets.QGridLayout()
        self.h_box2.addLayout(self.g_tree)

        self.v_box = QVBoxLayout()

        self.lg_pic = QtWidgets.QToolButton()
        self.lg_pic.setIcon(QtGui.QIcon("./bird.jpg"))  # 设置按钮图标
        self.lg_pic.setIconSize(QtCore.QSize(900, 450))
        self.v_box.addWidget(self.lg_pic)

        self.h_box2.addLayout(self.v_box)

        self.h_bottom_box = QHBoxLayout()
        self.v_box.addLayout(self.h_bottom_box)

        self.v_bottom_box_right = QVBoxLayout()
        self.v_bottom_box_left = QVBoxLayout()

        self.h_bottom_box.addLayout(self.v_bottom_box_left)

        self.sub_model_name = QtWidgets.QLabel("""    
        
        模型子物体名称:""")
        self.sub_model_infos = QtWidgets.QLabel("""   
        
        子物体贴图信息:""")
        # self.v_bottom_box_left.addStretch(1)
        self.v_bottom_box_left.addWidget(self.sub_model_name)
        # self.v_bottom_box_left.addStretch(1)
        self.v_bottom_box_left.addWidget(self.sub_model_infos)
        self.v_bottom_box_left.addStretch(7)

        # 选择材质 模块

        self.lower_right_icon = QtWidgets.QToolButton()
        self.lower_right_icon.setIcon(QtGui.QIcon('./cat.jpg'))  # 设置按钮图标
        self.lower_right_icon.setIconSize(QtCore.QSize(220, 220))  # 设置图标大小
        self.h_bottom_box.addWidget(self.lower_right_icon)

        self.h_bottom_box.addLayout(self.v_bottom_box_right)
        self.lower_right_label = QtWidgets.QLabel("      材质类型:")
        self.v_bottom_box_right.addStretch(2)
        self.v_bottom_box_right.addWidget(self.lower_right_label)
        self.v_bottom_box_right.addStretch(11)
        self.button_choose = QtWidgets.QPushButton("选择")
        self.v_bottom_box_right.addWidget(self.button_choose)
        self.v_bottom_box_right.addStretch(2)

        self.main_box = QVBoxLayout()
        # main_box.addStretch(1)
        self.main_box.addLayout(self.h_box1)
        # main_box.addStretch(1)
        self.main_box.addLayout(self.h_box2)
        # main_box.addStretch(1)
        self.setLayout(self.main_box)

        self.tree_widget = QTreeWidget(self)
        self.g_tree.addWidget(self.tree_widget, 5, 0, 1, 2)
        self.tree_widget.header().setVisible(False)

        # CONNECT FUNCTION PART

        self.button_choose.pressed.connect(self.select_material)
        self.button_open.pressed.connect(self.open_file_names_dialog)
        self.tree_widget.itemClicked['QTreeWidgetItem*', 'int'].connect(self.tree_item_click)
        # # 其中tree_item_click是自己定义的槽函数

        self.show()

    '''open file function'''
    def open_file_names_dialog(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)

        # str_path = ""
        if files:
            str_path = ''.join(files)
            _, file_name = os.path.split(str_path)
            print(str_path)

            rh = ReadHelper(str_path)
            global global_rh
            global_rh = rh

            self.path_edit.setText(str_path)

            QtWidgets.QTreeWidget.clear(self.tree_widget)  # clear last time

            self.tree_widget = QTreeWidget(self)
            self.g_tree.addWidget(self.tree_widget, 5, 0, 1, 3)
            self.tree_widget.header().setVisible(False)

            self.tree_widget.itemClicked['QTreeWidgetItem*', 'int'].connect(self.tree_item_click)
            # 其中tree_item_click是自己定义的槽函数

            key_list = rh.key_list
            print(key_list)

            root = QtWidgets.QTreeWidgetItem(self.tree_widget)  # QTreeWidgetItem object: root
            root.setText(0, rh.name)  # set text of root

            for i in range(len(key_list)):
                child = QtWidgets.QTreeWidgetItem(root)  # child of root
                child.setText(0, key_list[i])

    '''choose tree_item function'''
    def tree_item_click(self, item, n):
        global global_rh
        it = item.text(n)
        print(it)
        # file name
        self.sub_model_name.setText("""    
        
        模型子物体名称 : """ + it)
        values = global_rh.get_value(it)
        print(values)
        details = """    
        
        子物体贴图信息 : """
        flag = True
        for k, v in values.items():
            print(k, v)
            if flag:
                flag = False
            else:
                details += """ 
                                  """
            details += k
            details += ' : '
            details += v

        print(details)
        self.sub_model_infos.setText(details)

    '''select material function'''
    def select_material(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        str_path = file_name = ""
        if files:
            str_path = ''.join(files)
            _, file_name = os.path.split(str_path)

        self.lower_right_icon.setIcon(QtGui.QIcon(str_path))  # 设置按钮图标
        self.lower_right_label.setText('''      材质类型: 
        ''' + file_name)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())