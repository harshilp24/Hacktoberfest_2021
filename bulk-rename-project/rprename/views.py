# -*- coding: utf-8 -*-
# rprename/views.py

"""This module provides the RP Renamer main window."""

from collections import deque
from pathlib import Path

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QFileDialog, QWidget

from .rename import Renamer

from .ui.window import Ui_Window

FILTERS = ";;".join(
    (
        "PNG Files (*.png)",
        "JPEG Files (*.jpeg)",
        "JPG Files (*.jpg)",
        "GIF Files (*.gif)",
        "Text Files (*.txt)",
        "Python Files (*.py)",
    )
)


class Window(QWidget, Ui_Window):
    def __init__(self):
        super().__init__()
        self._files = deque()
        self._filesCount = len(self._files)
        self._setupUI()
        self._connectSignalsSlots()

    def _setupUI(self):
        self.setupUi(self)
        self._updateStateWhenNoFiles()

    def _updateStateWhenNoFiles(self):
        self._filesCount = len(self._files)
        self.load_files_button.setEnabled(True)
        self.load_files_button.setFocus(True)
        self.rename_files_button.setEnabled(False)
        self.prefix_edit.clear()
        self.prefix_edit.setEnabled(False)

    def _connectSignalsSlots(self):
        self.load_files_button.clicked.connect(self.loadFiles)
        self.rename_files_button.clicked.connect(self.renameFiles)
        self.prefix_edit.textChanged.connect(self._updateStateWhenReady)

    def _updateStateWhenReady(self):
        if self.prefix_edit.text():
            self.rename_files_button.setEnabled(True)
        else:
            self.rename_files_button.setEnabled(False)

    def loadFiles(self):
        self.dst_files_list.clear()
        if self.dir_edit.text():
            initDir = self.dir_edit.text()
        else:
            initDir = str(Path.home())
        files, filter = QFileDialog.getOpenFileNames(
            self, "Choose Files to Rename", initDir, filter=FILTERS
        )
        if len(files) > 0:
            fileExtension = filter[filter.index("*"): -1]
            self.extension_label.setText(fileExtension)
            srcDirName = str(Path(files[0]).parent)
            self.dir_edit.setText(srcDirName)
            for file in files:
                self._files.append(Path(file))
                self.src_files_list.addItem(file)
            self._filesCount = len(self._files)
            self._updateStateWhenFilesLoaded()

    def _updateStateWhenFilesLoaded(self):
        self.prefix_edit.setEnabled(True)
        self.prefix_edit.setFocus(True)

    def renameFiles(self):
        self._runRenamerThread()
        self._updateStateWhileRenaming()

    def _updateStateWhileRenaming(self):
        self.load_files_button.setEnabled(False)
        self.rename_files_button.setEnabled(False)

    def _runRenamerThread(self):
        prefix = self.prefix_edit.text()
        self._thread = QThread()
        self._renamer = Renamer(
            files=tuple(self._files),
            prefix=prefix,
        )
        self._renamer.moveToThread(self._thread)
        # Rename
        self._thread.started.connect(self._renamer.renameFiles)
        # Update state
        self._renamer.renamedFile.connect(self._updateStateWhenFileRenamed)
        self._renamer.progressed.connect(self._updateProgressBar)
        self._renamer.finished.connect(self._updateStateWhenNoFiles)
        # Clean up
        self._renamer.finished.connect(self._thread.quit)
        self._renamer.finished.connect(self._renamer.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        # Run the thread
        self._thread.start()

    def _updateStateWhenFileRenamed(self, newFile):
        self._files.popleft()
        self.src_files_list.takeItem(0)
        self.dst_files_list.addItem(str(newFile))

    def _updateProgressBar(self, fileNumber):
        progressPercent = int(fileNumber / self._filesCount * 100)
        self.progressBar.setValue(progressPercent)
