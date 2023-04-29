#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description : Main file
@File        : main.py.py
@IDE         : PyCharm
@Date        : 29/4/2023 15:31
"""

from PyQt5 import QtCore, QtGui, QtWidgets

from src.search import search
from src.download import download

class MusicDownloader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        

    def init_ui(self):
        # Create widgets
        self.search_bar = QtWidgets.QLineEdit()
        self.search_button = QtWidgets.QPushButton("Search")
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Title', 'Author', 'Duration', 'Download'])
        self.previous_button = QtWidgets.QPushButton("Previous")
        self.next_button = QtWidgets.QPushButton("Next")

        # Set widget properties
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Create layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.search_bar)
        layout.addWidget(self.search_button)
        layout.addWidget(self.table)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.previous_button)
        button_layout.addWidget(self.next_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Connect signals and slots
        self.search_button.clicked.connect(self.search_music)
        self.previous_button.clicked.connect(self.previous_results)
        self.next_button.clicked.connect(self.next_results)

        # Initialize variables
        self.limit = 10
        self.offset = 0

    def search_music(self):
        query = self.search_bar.text()
        music = search(query, self.limit, self.offset)
        self.table.setRowCount(len(music))
        for row, data in enumerate(music):
            title_item = QtWidgets.QTableWidgetItem(data['title'])
            author_item = QtWidgets.QTableWidgetItem(data['author'])
            duration_item = QtWidgets.QTableWidgetItem(data['duration'])
            download_button = QtWidgets.QPushButton("Download")
            download_button.clicked.connect(lambda _, id=data['id'], data=data: self.download_music(id, data))
            self.table.setItem(row, 0, title_item)
            self.table.setItem(row, 1, author_item)
            self.table.setItem(row, 2, duration_item)
            self.table.setCellWidget(row, 3, download_button)

    def download_music(self, id, data):
        download(id, data)

    def previous_results(self):
        self.offset = max(0, self.offset - self.limit)
        self.search_music()

    def next_results(self):
        self.offset += self.limit
        self.search_music()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MusicDownloader()
    window.show()
    sys.exit(app.exec_())