from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QColorDialog,
    QFileDialog,
)
from PySide6.QtGui import QIcon,QMovie,QColor,QPixmap
from PySide6.QtCore import QByteArray
import sys
import qrcode
from qt_material import apply_stylesheet

from urllib.request import urlopen

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.myColor = QColor("black")
        self.resize(450,500)
        # Layout
        self.Box = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        # Widgets
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')

        self.linkLabel = QLabel(self)
        self.linkLabel.setText('Link:')

        self.link = QLineEdit()
        self.name = QLineEdit()

        self.url = QPushButton('Generate')
        self.url.clicked.connect(self.QRmaker)

        self.color = QPushButton('Choice Color')
        self.color.clicked.connect(self.on_click)

        self.Qr = QLabel(self)
        self.Qr.setVisible(False)

        # Adding Widget to layout
        row1.addWidget(self.nameLabel)
        row1.addWidget(self.name)

        row2.addWidget(self.linkLabel)
        row2.addWidget(self.link)

        self.Box.addLayout(row1)
        self.Box.addLayout(row2)

        self.Box.addWidget(self.color)
        self.Box.addWidget(self.url)
        self.Box.addWidget(self.Qr)
        
        # Setting the layout of final window
        self.setLayout(self.Box)
        
    def QRmaker(self):
        name = self.name.text()
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        qr.add_data(self.link.text())
        qr.make(fit=True)
        # print(self.myColor)
        img = qr.make_image(fill_color=self.myColor, back_color="white")
        img.save(f"{name}.png")

        pixmap = QPixmap(f'{name}.png')
        self.Qr.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.Qr.setVisible(True)

        
    
    def on_click(self):
        print("on")
        self.openColorDialog()

    def openColorDialog(self):
        print("open")
        color = QColorDialog.getColor()
        

        if color.isValid():
            self.myColor = color.name()
            print(self.myColor)
        else:
            self.myColor = "black"
            
    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select a directory", "/home")
        if directory:
            print(directory)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app,theme="dark_cyan.xml")
    window = MainWindow()
    window.show()

    app.exec()