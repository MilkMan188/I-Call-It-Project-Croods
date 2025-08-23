#!/usr/bin/env python3
from PySide6.QtWidgets import QApplication
from gui.gui import Widget
import os
import sys

app = QApplication(sys.argv)

gif_path = "img/phaesia_twerk2.gif"
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

window = Widget(gif_path)
window.show()

app.exec()