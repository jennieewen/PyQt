from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import qtawesome

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(1200,800)
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

        self.main_layout.addWidget(self.left_widget,0,0,12,2)
        self.main_layout.addWidget(self.right_widget,0,5,12,10)
        self.setCentralWidget(self.main_widget)

        # next part

        self.left_label_1 = QtWidgets.QComboBox()
        self.left_label_1.setObjectName('left_label')
        self.left_label_1.addItem("A")
        self.left_label_1.addItem("B")
        self.left_label_1.addItems(["C", "D", "E"])

        self.left_label_2 = QtWidgets.QPushButton("我的音乐")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='white'), "华语流行")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), "在线FM")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film', color='white'), "热门MV")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), "本地音乐")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.download', color='white'), "下载管理")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "我的收藏")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "遇到问题")
        self.left_button_9.setObjectName('left_button')

        #search bar
        self.left_top_button = QtWidgets.QPushButton("打开文件")
        self.right_bar_widget = QtWidgets.QWidget()
        self.right_bar_layout = QtWidgets.QGridLayout()
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.left_layout.addWidget(self.left_top_button, 0, 0, 1, 3)


        self.top_center_bg = QtWidgets.QToolButton()
        self.top_center_bg.setIconSize(QtCore.QSize(600, 27))  # 300, 200
        self.right_bar_layout.addWidget(self.top_center_bg, 0, 0)


        self.top_center = QtWidgets.QLabel(" FILE NAME HERE")
        self.top_center.setObjectName('mid_label')
        self.right_bar_layout.addWidget(self.top_center, 0,0)


        self.top_right_button = QtWidgets.QPushButton("保存与退出")
        self.top_right_button.setObjectName('top_label')
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.right_bar_layout.addWidget(self.top_right_button, 0, 7, 0, 3)

        self.right_bar_widget_search_input = QtWidgets.QLabel()
        self.right_layout.addWidget(self.right_bar_widget_search_input, 5, 7, 1, 1)





        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)


        self.left_layout.addWidget(self.left_top_button, 0, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)





        self.right_recommend_widget = QtWidgets.QWidget()
        self.right_recommend_layout = QtWidgets.QGridLayout()
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.lg_pic = QtWidgets.QToolButton()
        self.lg_pic.setIcon(QtGui.QIcon('./dog.jpg'))
        self.lg_pic.setIconSize(QtCore.QSize(800, 400))

        self.mat_type_pic = QtWidgets.QToolButton()
        self.mat_type_pic.setText("猎场合辑")
        self.mat_type_pic.setIcon(QtGui.QIcon('./sq.jpg'))
        self.mat_type_pic.setIconSize(QtCore.QSize(100, 100))
        self.mat_type_pic.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_recommend_layout.addWidget(self.lg_pic, 0, 0)

        self.right_recommend_layout.addWidget(self.mat_type_pic, 0, 0)

        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)



        # LOWER MID

        self.lower_mid_widget = QtWidgets.QWidget()
        self.lower_mid_layout = QtWidgets.QGridLayout()
        self.lower_mid_widget.setLayout(self.lower_mid_layout)

        self.lower_mid_label = QtWidgets.QLabel("   模型子物体名称:")
        self.lower_mid_label.setObjectName('mid_label')

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
        self.lower_right_bg.setIconSize(QtCore.QSize(350, 200)) # 300, 200

        self.lower_right_icon = QtWidgets.QToolButton()
        self.lower_right_icon.setIcon(QtGui.QIcon('./sq.jpg'))
        self.lower_right_icon.setIconSize(QtCore.QSize(180, 200))

        self.right_playlist_layout.addWidget(self.lower_right_bg, 0, 0)
        self.right_playlist_layout.addWidget(self.lower_right_icon, 0, 0)


        self.right_layout.addWidget(self.right_playlist_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        self.right_layout.addWidget(self.lower_right_label, 5, 7, 1, 1)
        self.right_layout.addWidget(self.lower_right_button_1, 6, 7, 1, 1)









def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()