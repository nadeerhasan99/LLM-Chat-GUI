from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 790)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                 "gridline-color: rgb(255, 255, 255);\n"
                                 "border-top-color: rgb(255, 255, 255);\n"
                                 "border-color: rgb(0, 0, 255);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Chat history display
        self.chat = QtWidgets.QTextEdit(self.centralwidget)
        self.chat.setGeometry(QtCore.QRect(13, 60, 1021, 431))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chat.setFont(font)
        self.chat.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.chat.setObjectName("chat")
        self.chat.setReadOnly(True)
        self.chat.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)  # Enable line wrapping

        # Main label at the top
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

       # Textbox for typing the question
        self.Question = QtWidgets.QTextEdit(self.centralwidget)
        self.Question.setGeometry(QtCore.QRect(13, 576, 1021, 60))
        font = QtGui.QFont()
        font.setPointSize(10)  # Slightly increased font size
        self.Question.setFont(font)
        self.Question.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Question.setObjectName("Question")

        # Label for the question input area
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(304, 520, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        # Send button to submit the question
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(10, 660, 1021, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.send.setFont(font)
        self.send.setStyleSheet("background-color: rgb(0, 0, 255);\n"
                                "gridline-color: rgb(255, 255, 255);\n"
                                "color: rgb(255, 255, 255);")
        self.send.setObjectName("send")

        # Clear chat button
        self.clear_chat = QtWidgets.QPushButton(self.centralwidget)
        self.clear_chat.setGeometry(QtCore.QRect(10, 720, 1021, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear_chat.setFont(font)
        self.clear_chat.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                      "gridline-color: rgb(255, 255, 255);\n"
                                      "color: rgb(255, 255, 255);")
        self.clear_chat.setObjectName("clear_chat")

        # Set the central widget
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Connect the send and clear buttons to their respective functions
        self.send.clicked.connect(self.send_question)
        self.clear_chat.clicked.connect(self.clear_chat_area)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Chat"))
        self.Question.setStatusTip(_translate("MainWindow", "Type your question"))
        self.label_2.setText(_translate("MainWindow", "Type your question below"))
        self.send.setStatusTip(_translate("MainWindow", "Click to send your question"))
        self.send.setText(_translate("MainWindow", "Send"))
        self.clear_chat.setStatusTip(_translate("MainWindow", "Click to clear the chat area"))
        self.clear_chat.setText(_translate("MainWindow", "Clear Chat"))

    def send_question(self):
        # Get user input from the text box
        user_input = self.Question.toPlainText().strip()
    
        if user_input:
            # Display the question in the chat area
            self.chat.append(f"Question: {user_input}")
    
            # Clear the question input after sending
            self.Question.clear()
    
            headers = {"Content-Type": "application/json"}
            base_url = "https://5959-34-125-197-236.ngrok-free.app"  # Replace with your actual base URL
            endpoint = f"{base_url}/generate"
    
            try:
                # Make the API call
                response = requests.post(endpoint, headers=headers, json={
                    "inputs": "\n\n### Instructions:\n" + user_input + "\n\n### Response:\n",
                    "parameters": {"stop": ["###"], "max_tokens": 200}  
                })
    
                # Check if the response is successful
                if response.status_code == 200:
                    # Get the output and display in the chat area
                    output = response.json()
                    generated_text = output.get("generated_text", "No response from API")
                    self.chat.append(f"Answer: {generated_text}")
                else:
                    # Handle non-200 response
                    self.chat.append(f"Error: Received status code {response.status_code}")
    
            except Exception as e:
                self.chat.append(f"Error: {str(e)}")

    def clear_chat_area(self):
        # Clear the chat QTextEdit widget
        self.chat.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        pass  
