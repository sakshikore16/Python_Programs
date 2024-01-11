# hello.py

"""Simple Hello, World example with PyQt6."""

import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle("Sakshi App")
window.setGeometry(100, 100, 580, 580)
helloMsg = QLabel("<h1>Hello! Sakshi</h1>", parent=window)
helloMsg.move(580, 580)

# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())
