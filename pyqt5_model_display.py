from PyQt5 import QtCore, QtGui, QtWidgets
import os
import qtawesome
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ReadHelper import ReadHelper

global global_fileContent
global global_modelTitle
global global_rh

global_fileContent = './dog.jpg'
global_modelTitle = ""
global_mat_type = ""
global_rh = None


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)  # prevents starttimer error
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

        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)

        self.top_left_button = QtWidgets.QPushButton("打开文件tst")
        self.top_left_button.setObjectName('top_label')
        self.right_bar_layout.addWidget(self.top_left_button, 1, 0, 1, 3)

        self.top_center_bg = QtWidgets.QToolButton()
        self.top_center_bg.setIconSize(QtCore.QSize(600, 27))  # 300, 200
        self.right_bar_layout.addWidget(self.top_center_bg, 0, 5)

        self.top_center = QtWidgets.QLabel("")
        self.top_center.setObjectName('mid_label')
        self.right_bar_layout.addWidget(self.top_center, 0, 0)

        self.top_right_button = QtWidgets.QPushButton("保存与退出")
        self.top_right_button.setIconSize(QtCore.QSize(30, 27))  # 300, 200
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

        # LOWER RIGHT SECTION

        self.right_playlist_widget = QtWidgets.QWidget()
        self.right_playlist_layout = QtWidgets.QGridLayout()
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        self.lower_right_label = QtWidgets.QLabel("      材料类型:" + global_mat_type)
        self.lower_right_label.setObjectName('right_lable')
        print(global_mat_type)

        self.lower_right_button_1 = QtWidgets.QPushButton("选择")
        self.lower_right_button_1.setObjectName('left_label')
        self.right_layout.addWidget(self.lower_right_button_1, 6, 7, 1, 1)

        self.lower_right_bg = QtWidgets.QToolButton()
        self.lower_right_bg.setIconSize(QtCore.QSize(350, 200))  # 300, 200

        self.lower_right_icon = QtWidgets.QToolButton()
        self.lower_right_icon.setIcon(QtGui.QIcon(global_fileContent))  # 设置按钮图标
        self.lower_right_icon.setIconSize(QtCore.QSize(180, 200))  # 设置图标大小

        self.right_playlist_layout.addWidget(self.lower_right_bg, 0, 0)
        self.right_playlist_layout.addWidget(self.lower_right_icon, 0, 0)

        self.right_layout.addWidget(self.right_playlist_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        self.right_layout.addWidget(self.lower_right_label, 5, 7, 1, 1)
        self.right_layout.addWidget(self.lower_right_button_1, 6, 7, 1, 1)

        self.tree_widget = QTreeWidget(self)
        self.left_layout.addWidget(self.tree_widget, 5, 0, 1, 3)
        self.tree_widget.header().setVisible(False)

        # CONNECT FUNCTION PART

        self.lower_right_button_1.pressed.connect(self.selectMaterial)
        self.top_left_button.pressed.connect(self.openFileNamesDialog)
        self.tree_widget.itemClicked['QTreeWidgetItem*', 'int'].connect(self.tree_item_click)
        # # 其中tree_item_click是自己定义的槽函数

        self.show()

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
            self.top_center = QtWidgets.QLabel.clear(self.top_center)
            self.top_center = QtWidgets.QLabel(rh.path)  # create
            self.top_center.setObjectName('mid_label')  # setParameter
            self.right_bar_layout.addWidget(self.top_center, 0, 0)


            self.lower_mid_label = QtWidgets.QLabel(global_modelTitle)

            self.lower_mid_label.setObjectName('middle_label')
            self.right_layout.addWidget(self.lower_mid_label, 4, 2, 1, 1)

            # clear last time
            QtWidgets.QLabel.clear(self.lower_mid_label_2)
            # QtWidgets.QTreeWidget.clear(self.tree_widget)  # QTreeWidgetItem object: root

            self.tree_widget = QTreeWidget(self)
            self.left_layout.addWidget(self.tree_widget, 5, 0, 1, 3)
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
            self.right_layout.addWidget(self.lower_mid_label_2, 5, 2, 1, 1)

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


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    import sys

    main()