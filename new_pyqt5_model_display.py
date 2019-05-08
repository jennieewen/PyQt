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
from PyQt5.QtGui import QPainter, QColor, QBrush


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)  # prevents starttimer error
        self.setFixedSize(1200, 800)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        self.button_open = QPushButton("打开FBX模型文件")
        self.button_open.setObjectName("open")
        self.path_edit = QLineEdit()
        self.path_edit.setObjectName("path")
        # self.path_edit.setDisabled(True) # 无法选中和编辑
        self.button_exit = QPushButton("保存并退出")
        self.button_exit.setObjectName("exit")

        self.h_box1 = QHBoxLayout()
        # self.h_box1.addStretch(1)
        self.h_box1.addWidget(self.button_open)
        self.h_box1.addStretch(1)
        self.h_box1.addWidget(self.path_edit, 50)
        self.h_box1.addStretch(1)
        self.h_box1.addWidget(self.button_exit)
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

        self.h_bottom_box_right = QHBoxLayout()
        self.v_bottom_box_left = QVBoxLayout()
        self.h_bottom_box_right_widget = QtWidgets.QWidget()
        self.v_bottom_box_left_widget = QtWidgets.QWidget()
        self.h_bottom_box_right_widget.setLayout(self.h_bottom_box_right)
        self.v_bottom_box_left_widget.setLayout(self.v_bottom_box_left)


        self.h_bottom_box.addWidget(self.v_bottom_box_left_widget)

        self.sub_model_name = QtWidgets.QLabel("    模型子物体名称:")
        self.sub_model_name.setObjectName("text_label")

        self.sub_model_name_name = QtWidgets.QLabel("")

        self.sub_model_name_name.setObjectName("label_name")

        self.sub_model_infos = QtWidgets.QLabel(""" 
        
        子物体贴图信息:""")

        self.sub_model_infos.setObjectName("text_label")

        self.sub_model_info_info = QtWidgets.QLabel("")
        self.sub_model_info_info.setObjectName("info_name")

        # 名称信息 模块

        self.h_bottom_box_left_modelname = QHBoxLayout()

        # self.v_bottom_box_left.addStretch(1)
        self.v_bottom_box_left.addLayout(self.h_bottom_box_left_modelname)
        self.h_bottom_box_left_modelname.addWidget(self.sub_model_name)
        self.h_bottom_box_left_modelname.addWidget(self.sub_model_name_name)

        self.h_bottom_box_left_modelinfo = QHBoxLayout()
        # self.v_bottom_box_left.addStretch(1)
        self.v_bottom_box_left.addLayout(self.h_bottom_box_left_modelinfo)
        self.h_bottom_box_left_modelinfo.addWidget(self.sub_model_infos)
        self.h_bottom_box_left_modelinfo.addWidget(self.sub_model_info_info)
        self.v_bottom_box_left.addStretch(7)

        # 选择材质 模块

        self.lower_right_icon = QtWidgets.QToolButton()
        self.lower_right_icon.setIcon(QtGui.QIcon('./cat.jpg'))  # 设置按钮图标
        self.lower_right_icon.setIconSize(QtCore.QSize(180, 180))  # 设置图标大小
        self.h_bottom_box_right.addWidget(self.lower_right_icon)

        self.h_bottom_box.addWidget(self.h_bottom_box_right_widget)
        self.lower_right_label = QtWidgets.QLabel("      材质类型:")
        self.lower_right_label.setObjectName("text_label")

        self.v_bottom_box_right = QVBoxLayout()
        self.h_bottom_box_right.addLayout(self.v_bottom_box_right)

        self.v_bottom_box_right.addStretch(2)
        self.v_bottom_box_right.addWidget(self.lower_right_label)
        self.v_bottom_box_right.addStretch(11)
        self.button_choose = QtWidgets.QPushButton("选 择")
        self.button_choose.setObjectName("choose")
        self.v_bottom_box_right.addWidget(self.button_choose)
        self.v_bottom_box_right.addStretch(2)

        with open('./style_bottom.qss', 'r') as f:
            self.h_bottom_box_right_widget.setStyleSheet(f.read())

        with open('./style_bottom.qss', 'r') as f:
            self.v_bottom_box_left_widget.setStyleSheet(f.read())

        self.h_box1_widget = QtWidgets.QWidget()
        self.h_box1_widget.setLayout(self.h_box1)
        self.main_box = QVBoxLayout()
        # main_box.addStretch(1)
        self.main_box.addWidget(self.h_box1_widget)
        # main_box.addStretch(1)
        self.main_box.addLayout(self.h_box2)
        # main_box.addStretch(1)
        self.setLayout(self.main_box)

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setObjectName("tree")

        self.tree_widget_header = self.tree_widget.header()
        self.tree_widget_header.setVisible(False)
        self.g_tree.addWidget(self.tree_widget, 5, 0, 1, 2)

        # test tree style (need delete later)

        str_path = "./a.txt"
        rh = ReadHelper(str_path)
        global global_rh
        global_rh = rh
        key_list = rh.key_list
        # print(key_list)

        self.root = QtWidgets.QTreeWidgetItem(self.tree_widget)  # QTreeWidgetItem object: self.root
        self.root.setIcon(0, QtGui.QIcon("./bear.jpg"))

        self.root.setText(0, rh.name)  # set text of self.root
        col = QColor(0, 124, 176)  # 0 124 176 blue
        # col.setNamedColor("#fff")
        self.root.setBackground(0, col)
        # col.setNamedColor("#")

        # print(self.root)

        self.child = []

        for i in range(len(key_list)):
            child_ = QtWidgets.QTreeWidgetItem(self.root)  # child of root
            child_.setText(0, key_list[i])
            # print(child_)
            self.child.append(child_)


        # test tree style end

        # CONNECT FUNCTION PART
        self.button_open.pressed.connect(self.open_file_names_dialog)
        self.tree_widget.itemClicked['QTreeWidgetItem*', 'int'].connect(self.tree_item_click)
        # # 其中tree_item_click是自己定义的槽函数
        self.tree_widget.itemSelectionChanged.connect(self.tree_item_change)
        self.tree_widget.setRootIsDecorated(False)

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

            self.root = QtWidgets.QTreeWidgetItem(self.tree_widget)  # QTreeWidgetItem object: root
            self.root.setText(0, rh.name)  # set text of root

            for i in range(len(key_list)):
                child = QtWidgets.QTreeWidgetItem(self.root)  # child of root
                child.setText(0, key_list[i])

    '''choose tree_item function'''
    def tree_item_click(self, item, n):
        if item == self.root:
            print("root")
            if item.isExpanded():
                self.tree_widget.collapseItem(item)
            else:
                self.tree_widget.expandItem(item)
        else:
            global global_rh
            # print(n)
            it = item.text(n)
            # print(item)
            col = QColor(0, 124, 176)  # 0 124 176 blue
            item.setForeground(0, col)

            # file name
            self.sub_model_name_name.setText(it)
            values = global_rh.get_value(it)
            # print(values)
            details = ''
            flag = True
            for k, v in values.items():
                # print(k, v)
                if flag:
                    flag = False
                else:
                    details += """ 
                                      """
                details += k
                details += ' : '
                details += v

            # print(details)
            self.sub_model_info_info.setText(details)

    '''select change function'''
    def tree_item_change(self):
        print("select change")
        for c in self.child:
            col = QColor(25, 25, 5)
            col.setNamedColor("#fff")
            c.setForeground(0, col)
            # c.set

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

    def on_button_click(self):
        q = QApplication.instance()
        q.quit()

    # 支持窗口拖动,重写两个方法
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and QtCore.Qt.LeftButton:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

    '''read qss file'''
    @staticmethod
    def read_qss(style):
        with open(style, 'r') as f:
            return f.read()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    style_sheet = ex.read_qss('./style.qss')
    ex.setStyleSheet(style_sheet)
    ex.show()
    sys.exit(app.exec_())