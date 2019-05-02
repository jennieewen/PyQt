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

        self.b1 = QPushButton("open")
        self.b2 = QPushButton("file path name")
        self.b3 = QPushButton("save and exit")
        self.b4 = QPushButton("tree")

        self.h_box1 = QHBoxLayout()
        # h_box1.addStretch(1)
        self.h_box1.addWidget(self.b1)
        self.h_box1.addWidget(self.b2)
        self.h_box1.addWidget(self.b3)

        self.h_box2 = QHBoxLayout()
        self.g_tree = QtWidgets.QGridLayout()
        self.h_box2.addLayout(self.g_tree)

        self.v_box = QVBoxLayout()

        self.lg_pic = QtWidgets.QToolButton()
        self.lg_pic.setIcon(QtGui.QIcon("./cat.jpg"))  # 设置按钮图标
        self.lg_pic.setIconSize(QtCore.QSize(800, 400))
        self.v_box.addWidget(self.lg_pic)

        self.h_box2.addLayout(self.v_box)

        self.h_bottom_box = QHBoxLayout()
        self.v_box.addLayout(self.h_bottom_box)

        self.v_bottom_box_right = QVBoxLayout()

        self.lower_mid_label = QtWidgets.QLabel("   模型子物体名称:" )
        self.lower_mid_label.setObjectName('middle_label')

        self.lower_mid_label_2 = QtWidgets.QLabel("   子物体贴图信息:")
        self.lower_mid_label_2.setObjectName('mid_label')

        self.h_bottom_box.addWidget(self.lower_mid_label)
        self.h_bottom_box.addWidget(self.lower_mid_label_2)

        self.lower_right_icon = QtWidgets.QToolButton()
        self.lower_right_icon.setIcon(QtGui.QIcon('./bear.jpg'))  # 设置按钮图标
        self.lower_right_icon.setIconSize(QtCore.QSize(180, 200))  # 设置图标大小
        self.h_bottom_box.addWidget(self.lower_right_icon)

        self.h_bottom_box.addLayout(self.v_bottom_box_right)
        self.lower_right_label = QtWidgets.QLabel("      材料类型:")
        self.v_bottom_box_right.addStretch(2)
        self.v_bottom_box_right.addWidget(self.lower_right_label)
        self.v_bottom_box_right.addStretch(5)
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
        self.g_tree.addWidget(self.tree_widget, 0, 0, 1, 2)
        self.tree_widget.header().setVisible(False)

        # CONNECT FUNCTION PART

        self.button_choose.pressed.connect(self.selectMaterial)
        self.b1.pressed.connect(self.openFileNamesDialog)
        self.tree_widget.itemClicked['QTreeWidgetItem*', 'int'].connect(self.tree_item_click)
        # # 其中tree_item_click是自己定义的槽函数

        self.show()

    '''open file function'''
    def openFileNamesDialog(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print("files", files)
            str = ''.join(files)
            print(str)

            rh = ReadHelper(str)
            global global_rh
            global_rh = rh

            # print(filePath)
            # self.top_center = QtWidgets.QLabel.clear(self.top_center)
            self.top_center = QtWidgets.QLabel(rh.path)  # create
            self.top_center.setObjectName('mid_label')  # setParameter
            # self.right_bar_layout.addWidget(self.top_center, 0, 0)

            # self.lower_mid_label = QtWidgets.QLabel(global_modelTitle)
            #
            # self.lower_mid_label.setObjectName('middle_label')
            # self.right_layout.addWidget(self.lower_mid_label, 4, 2, 1, 1)

            # clear last time
            QtWidgets.QLabel.clear(self.lower_mid_label_2)
            QtWidgets.QTreeWidget.clear(self.tree_widget)  # QTreeWidgetItem object: root

            self.tree_widget = QTreeWidget(self)
            self.g_tree.addWidget(self.tree_widget, 5, 0, 1, 3)
            self.tree_widget.header().setVisible(False)

            self.tree_widget.itemClicked['QTreeWidgetItem*', 'int'].connect(self.tree_item_click)
            # 其中tree_item_click是自己定义的槽函数

            # QTreeWidget add data
            self.tree_widget.setAlternatingRowColors(True)

            key_list = rh.key_list
            print(key_list)

            root = QtWidgets.QTreeWidgetItem(self.tree_widget)  # QTreeWidgetItem object: root
            root.setText(0, rh.name)  # set text of root

            for i in range(len(key_list)):
                child = QtWidgets.QTreeWidgetItem(root)  # child of root
                child.setText(0, key_list[i])

            # "   子物体贴图信息:"
            self.lower_mid_label_2 = QtWidgets.QLabel("   子物体贴图信息:")
            self.lower_mid_label_2.setObjectName('mid_label')
            # self.right_layout.addWidget(self.lower_mid_label_2, 5, 2, 1, 1)

    '''choose tree_item function'''
    def tree_item_click(self, item, n):
        global global_rh
        it = item.text(n)
        print(it)
        # file name
        self.lower_mid_label.setText("   模型子物体名称: " + it)
        values = global_rh.get_value(it)
        print(values)
        details = "   子物体贴图信息:\n"
        for k, v in values.items():
            print(k, v)
            details += "   "
            details += k
            details += ' : '
            details += v
            details += '\n'
        print(details)
        self.lower_mid_label_2.setText(details)

        # change pic
        self.lg_pic.setIcon(QtGui.QIcon(global_rh.get_value(it)['url']))

    '''select material function'''
    def selectMaterial(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)

        if files:
            str = ''.join(files)
            _, fileName = os.path.split(str)

        # setting icon for material
        global global_fileContent
        global_fileContent = './' + fileName
        self.lower_right_icon.setIcon(QtGui.QIcon(global_fileContent))

        # setting file path for material type
        self.lower_right_label = QtWidgets.QLabel.clear(self.lower_right_label)
        global global_mat_type
        global_mat_type = fileName
        self.lower_right_label = QtWidgets.QLabel("      材料类型: \n" + "     " + global_mat_type)
        self.lower_right_label.setObjectName('right_lable')
        self.right_layout.addWidget(self.lower_right_label, 5, 7, 1, 1)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())