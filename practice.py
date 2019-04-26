from PyQt5 import QtCore, QtGui, QtWidgets

import os
import qtawesome

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QFileDialog

global global_fileContent
global global_modelTitle
global global_filepath

global_fileContent = './dog.jpg'
global_modelTitle = ""
global_filepath = 'C:/Users/jenni/Desktop/python/projects/school_project/appFolder/a.txt'


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)  # prevents starttimer error

    def initUi(self):

        self.setFixedSize(1200, 800)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)

        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 2, 0, 12, 3)
        self.main_layout.addWidget(self.right_widget, 1, 5, 12, 10)
        self.setCentralWidget(self.main_widget)

        self.treeview = QTreeView(self)
        # self.treeview.setModel(QStandardItemModel)
        # self.treeview.route.connect(self.route)
        self.left_layout.addWidget(self.treeview, 5, 0, 1, 3)
        self.treeview.header().setVisible(False)

        self.treeview.doubleClicked.connect(self.treeview_Clicked)

        ''' 
        importFile = global_filepath
        _, importFileDisplay = os.path.split(importFile)

        self.model = QStandardItemModel()
        self.rootNode = self.model.invisibleRootItem()
        self.branch1 = QStandardItem(importFileDisplay)
        self.branch2 =QStandardItem(importFileDisplay)

       # self.lower_mid_label = QtWidgets.QLabel("   模型子物体名称:" + global_modelTitle)
       # self.lower_mid_label.setObjectName('middle_label')



        #self.right_layout.addWidget(self.lower_mid_label, 4, 2, 1, 1)
        '''

        '''
        self.model = QStandardItemModel()
        self.rootNode = self.model.invisibleRootItem()

        self.branch1 = QtWidgets.QLabel(global_modelTitle)
        self.branch1.setObjectName('middle_label')
        self.rootNode.appendRow([self.branch1, None])
        '''
        '''self.rootNode.appendRow([self.branch1, None])
        self.rootNode.appendRow([self.branch2, None])

        self.treeview.setModel(self.model)
        self.treeview.setAlternatingRowColors(True)

        lst = []
        with open(importFile, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                score = line.split(":")
                lst.append(score)
                dict = {element[0]: element[1] for element in lst}
                print(dict)
            for k, v in dict.items():
                print("key", k)
                self.branch1.appendRow(([QStandardItem(k), None]))'''

        self.left_bar_bg = QtWidgets.QPushButton(qtawesome.icon('fa.angle-down', color='white'), "choose pic")
        self.left_bar_bg.setObjectName('left_button')
        self.left_layout.addWidget(self.left_bar_bg, 3, 0, 1, 3)
        self.left_bar_bg.pressed.connect(self.openFileNamesDialog)

        self.left_label_2 = QtWidgets.QPushButton("我的音乐")
        self.left_label_2.setObjectName('left_label')
        self.left_layout.addWidget(self.left_label_2, 2, 0, 1, 3)

        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')
        self.left_layout.addWidget(self.left_label_3, 4, 0, 1, 5)
        self.left_layout.addWidget(self.left_bar_bg, 0, 0)

        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)

        self.left_top_button = QtWidgets.QPushButton("打开文件")
        self.left_top_button.setObjectName('top_label')
        self.main_layout.addWidget(self.left_top_button, 1, 0, 1, 3)
        self.left_top_button.pressed.connect(self.openFileNamesDialog)

        self.top_center_bg = QtWidgets.QToolButton()
        self.top_center_bg.setIconSize(QtCore.QSize(600, 27))  # 300, 200
        self.right_bar_layout.addWidget(self.top_center_bg, 0, 0)

        self.top_center = QtWidgets.QLabel(" FILE NAME HERE")
        self.top_center.setObjectName('mid_label')
        self.right_bar_layout.addWidget(self.top_center, 0, 0)

        self.top_right_button = QtWidgets.QPushButton("保存与退出")
        self.top_right_button.setObjectName('top_label')
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.right_bar_layout.addWidget(self.top_right_button, 0, 7, 0, 3)
        self.right_bar_widget_search_input = QtWidgets.QLabel()
        self.right_layout.addWidget(self.right_bar_widget_search_input, 5, 7, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)
        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)
        self.lg_pic = QtWidgets.QToolButton()
        self.lg_pic.setIcon(QtGui.QIcon(global_fileContent))  # 设置按钮图标
        self.lg_pic.setIconSize(QtCore.QSize(800, 400))  # 设置图标大小

        self.right_recommend_layout.addWidget(self.lg_pic, 0, 0)

        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

        # fourth part - LOWER MID

        self.lower_mid_widget = QtWidgets.QWidget()  # 最新歌曲部件
        self.lower_mid_layout = QtWidgets.QGridLayout()  # 最新歌曲部件网格布局
        self.lower_mid_widget.setLayout(self.lower_mid_layout)

        self.lower_mid_label = QtWidgets.QLabel("   模型子物体名称:" + global_modelTitle)
        self.lower_mid_label.setObjectName('middle_label')

        self.lower_mid_label_2 = QtWidgets.QLabel("   子物体贴图信息:")
        self.lower_mid_label_2.setObjectName('mid_label')

        self.lower_mid_bg = QtWidgets.QToolButton()
        self.lower_mid_bg.setIconSize(QtCore.QSize(600, 400))  # 600, 200

        self.right_layout.addWidget(self.lower_mid_bg, 5, 2)

        self.right_layout.addWidget(self.lower_mid_widget, 3, 0, 1, 5)
        self.right_layout.addWidget(self.lower_mid_widget, 4, 3, 1, 4)

        self.right_layout.addWidget(self.lower_mid_label, 4, 2, 1, 1)
        self.right_layout.addWidget(self.lower_mid_label_2, 5, 2, 1, 1)

        # LOWER RIGHT SECTION

        self.right_playlist_widget = QtWidgets.QWidget()
        self.right_playlist_layout = QtWidgets.QGridLayout()
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        self.lower_right_label = QtWidgets.QLabel("材料类型")
        self.lower_right_label.setObjectName('right_lable')

        self.lower_right_button_1 = QtWidgets.QPushButton("选择")
        self.lower_right_button_1.setObjectName('left_label')

        self.lower_right_bg = QtWidgets.QToolButton()
        self.lower_right_bg.setIconSize(QtCore.QSize(350, 200))  # 300, 200

        self.lower_right_icon = QtWidgets.QToolButton()
        self.lower_right_icon.setIcon(QtGui.QIcon('./sq.jpg'))
        self.lower_right_icon.setIconSize(QtCore.QSize(180, 200))

        self.right_playlist_layout.addWidget(self.lower_right_bg, 0, 0)
        self.right_playlist_layout.addWidget(self.lower_right_icon, 0, 0)

        self.right_layout.addWidget(self.right_playlist_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        self.right_layout.addWidget(self.lower_right_label, 5, 7, 1, 1)
        self.right_layout.addWidget(self.lower_right_button_1, 6, 7, 1, 1)

        self.show()

    def OpenFileFullPathDiaglog(self):

        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print("files", files)
            str = ''.join(files)
            print(str)

            # File Path
            filePath = str
            print(filePath)
            self.top_center = QtWidgets.QLabel.clear(self.top_center)
            self.top_center = QtWidgets.QLabel(filePath)  # create
            self.top_center.setObjectName('mid_label')  # setParameter
            self.right_bar_layout.addWidget(self.top_center, 0, 0)

            # file path shortened
            _, fileName = os.path.split(str)

            # file name
            self.lower_mid_label = QtWidgets.QLabel.clear(self.lower_mid_label)

            global global_modelTitle
            global_modelTitle = "   模型子物体名称: " + fileName
            self.lower_mid_label = QtWidgets.QLabel(global_modelTitle)

            self.lower_mid_label.setObjectName('middle_label')
            self.right_layout.addWidget(self.lower_mid_label, 4, 2, 1, 1)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print("files", files)
            str = ''.join(files)
            print(str)

            # File Path
            filePath = str
            # print(filePath)
            self.top_center = QtWidgets.QLabel.clear(self.top_center)
            self.top_center = QtWidgets.QLabel(filePath)  # create
            self.top_center.setObjectName('mid_label')  # setParameter
            self.right_bar_layout.addWidget(self.top_center, 0, 0)

            # file path shortened
            _, fileName = os.path.split(str)

            # file name
            self.lower_mid_label = QtWidgets.QLabel.clear(self.lower_mid_label)

            global global_modelTitle
            global_modelTitle = "   模型子物体名称: " + fileName
            self.lower_mid_label = QtWidgets.QLabel(global_modelTitle)

            self.lower_mid_label.setObjectName('middle_label')
            self.right_layout.addWidget(self.lower_mid_label, 4, 2, 1, 1)

            # image file
            # self.lg_pic.setIcon(QtGui.QIcon('./'+fileName))
            global global_fileContent
            global_fileContent = './' + fileName;
            self.lg_pic.setIcon(QtGui.QIcon(global_fileContent))

            # entire path
            global global_filepath
            global_filepath = filePath
            # print("global filepath", global_filepath)
            self.get_dict()

    def get_dict(self):
        importFile = global_filepath
        _, importFileDisplay = os.path.split(importFile)

        self.model = QStandardItemModel()
        self.rootNode = self.model.invisibleRootItem()
        self.branch1 = QStandardItem(importFileDisplay)
        self.rootNode.appendRow([self.branch1, None])

        self.treeview.setModel(self.model)
        self.treeview.setAlternatingRowColors(True)
        self.lower_mid_label_2 = QtWidgets.QLabel.clear(self.lower_mid_label_2)

        lst = []
        with open(importFile, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                score = line.split(":")
                lst.append(score)
                dict1 = {element[0]: element[1] for element in lst}
            for k, v in dict1.items():
                # print("key", k, "value", v)
                self.branch1.appendRow(([QStandardItem(k), None]))
                print("POP", k)

            # global global_fileInfo
            global_fileInfo = "   子物体贴图信息:" + v
            # print("value", v)
            self.lower_mid_label_2 = QtWidgets.QLabel(global_fileInfo)
            self.lower_mid_label_2.setObjectName('mid_label')
            self.right_layout.addWidget(self.lower_mid_label_2, 5, 2, 1, 1)

            return dict1

    def treeview_Clicked(self):

        print("clicked")

    '''def treeview_Clicked(self, index):
        importFile = global_filepath
        _, importFileDisplay = os.path.split(importFile)

        self.model = QStandardItemModel()
        self.rootNode = self.model.invisibleRootItem()
        self.branch1 = QStandardItem(importFileDisplay)
        self.rootNode.appendRow([self.branch1, None])

        self.treeview.setModel(self.model)
        self.treeview.setAlternatingRowColors(True)
        self.lower_mid_label_2 = QtWidgets.QLabel.clear(self.lower_mid_label_2)
        lst = []
        with open(importFile, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                score = line.split(":")
                lst.append(score)
                dict = {element[0]: element[1] for element in lst}
                print(dict)
            for k, v in dict.items():
                self.branch1.appendRow(([QStandardItem(k), None]))
                print("k",k)
                print("v", v)
                print("line", line)
                print("score", score)
                if k == score[0]:
                        self.item = self.treeview.selectedIndexes()[::2]
                        print(self.item.model().itemFromIndex(index).text())


                global global_fileInfo
                global_fileInfo = "   子物体贴图信息:" + v
                print("value", v)
                self.lower_mid_label_2 = QtWidgets.QLabel(global_fileInfo)
                self.lower_mid_label_2.setObjectName('mid_label')
                self.right_layout.addWidget(self.lower_mid_label_2, 5, 2, 1, 1)

        print("treeview clicked")




        global_modelTitle = "   模型子物体名称: " + fileName
        self.lower_mid_label = QtWidgets.QLabel(global_modelTitle)

        self.lower_mid_label.setObjectName('middle_label')
        self.right_layout.addWidget(self.lower_mid_label, 4, 2, 1, 1)
        '''

    def get_value(self, key):
        importFile = global_filepath
        _, importFileDisplay = os.path.split(importFile)
        lst = []
        with open(importFile, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                score = line.split(":")
                lst.append(score)
                dict = {element[0]: element[1] for element in lst}

                # print(dict)
            for k, v in dict1.items():
                if key == k:
                    return v


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    import sys

    main()