import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pkg_resources
from datetime import datetime
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDateEdit


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        current_date = datetime.now().strftime("%Y-%m-%d")
        date_label = QtWidgets.QLabel(current_date, self)

        self.item_title_label = QtWidgets.QLabel("Item Title", self)
        self.item_title_entry = QtWidgets.QLineEdit(self)
        # self.item_title_entry.setValidator()
        self.item_title_mult_label = QtWidgets.QLabel("", self)

        self.item_link_label = QtWidgets.QLabel("Item Link", self)
        self.item_link_entry = QtWidgets.QLineEdit(self)
        # self.item_link_entry.setValidator()
        self.item_link_mult_label = QtWidgets.QLabel("", self)

        self.item_tracking_label = QtWidgets.QLabel("Item Tracking", self)
        self.item_tracking_entry = QtWidgets.QLineEdit(self)
        # self.item_tracking_entry.setValidator()
        self.item_tracking_mult_label = QtWidgets.QLabel("", self)

        self.item_order_label = QtWidgets.QLabel("Order Number", self)
        self.item_order_entry = QtWidgets.QLineEdit(self)
        # self.item_order_entry.setValidator(QtGui.QIntValidator())
        self.item_order_mult_label = QtWidgets.QLabel("", self)

        self.item_cost_label = QtWidgets.QLabel("Item Cost", self)
        self.item_cost_entry = QtWidgets.QLineEdit(self)

        validator = QtGui.QDoubleValidator()
        self.item_cost_entry.setValidator(validator)

        self.item_cost_mult_label = QtWidgets.QLabel("", self)

        self.withdraw_label = QtWidgets.QLabel("Withdraw", self)
        self.withdraw_entry = QtWidgets.QLineEdit(self)
        self.withdraw_entry.setValidator(validator)

        self.withdraw_mult_label = QtWidgets.QLabel("", self)

        self.profit_label = QtWidgets.QLabel("Profit", self)
        self.profit_entry = QtWidgets.QLabel(self)
        self.profit_entry.setObjectName("profit_entry")
        self.percentage_label = QtWidgets.QLabel(self)

        self.calculate_button = QtWidgets.QPushButton("Calculate", self)
        self.calculate_button.clicked.connect(self.calculate_profit)

        self.sold_date_edit = QtWidgets.QDateEdit(self)
        self.sold_date_edit.setCalendarPopup(True)
        self.sold_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.sold_date_edit.setDate(QDate.currentDate())

        self.ship_date_edit = QtWidgets.QDateEdit(self)
        self.ship_date_edit.setCalendarPopup(True)
        self.ship_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.ship_date_edit.setDate(QDate.currentDate())

        self.customer_details_label = QtWidgets.QLabel(
            "Customer Details", self)
        self.customer_details_entry = QtWidgets.QLineEdit(self)

        self.withdraw_doller_price_label = QtWidgets.QLabel("", self)
        self.withdraw_doller_price_entry = QtWidgets.QLineEdit(self)

        self.item_doller_price_label = QtWidgets.QLabel("", self)
        self.item_doller_price_entry = QtWidgets.QLineEdit(self)

        layout = QtWidgets.QFormLayout()
        hbox_layout = QtWidgets.QHBoxLayout()

        layout.addRow(date_label)
        layout.addRow(self.item_title_label, self.item_title_entry)
        layout.addRow(self.item_link_label, self.item_link_entry)
        layout.addRow(self.item_tracking_label, self.item_tracking_entry)
        layout.addRow(self.item_order_label, self.item_order_entry)
        layout.addRow("Sold Date", self.sold_date_edit)
        layout.addRow("Ship Date", self.ship_date_edit)
        layout.addRow(self.customer_details_label, self.customer_details_entry)

        hbox_layout = QtWidgets.QHBoxLayout()
        hbox_layout.addWidget(self.item_cost_label)
        hbox_layout.addWidget(self.item_cost_entry)
        hbox_layout.addWidget(self.item_doller_price_entry)
        self.item_doller_price_entry.setText("380")
        self.item_doller_price_entry.setPlaceholderText("380")
        hbox_layout.addWidget(self.item_cost_mult_label)
        layout.addRow(hbox_layout)

        self.item_cost_entry.setFixedWidth(95)
        self.item_doller_price_entry.setFixedWidth(95)
        self.item_cost_mult_label.setFixedWidth(68)

        hbox_layout2 = QtWidgets.QHBoxLayout()
        hbox_layout2.addWidget(self.withdraw_label)
        hbox_layout2.addWidget(self.withdraw_entry)
        hbox_layout2.addWidget(self.withdraw_doller_price_entry)
        self.withdraw_doller_price_entry.setText("350")
        self.withdraw_doller_price_entry.setPlaceholderText("350")
        hbox_layout2.addWidget(self.withdraw_mult_label)
        layout.addRow(hbox_layout2)

        self.withdraw_entry.setFixedWidth(95)
        self.withdraw_doller_price_entry.setFixedWidth(95)
        self.withdraw_mult_label.setFixedWidth(68)

        hbox_layout3 = QtWidgets.QHBoxLayout()
        hbox_layout3.addWidget(self.profit_label)
        hbox_layout3.addWidget(self.profit_entry)
        hbox_layout3.addWidget(self.percentage_label)
        layout.addRow(hbox_layout3)

        layout.addRow(self.calculate_button)
        self.export_button = QtWidgets.QPushButton("Export to txt", self)
        self.export_button.clicked.connect(self.export_to_txt)
        layout.addRow(self.export_button)

        date_label.setObjectName("date_label")
        self.sold_date_edit.setObjectName("date_view")
        self.ship_date_edit.setObjectName("date_view")

        widget = QtWidgets.QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def calculate_profit(self):
        item_doller_price = self.item_doller_price_entry.text()
        withdraw_doller_price = self.withdraw_doller_price_entry.text()
        item_cost = self.item_cost_entry.text()
        withdraw = self.withdraw_entry.text()

        try:
            item_doller_price = float(
                item_doller_price) if item_doller_price != "" else 380
            withdraw_doller_price = float(
                withdraw_doller_price) if withdraw_doller_price != "" else 350
            item_cost = float(item_cost)
            withdraw = float(withdraw)
            # Do multiplications and calculations here
            real_item_price = item_cost * item_doller_price
            real_withdraw_price = withdraw * withdraw_doller_price
            profit = real_withdraw_price - real_item_price
            formatted_profit = format(profit, '.2f')
            profit_percentage = (profit / real_item_price) * 100
            formatted_profit_percentage = format(
                profit_percentage, '.2f') + "%"
            self.percentage_label.setText(formatted_profit_percentage)
        except ValueError:
            self.profit_entry.setText(
                "Invalid Input")
            self.profit_entry.setStyleSheet("color: red;")
        else:
            if profit < 0:
                self.profit_entry.setStyleSheet("color: #ff0000;")
            elif 0 <= profit < 400:
                self.profit_entry.setStyleSheet("color: #ff9900;")
            else:
                self.profit_entry.setStyleSheet("color: #2bff00;")
            self.profit_entry.setText(str(formatted_profit))
            self.percentage_label.setStyleSheet(self.profit_entry.styleSheet())
            self.update_mult_labels(item_doller_price, withdraw_doller_price)
            

    def update_mult_labels(self, item_doller_price, withdraw_doller_price):
        self.item_cost_mult_label.setText("{:.2f}".format(
            float(self.item_cost_entry.text()) * item_doller_price))
        self.withdraw_mult_label.setText("{:.2f}".format(
            float(self.withdraw_entry.text()) * withdraw_doller_price))

    def export_to_txt(self):
        item_cost = self.item_cost_entry.text()
        withdraw = self.withdraw_entry.text()
        profit = self.profit_entry.text()
        item_title = self.item_title_entry.text()
        item_link = self.item_link_entry.text()
        item_tracking = self.item_tracking_entry.text()
        item_order_number = self.item_order_entry.text()
        customer_details = self.customer_details_entry.text().replace("\n", ", ")
        sold_date = self.sold_date_edit.date().toString()
        ship_date = self.ship_date_edit.date().toString()
        profit_percentage = self.percentage_label.text()
        filename = f"{item_title}.txt"

        with open(filename, "w") as file:
            file.truncate()
            file.write("*******      Item Details      *******")
            file.write("\n\n")
            file.write("Item Title: " + item_title + "\n")
            file.write("Item Link: " + item_link + "\n")
            file.write("Item Tracking: " + item_tracking + "\n")
            file.write("Order Number: " + item_order_number + "\n")
            file.write("Customer Details: " + customer_details + "\n")
            file.write("Item Cost: " + item_cost + "\n")
            file.write("Withdraw: " + withdraw + "\n")
            file.write("Profit: " + profit + "\n")
            file.write("Profit Percentage:" + profit_percentage + "\n")
            file.write("Sold Date: " + sold_date + "\n")
            file.write("Ship Date: " + ship_date + "\n")

        os.startfile(filename)


app = QtWidgets.QApplication(sys.argv)
with pkg_resources.resource_stream(__name__, "style.css") as css_file:
    css = css_file.read().decode()
    app.setStyleSheet(css)
window = MainWindow()

window.setMaximumSize(414, 560)
window.setMinimumSize(414, 560)
window.setGeometry(500, 50, 414, 560)


window.setWindowTitle("Ebay Profit Cal")
window.show()
sys.exit(app.exec_())
