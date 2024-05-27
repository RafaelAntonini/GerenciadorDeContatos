from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QWidget, QMessageBox, QRadioButton, QComboBox, QTableView
from PyQt5 import QtWidgets
from PyQt5 import uic
import db
import sys

class NewContactWindow(QMainWindow):
  def __init__(self):
    super(NewContactWindow, self).__init__() 
    uic.loadUi("newContact.ui", self)   
    self.findChild(QPushButton, 'pushButton').clicked.connect(self.register)
    self.findChild(QPushButton, 'backButton').clicked.connect(self.goBack)
  def register(self):
    name = self.findChild(QLineEdit, 'name').text()
    if not name.isalpha() or len(name) < 3:
      return self.showMsg('Por favor preencha o nome corretamente! ')
    surname = self.findChild(QLineEdit, 'surname').text()
    if not surname.isalpha() or len(surname) < 3:
      return self.showMsg('Por favor preencha o sobrenome corretamente! ')
    num = self.findChild(QLineEdit, 'number').text()
    if not num.isdigit() or len(num) != 11:
      return self.showMsg('Por favor preencha o número corretamente!\nEle deve ter 11 dígitos e conter apenas números. ')
    email = self.findChild(QLineEdit, 'email').text()
    if len(email) < 7 or '@' not in email or '.' not in email:
      return self.showMsg('Por favor, preencha o email corretamente!')
    db.session.add(db.Contacts(name = self.findChild(QLineEdit, 'name').text(), 
                               surname = self.findChild(QLineEdit, 'surname').text(), 
                               country = self.findChild(QComboBox, 'comboBox').currentText(), 
                               number = self.findChild(QLineEdit, 'number').text(),
                               email = self.findChild(QLineEdit, 'email').text()))
    db.session.commit()         
    self.showMsg('Contato registrado com sucesso.', 'Aviso') 
    self.clearAll()

  def showMsg(self, texto, title='Erro'):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(texto)
    msg.exec_()  
  def clearAll(self):
    self.findChild(QLineEdit, 'name').setText('')
    self.findChild(QLineEdit, 'surname').setText('')
    self.findChild(QLineEdit, 'number').setText('')
    self.findChild(QLineEdit, 'email').setText('')
    

  def goBack(self):
    self.hide()
    self.v = MainWindow()
    self.v.show()
class ViewContactWindow(QMainWindow):
  def __init__(self):
    super(ViewContactWindow, self).__init__() 
    uic.loadUi("viewContact.ui", self)
    self.findChild(QPushButton, 'pushButton').clicked.connect(self.view)
    self.findChild(QPushButton, 'backButton').clicked.connect(self.goBack)
  def view(self):
    data = db.session.query(db.Contacts).all()
    self.tableWidget.setRowCount(len(data))
    for i in range (len(data)):
      self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(data[i].name)))
      self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(data[i].surname)))
      self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(str(data[i].country)))
      self.tableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(str(data[i].number)))
    
  def showMsg(self, texto, title='Erro'):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(texto)
    msg.exec_()
  def goBack(self):
    self.hide()
    self.v = MainWindow()
    self.v.show()
class EditContactWindow(QMainWindow):
  def __init__(self):
    super(EditContactWindow, self).__init__() 
    uic.loadUi("editContact.ui", self)
    self.comboBox.addItems('One Two Three Four'.split()) 
    self.findChild(QPushButton, 'pushButton').clicked.connect(self.updateContact)
    self.findChild(QPushButton, 'backButton').clicked.connect(self.goBack)
    self.loadContacts()
  def loadContacts(self):
    data = db.session.query(db.Contacts).all()
    self.comboBox.clear()
    for contact in data:
      self.comboBox.addItem(contact.name)
  def updateContact(self):
    selectedName = self.findChild(QComboBox, 'comboBox').currentText()
    contact = db.session.query(db.Contacts).filter_by(name=selectedName).first()
        
    newName = self.findChild(QLineEdit, 'name').text()
    newSurname = self.findChild(QLineEdit, 'name_3').text()
    newNumber = self.findChild(QLineEdit, 'name_2').text()

    if not newName.isalpha() or len(newName) < 3:
      return self.showMsg('Por favor preencha o nome corretamente! ')
    if not newSurname.isalpha() or len(newSurname) < 3:
      return self.showMsg('Por favor preencha o sobrenome corretamente! ')
    if not newNumber.isdigit() or len(newNumber) != 11:
      return self.showMsg('Por favor preencha um número válido! ')
  
    contact.name = newName
    contact.surname = newSurname
    contact.number = newNumber
    db.session.commit()    
    self.showMsg('Contato alterado com sucesso.', 'Aviso') 
    self.loadContacts()
    self.clearAll() 

  def showMsg(self, texto, title='Erro'):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(texto)
    msg.exec_()  
  def goBack(self):
    self.hide()
    self.v = MainWindow()
    self.v.show()
  def clearAll(self):
    self.findChild(QLineEdit, 'name').setText('')
    self.findChild(QLineEdit, 'name_2').setText('')
    self.findChild(QLineEdit, 'name_3').setText('')
class RemoveContactWindow(QMainWindow):
  def __init__(self):
    super(RemoveContactWindow, self).__init__() 
    uic.loadUi("removeContact.ui", self)
    self.findChild(QPushButton, 'backButton').clicked.connect(self.goBack)
    self.findChild(QPushButton, 'pushButton').clicked.connect(self.removeContact)
    self.loadContacts()
  def loadContacts(self):
    data = db.session.query(db.Contacts).all()
    self.findChild(QComboBox, 'comboBox').clear()
    for contact in data:
      self.findChild(QComboBox, 'comboBox').addItem(contact.name)
  def removeContact(self):
    selectedName = self.comboBox.currentText()
    contact = db.session.query(db.Contacts).filter_by(name=selectedName).first()
        
    if contact:
      confirmation = QMessageBox.question(self, 'Confirmar exclusão', 
                                          f'Você tem certeza que gostaria de deletar o contato: {contact.name}?',
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
      if confirmation == QMessageBox.Yes:
        db.session.delete(contact)
        db.session.commit()
        self.showMsg('Contato removido com sucesso.', 'Aviso')
        self.loadContacts()
      else:
        self.label.setText('')
    else:
      self.showMsg('Contato não encontrado.', 'Erro')
  def showMsg(self, texto, title='Erro'):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(texto)
    msg.exec_()  
  def goBack(self):
    self.hide()
    self.v = MainWindow()
    self.v.show()
class MainWindow(QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()
    uic.loadUi("ui.ui", self)
    self.findChild(QPushButton, 'newButton').clicked.connect(self.newContact)
    self.findChild(QPushButton, 'viewButton').clicked.connect(self.viewContact)
    self.findChild(QPushButton, 'editButton').clicked.connect(self.editContact)
    self.findChild(QPushButton, 'removeButton').clicked.connect(self.removeContact)
    self.findChild(QPushButton, 'exitButton').clicked.connect(self.exit)
    self.show()
  def newContact(self):
     self.hide()
     self.v = NewContactWindow()
     self.v.show()
  def viewContact(self):
     self.hide()
     self.v = ViewContactWindow()
     self.v.show()
  def editContact(self):
     self.hide()
     self.v = EditContactWindow()
     self.v.show()
  def removeContact(self):
     self.hide()
     self.v = RemoveContactWindow()
     self.v.show()
  def exit(self):
    exit()

app = QApplication(sys.argv)
UIWindow = MainWindow()
app.exec_()     
            
      

