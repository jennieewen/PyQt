#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
new UI
Authors: Jennieewen & wmxl
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

        # 顶部 打开文件和地址栏
        self.button_open = QPushButton("打开FBX模型文件")
        self.button_open.setObjectName("open")
        self.path_edit = QLineEdit()
        self.path_edit.setObjectName("path")
        self.button_exit = QPushButton("保存并退出")
        self.button_exit.setObjectName("exit")

        self.h_box1 = QHBoxLayout()
        self.h_box1.addWidget(self.button_open)
        self.h_box1.addStretch(1)
        self.h_box1.addWidget(self.path_edit, 50)
        self.h_box1.addStretch(1)
        self.h_box1.addWidget(self.button_exit)

        self.h_box2 = QHBoxLayout()
        self.g_tree = QHBoxLayout()
        self.h_box2.addLayout(self.g_tree)

        self.tree_widget = QTreeWidget(self)
        self.tree_widget.setObjectName("tree")
        self.tree_widget.header().setVisible(False)
        self.g_tree.addWidget(self.tree_widget)
        self.g_tree.addStretch(1)

        self.v_box = QVBoxLayout()

        # large picture part - start
        self.lg_pic = QToolButton()
        self.lg_pic.setIcon(QtGui.QIcon("./bird.jpg"))
        self.lg_pic.setIconSize(QtCore.QSize(873, 450))

        self.g_lg_pic = QGridLayout()
        self.g_lg_pic_widget = QWidget()
        self.g_lg_pic_widget.setObjectName("lg_pic_layout")
        self.g_lg_pic_widget.setLayout(self.g_lg_pic)

        self.v_box.addWidget(self.g_lg_pic_widget)
        self.g_lg_pic.addWidget(self.lg_pic)
        self.h_box2.addLayout(self.v_box)
        # large picture part - end

        self.h_bottom_box = QHBoxLayout()
        self.v_box.addLayout(self.h_bottom_box)

        # BOTTOM PART STRUCTURE - START
        self.v_bottom_box_left = QVBoxLayout()
        self.v_bottom_box_left_widget = QWidget()
        self.v_bottom_box_left_widget.setLayout(self.v_bottom_box_left)

        self.g_bottom_box_right = QGridLayout()
        self.g_bottom_box_right_widget = QWidget()
        self.g_bottom_box_right_widget.setObjectName("right_layout")
        self.g_bottom_box_right_widget.setLayout(self.g_bottom_box_right)

        self.h_bottom_box.addWidget(self.v_bottom_box_left_widget)
        self.h_bottom_box.addWidget(self.g_bottom_box_right_widget)
        # BOTTOM PART STRUCTURE - END

        # MODEL NAME AND INFO PART - START
        self.g_model_name = QGridLayout()
        self.g_model_name_widget = QWidget()
        self.g_model_name_widget.setObjectName("top_layout")
        self.g_model_name_widget.setLayout(self.g_model_name)

        self.g_model_info = QGridLayout()
        self.g_model_info_widget = QWidget()
        self.g_model_info_widget.setObjectName("bottom_layout")
        self.g_model_info_widget.setLayout(self.g_model_info)

        self.v_bottom_box_left.addWidget(self.g_model_name_widget)
        self.v_bottom_box_left.addWidget(self.g_model_info_widget)

        self.sub_model_name = QtWidgets.QLabel('      模型子物体名称 :')
        self.sub_model_name.setObjectName("text_label")
        self.sub_model_name_name = QtWidgets.QLabel("a.txtxtxt")
        self.sub_model_name_name.setObjectName("label_name")

        self.sub_model_infos = QtWidgets.QLabel('         子物体贴图信息 :')
        self.sub_model_infos.setObjectName("text_label_2")
        self.sub_model_info_info = QtWidgets.QLabel("sdffsdfsfsfsdfsdfsdfds"
                                                    "sdfsfdfsdfsdfsdfsdfdsfd")
        self.sub_model_info_info.setObjectName("info_name")

        self.g_model_name.addWidget(self.sub_model_name, 0, 0, 1, 1)
        self.g_model_name.addWidget(self.sub_model_name_name, 0, 1, 1, 1)

        self.g_model_info.addWidget(self.sub_model_infos, 0, 0, 1, 1)
        self.g_model_info.addWidget(self.sub_model_info_info, 0, 1, 1, 1)


        # 选择材质 模块

        self.lower_right_icon = QtWidgets.QToolButton()
        self.lower_right_icon.setIcon(QtGui.QIcon('./cat.jpg'))  # 设置按钮图标
        self.lower_right_icon.setIconSize(QtCore.QSize(180, 180))  # 设置图标大小
        self.g_bottom_box_right.addWidget(self.lower_right_icon)

        self.h_bottom_box.addWidget(self.g_bottom_box_right_widget)
        self.lower_right_label = QtWidgets.QLabel("      材质类型 :")
        self.lower_right_label.setObjectName("text_label")
        self.lower_right_label_detail = QtWidgets.QLabel("bear")
        self.lower_right_label_detail.setObjectName("text_label_detail")
        self.button_choose = QtWidgets.QPushButton("选 择")
        self.button_choose.setObjectName("choose")

        self.g_bottom_box_right.addWidget(self.lower_right_icon, 0, 0, 3, 1)
        self.g_bottom_box_right.addWidget(self.lower_right_label, 0, 1, 1, 1)
        self.g_bottom_box_right.addWidget(self.lower_right_label_detail, 1, 1, 1, 1)
        self.g_bottom_box_right.addWidget(self.button_choose, 2, 1, 1, 1)


        with open('./style_bottom.qss', 'r') as f:
            self.g_bottom_box_right_widget.setStyleSheet(f.read())

        with open('./style_bottom.qss', 'r') as f:
            self.v_bottom_box_left_widget.setStyleSheet(f.read())

        # 主要布局设置
        self.h_box1_widget = QtWidgets.QWidget()
        self.h_box1_widget.setLayout(self.h_box1)
        self.main_box = QVBoxLayout()
        self.main_box.addWidget(self.h_box1_widget)
        self.main_box.addLayout(self.h_box2)
        self.setLayout(self.main_box)



        # CONNECT FUNCTION PART

        self.button_open.pressed.connect(self.open_file_names_dialog)
        self.button_choose.pressed.connect(self.select_material)
        self.tree_widget.itemClicked['QTreeWidgetItem*', 'int'].connect(self.tree_item_click)
        # # 其中tree_item_click是自己定义的槽函数

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
            self.tree_widget.setObjectName("tree")
            self.g_tree.addWidget(self.tree_widget, 0, 0, 20, 200)
            self.tree_widget.header().setVisible(False)

            self.tree_widget.itemClicked['QTreeWidgetItem*', 'int'].connect(self.tree_item_click)
            # 其中tree_item_click是自己定义的槽函数

            key_list = rh.key_list
            print(key_list)

            # 取消自带的小箭头
            self.tree_widget.setRootIsDecorated(False)
            # 取消原来的选中蓝色效果
            self.tree_widget.setSelectionMode(QAbstractItemView.NoSelection)
            # 取消原来的选中框框
            self.tree_widget.setFocusPolicy(QtCore.Qt.NoFocus)
            # self.tree_widget.setFocusPolicy(False)  same effect as above line

            # 树的根节点
            self.root = QtWidgets.QTreeWidgetItem(self.tree_widget)  # QTreeWidgetItem object: self.root
            self.root.setIcon(0, QtGui.QIcon("icons/closed_folder.png"))
            self.root.setText(0, " " + rh.name + "                   ▾")  # set text of self.root
            col = QColor(0, 124, 176)  # 0 124 176 blue
            # col.setNamedColor("#fff")
            self.root.setBackground(0, col)
            self.root.setSizeHint(0, QtCore.QSize(45, 45))

            self.child = []
            for i in range(len(key_list)):
                child_ = QtWidgets.QTreeWidgetItem(self.root)  # child of root
                child_.setText(0, "    " + key_list[i])
                child_.setFont(0, QtGui.QFont("Microsoft YaHei", 10))
                child_.setSizeHint(0, QtCore.QSize(45, 45))
                # print(child_)
                self.child.append(child_)

    '''choose tree_item function'''
    def tree_item_click(self, item, n):
        # 把上次的颜色恢复成白色
        for c in self.child:
            col = QColor(255, 255, 255)
            c.setForeground(0, col)
        # 如果当前item是root
        if item == self.root:
            print("root")
            if item.isExpanded():
                self.tree_widget.collapseItem(item)
                self.root.setIcon(0, QtGui.QIcon("icons/closed_folder.png"))
                self.root.setText(0, " " + global_rh.name + "                   ▾")
            else:
                self.tree_widget.expandItem(item)
                self.root.setIcon(0, QtGui.QIcon("icons/open_folder.png"))
                self.root.setText(0, " " + global_rh.name + "                   ▴")
        # 如果当前item是孩子节点
        else:
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
                details += "\n"
                # print("kv: " + k, v)
                if flag:
                    flag = False
                else:
                    pass
                details += k
                details += ' : '
                details += v

            print(details)
            self.sub_model_info_info.setText(details)

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
        self.lower_right_label.setText("      材质类型 : ")

        self.lower_right_label_detail.setText("         " + file_name)

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

