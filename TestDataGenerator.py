# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from Utils.generatory import generate_nip, generate_regon, generate_do, generate_ppe
from random_pesel import RandomPESEL
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 550)
        fontNr = QtGui.QFont()
        fontGd = QtGui.QFont()
        fontCp = QtGui.QFont()
        fontPpe = QtGui.QFont()
        fontNr.setPointSize(20)
        fontGd.setPointSize(14)
        fontGd.setBold(True)
        fontCp.setPointSize(10)
        fontPpe.setPointSize(18)
        font = QtGui.QFont()
        font.setPointSize(8)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.generuj_dane = QtWidgets.QPushButton(self.centralwidget)
        self.generuj_dane.setGeometry(QtCore.QRect(220, 30, 180, 50))
        self.generuj_dane.setFont(fontGd)
        self.generuj_dane.setObjectName("generuj_dane")
        self.generuj_dane.clicked.connect(self.genDataAll)

        self.nr_nip = QtWidgets.QTextBrowser(self.centralwidget)
        self.nr_nip.setGeometry(QtCore.QRect(130, 120, 461, 51))
        self.nr_nip.setFont(fontNr)
        self.nr_nip.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nr_nip.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nr_nip.setObjectName("nr_nip")

        self.copy_nip = QtWidgets.QPushButton(self.centralwidget)
        self.copy_nip.setGeometry(QtCore.QRect(30, 120, 81, 51))
        self.copy_nip.setFont(fontCp)
        self.copy_nip.setObjectName("copy_nip")

        self.copy_pesel = QtWidgets.QPushButton(self.centralwidget)
        self.copy_pesel.setGeometry(QtCore.QRect(30, 190, 81, 51))
        self.copy_pesel.setFont(fontCp)
        self.copy_pesel.setObjectName("copy_pesel")

        self.nr_pesel = QtWidgets.QTextBrowser(self.centralwidget)
        self.nr_pesel.setGeometry(QtCore.QRect(130, 190, 461, 51))
        self.nr_pesel.setFont(fontNr)
        self.nr_pesel.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nr_pesel.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nr_pesel.setObjectName("nr_pesel")

        self.nr_do = QtWidgets.QTextBrowser(self.centralwidget)
        self.nr_do.setGeometry(QtCore.QRect(130, 290, 461, 51))
        self.nr_do.setFont(fontNr)
        self.nr_do.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nr_do.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nr_do.setObjectName("nr_do")

        self.copy_do = QtWidgets.QPushButton(self.centralwidget)
        self.copy_do.setGeometry(QtCore.QRect(30, 290, 81, 51))
        self.copy_do.setFont(font)
        self.copy_do.setObjectName("copy_do")

        self.copy_regon = QtWidgets.QPushButton(self.centralwidget)
        self.copy_regon.setGeometry(QtCore.QRect(30, 360, 81, 51))
        self.copy_regon.setFont(fontCp)
        self.copy_regon.setObjectName("copy_regon")

        self.nr_regon = QtWidgets.QTextBrowser(self.centralwidget)
        self.nr_regon.setGeometry(QtCore.QRect(130, 360, 461, 51))
        self.nr_regon.setFont(fontNr)
        self.nr_regon.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nr_regon.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nr_regon.setObjectName("nr_regon")

        self.nr_ppe = QtWidgets.QTextBrowser(self.centralwidget)
        self.nr_ppe.setGeometry(QtCore.QRect(130, 430, 461, 51))
        self.nr_ppe.setFont(fontPpe)
        self.nr_ppe.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nr_ppe.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nr_ppe.setObjectName("nr_ppe")

        self.copy_ppe = QtWidgets.QPushButton(self.centralwidget)
        self.copy_ppe.setGeometry(QtCore.QRect(30, 430, 81, 51))
        self.copy_ppe.setFont(fontCp)
        self.copy_ppe.setObjectName("copy_ppe")

        self.osd = QtWidgets.QComboBox(self.centralwidget)
        for item in range(32):
            self.osd.addItem("")

        self.osd.setObjectName("osd")
        self.osd.setGeometry(QtCore.QRect(130, 490, 461, 35))
        self.osd.setFont(font)

        self.labelWiek = QtWidgets.QLabel(self.centralwidget)
        self.labelWiek.setGeometry(QtCore.QRect(190, 250, 47, 13))
        self.labelWiek.setFont(fontCp)
        self.labelWiek.setObjectName("labelWiek")

        self.labelSex = QtWidgets.QLabel(self.centralwidget)
        self.labelSex.setGeometry(QtCore.QRect(360, 250, 31, 16))
        self.labelSex.setFont(fontCp)
        self.labelSex.setObjectName("labelSex")

        self.wiek_min = QtWidgets.QSpinBox(self.centralwidget)
        self.wiek_min.setGeometry(QtCore.QRect(230, 250, 42, 22))
        self.wiek_min.setProperty("value", 18)
        self.wiek_min.setObjectName("wiek_min")

        self.wiek_max = QtWidgets.QSpinBox(self.centralwidget)
        self.wiek_max.setGeometry(QtCore.QRect(290, 250, 42, 22))
        self.wiek_max.setProperty("value", 99)
        self.wiek_max.setObjectName("wiek_max")

        self._toggle = True

        self.ch_female = QtWidgets.QCheckBox(self.centralwidget)
        self.ch_female.setGeometry(QtCore.QRect(400, 250, 31, 17))
        self.ch_female.setFont(fontCp)
        self.ch_female.setChecked(self._toggle)
        self.ch_female.setObjectName("ch_female")
        self.ch_female.clicked.connect(self.toggle)

        self.ch_male = QtWidgets.QCheckBox(self.centralwidget)
        self.ch_male.setGeometry(QtCore.QRect(440, 250, 31, 17))
        self.ch_male.setFont(fontCp)
        self.ch_male.setChecked(not self._toggle)
        self.ch_male.setObjectName("ch_male")
        self.ch_male.clicked.connect(self.toggle)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def toggle(self):
        self._toggle = not self._toggle
        self.ch_female.setChecked(self._toggle)
        self.ch_male.setChecked(not self._toggle)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generator Danych Do Formularzy"))
        self.generuj_dane.setText(_translate("MainWindow", "Generuj Dane "))
        self.nr_nip.setText(_translate("MainWindow", ""))
        self.copy_nip.setToolTip(_translate("MainWindow", "Kopiuj"))
        self.copy_nip.setText(_translate("MainWindow", "NIP"))
        self.copy_pesel.setToolTip(_translate("MainWindow", "Kopiuj"))
        self.copy_pesel.setText(_translate("MainWindow", "PESEL"))
        self.nr_pesel.setText(_translate("MainWindow", ""))
        self.nr_do.setText(_translate("MainWindow", ""))
        self.copy_do.setToolTip(_translate("MainWindow", "Kopiuj"))
        self.copy_do.setText(_translate("MainWindow", "NR\n DOWODU\n OSOBISTEGO"))
        self.copy_regon.setToolTip(_translate("MainWindow", "Kopiuj"))
        self.copy_regon.setText(_translate("MainWindow", "REGON"))
        self.nr_regon.setText(_translate("MainWindow", ""))
        self.nr_ppe.setText(_translate("MainWindow", ""))
        self.copy_ppe.setToolTip(_translate("MainWindow", "Kopiuj"))
        self.copy_ppe.setText(_translate("MainWindow", "NR PPE"))
        self.labelWiek.setText(_translate("MainWindow", "Wiek"))
        self.labelSex.setText(_translate("MainWindow", "Płeć"))
        self.ch_female.setText(_translate("MainWindow", "K"))
        self.ch_male.setText(_translate("MainWindow", "M"))
        self.copy_ppe.pressed.connect(self.nr_ppe.selectAll)
        self.copy_ppe.released.connect(self.nr_ppe.copy)
        self.copy_regon.pressed.connect(self.nr_regon.selectAll)
        self.copy_regon.released.connect(self.nr_regon.copy)
        self.copy_do.pressed.connect(self.nr_do.selectAll)
        self.copy_do.released.connect(self.nr_do.copy)
        self.copy_pesel.pressed.connect(self.nr_pesel.selectAll)
        self.copy_pesel.released.connect(self.nr_pesel.copy)
        self.copy_nip.pressed.connect(self.nr_nip.selectAll)
        self.copy_nip.released.connect(self.nr_nip.copy)
        self.osd.setItemText(0, _translate("MainWindow", u"PGE Dystrybucja S.A. Oddzia\u0142 Bia\u0142ystok", None))
        self.osd.setItemText(1, _translate("MainWindow", u"PGE Dystrybucja S.A. Oddzia\u0142 Lublin", None))
        self.osd.setItemText(2,
                             _translate("MainWindow", u"PGE Dystrybucja S.A. Oddzia\u0142 \u0141\u00f3d\u017a - Miasto",
                                        None))
        self.osd.setItemText(3,
                             _translate("MainWindow", u"PGE Dystrybucja S.A. Oddzia\u0142 \u0141\u00f3d\u017a - Teren",
                                        None))
        self.osd.setItemText(4, _translate("MainWindow", u"PGE Dystrybucja S.A. Oddzia\u0142 Rzesz\u00f3w", None))
        self.osd.setItemText(5, _translate("MainWindow", u"PGE Dystrybucja S.A. Oddzia\u0142 Skar\u017cysko-Kamienna",
                                           None))
        self.osd.setItemText(6, _translate("MainWindow", u"PGE Dystrybucja S.A. Oddzia\u0142 Warszawa", None))
        self.osd.setItemText(7, _translate("MainWindow", u"PGE Dystrybucja S.A. Oddzia\u0142 Zamo\u015b\u0107", None))
        self.osd.setItemText(8, _translate("MainWindow", u"TAURON Dystrybucja S.A. (Krak\u00f3w)", None))
        self.osd.setItemText(9, _translate("MainWindow", u"TAURON Dystrybucja S.A. (Wroc\u0142aw)", None))
        self.osd.setItemText(10, _translate("MainWindow", u"TAURON Dystrybucja S.A. (Gliwice)", None))
        self.osd.setItemText(11, _translate("MainWindow", u"Enea Operator Sp. z o.o.", None))
        self.osd.setItemText(12, _translate("MainWindow", u"Energa Operator S.A.", None))
        self.osd.setItemText(13, _translate("MainWindow", u"Innogy Stoen Operator Sp. z o.o.", None))
        self.osd.setItemText(14, _translate("MainWindow", u"PKP Energetyka S.A.", None))
        self.osd.setItemText(15, _translate("MainWindow", u"POLENERGIA Dystrybucja Sp. z o.o.", None))
        self.osd.setItemText(16, _translate("MainWindow", u"Elco Energy Sp. z o.o.", None))
        self.osd.setItemText(17, _translate("MainWindow", u"ELSEN S.A.", None))
        self.osd.setItemText(18, _translate("MainWindow", u"Energia Euro Park Sp. z o.o.", None))
        self.osd.setItemText(19, _translate("MainWindow", u"Energomedia Sp. z o.o.", None))
        self.osd.setItemText(20, _translate("MainWindow", u"Energoserwis Kleszcz\u00f3w Sp. z o.o.", None))
        self.osd.setItemText(21, _translate("MainWindow", u"ESV Wis\u0142osan Sp. z o.o.", None))
        self.osd.setItemText(22, _translate("MainWindow", u"Przedsi\u0119biorstwo Energetyczne ESV S.A.", None))
        self.osd.setItemText(23, _translate("MainWindow", u"Green Lights Dystrybucja Sp. z o.o.", None))
        self.osd.setItemText(24, _translate("MainWindow", u"Green Lights Sp. z o.o.", None))
        self.osd.setItemText(25, _translate("MainWindow", u"Green Lights Holding Sp. z o.o.", None))
        self.osd.setItemText(26, _translate("MainWindow",
                                            u"Grupa Energia Obr\u00f3t GE Sp\u00f3\u0142ka z o.o. Sp\u00f3\u0142ka komandytowa",
                                            None))
        self.osd.setItemText(27, _translate("MainWindow",
                                            u"Grupa Energia GE Sp\u00f3\u0142ka z o.o. Sp\u00f3\u0142ka komandytowa",
                                            None))
        self.osd.setItemText(28, _translate("MainWindow", u"Miejska Energetyka Cieplna Sp. z o.o.", None))
        self.osd.setItemText(29, _translate("MainWindow", u"Plus Energia Sp. z o.o.", None))
        self.osd.setItemText(30, _translate("MainWindow", u"Power 21 Sp. z o.o.", None))
        self.osd.setItemText(31, _translate("MainWindow", u"Terawat Dystrybucja Sp. z o.o.", None))

    def genDataAll(self):
        self.genNip()
        self.genPesel()
        self.genRegon()
        self.genDo()
        self.genOsdValue()

    def genNip(self):
        nip = generate_nip()
        self.nr_nip.setText(nip)

    def genPesel(self):
        stateF = self.ch_female.isChecked()
        stateM = self.ch_male.isChecked()
        if stateF:
            x = "f"
        elif stateM:
            x = "m"
        y = self.wiek_min.value()
        z = self.wiek_max.value()
        pesel = RandomPESEL().generate(gender=x, min_age=y, max_age=z)
        self.nr_pesel.setText(pesel)

    def genRegon(self):
        regon = generate_regon()
        self.nr_regon.setText(regon)

    def genDo(self):
        do = generate_do()
        self.nr_do.setText(do)

    def genOsdValue(self):
        maskaOsd = self.osd.currentText()
        ppe = generate_ppe(maskaOsd)
        self.nr_ppe.setText(ppe)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
