from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QTabWidget, QPushButton, QLabel, QLineEdit, QSpacerItem


class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyResume")
        self.resize(800, 600)
        tab_widget = QTabWidget(self)

        # Information
        widget_form = QWidget()
        label_full_name = QLabel("Full name :")
        line_edit_full_name = QLineEdit()
        form_layout = QHBoxLayout()
        form_layout.addWidget(label_full_name)
        form_layout.addWidget(line_edit_full_name)
        widget_form.setLayout(form_layout)

        # Add tabs to widget
        tab_widget.addTab(widget_form, "Information")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)
