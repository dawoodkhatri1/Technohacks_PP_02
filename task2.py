import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout


class TempConverter(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle('Temperature Converter')
        self.setStyleSheet("background-color: black;")

        # Layout
        layout = QVBoxLayout()

        # Input field for Fahrenheit
        self.fahrenheit_input = QLineEdit(self)
        self.fahrenheit_input.setStyleSheet("background-color: lightgray; color: black;")
        self.fahrenheit_input.setPlaceholderText('Enter temperature in Fahrenheit')
        layout.addWidget(self.fahrenheit_input)

        # Convert to Celsius button
        self.to_celsius_button = QPushButton('Convert to Celsius', self)
        self.to_celsius_button.setStyleSheet("background-color: blue; color: white;")
        self.to_celsius_button.clicked.connect(self.convert_to_celsius)
        layout.addWidget(self.to_celsius_button)

        # Input field for Celsius
        self.celsius_input = QLineEdit(self)
        self.celsius_input.setStyleSheet("background-color: lightgray; color: black;")
        self.celsius_input.setPlaceholderText('Enter temperature in Celsius')
        layout.addWidget(self.celsius_input)

        # Convert to Fahrenheit button
        self.to_fahrenheit_button = QPushButton('Convert to Fahrenheit', self)
        self.to_fahrenheit_button.setStyleSheet("background-color: blue; color: white;")
        self.to_fahrenheit_button.clicked.connect(self.convert_to_fahrenheit)
        layout.addWidget(self.to_fahrenheit_button)

        # Label to display the result
        self.result_label = QLabel('', self)
        self.result_label.setStyleSheet("background-color: yellow; color: black;")
        layout.addWidget(self.result_label)

        # Layout for the main window
        self.setLayout(layout)

    def convert_to_celsius(self):
        try:
            fahrenheit = float(self.fahrenheit_input.text())
            celsius = (fahrenheit - 32) * 5.0 / 9.0
            self.result_label.setText(f'{fahrenheit}°F = {celsius:.2f}°C')
        except ValueError:
            self.result_label.setText('Invalid input for Fahrenheit')

    def convert_to_fahrenheit(self):
        try:
            celsius = float(self.celsius_input.text())
            fahrenheit = celsius * 9.0 / 5.0 + 32
            self.result_label.setText(f'{celsius}°C = {fahrenheit:.2f}°F')
        except ValueError:
            self.result_label.setText('Invalid input for Celsius')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = TempConverter()
    converter.show()
    sys.exit(app.exec_())
