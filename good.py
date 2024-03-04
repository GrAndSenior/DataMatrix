from PyQt5.QtWidgets import QMainWindow, QFileDialog, QProgressBar, QMenu, QMessageBox, QAction
from PyQt5.QtCore import QDate, Qt
from PyQt5 import QtGui
import goods
import pandas as pd
from pandasmodel import PandasModel
from pdfpreview import PdfPreview
from layoutdm import LayoutDM
from zplprinter import ZplPrinter
from time import time
from csv import QUOTE_NONE

class Good(QMainWindow, goods.Ui_GoodWindow):
    def __init__(self, parent, **kwargs) -> None:
        super().__init__(parent)
        self.setupUi(self)  # Это для инициализации  дизайна
        self.parent = parent
        self.options = parent.options
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0,100)
        self.statusBar().addPermanentWidget(self.progress_bar)
        self.progress_bar.hide()
        self.gbK.hide()
        self.gbP.hide()

        addgrup_action = QAction( u"Печать с текущего кода", self )
        addgrup_action.setToolTip( u"Продолжить печать с выбранного кода" )
        self.tvDmCodes.addAction( addgrup_action )
        addgrup_action.triggered.connect( self.on_resumeprint )
        addgrup_action = QAction( u"Печать выделенных кодов", self )
        addgrup_action.setToolTip( u"Распечатать только выбранные коды" )
        self.tvDmCodes.addAction( addgrup_action )
        addgrup_action.triggered.connect( self.on_printselected )

        addgrup_action = QAction( u"Печать всех кодов", self )
        addgrup_action.setToolTip( u"Распечатать все коды по товару" )
        self.tvDmCodes.addAction( addgrup_action )
        addgrup_action.triggered.connect( self.on_zplprint )

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tvDmCodes.setContextMenuPolicy( Qt.ActionsContextMenu )

        for key, value in kwargs.items():
            if key == 'number':
                self.number = value
                if value != '':
                    self.setWindowTitle('Маркировка Datamatrix - информация по товару')
                else:
                    self.setWindowTitle('Маркировка Datamatrix - добавление нового товара')
            elif key == 'customer':
                self.customer = value
            elif key == 'id_state':
                self.id_state = value
            elif key == 'date_on':
                if isinstance(value, str):
                    self.date_on = QDate.fromString(value, "dd.MM.yyyy")
                else:
                    self.date_on = value
            elif key == 'manager':
                self.manager = value
            elif key == 'good':
                self.good = value
            elif key == 'category':
                self.id_category = value
        
        self.setWidgetData()
        self.accept_actions()

    def on_resumeprint(self, point):
        tmp = self.data_frame.iloc[self.tvDmCodes.currentIndex().row():]
        self.zplprint = ZplPrinter(self, tmp['gs1dm'].tolist())
        self.zplprint.show() 

    def on_printselected(self, point):
        selectedRows = []
        for sel in self.tvDmCodes.selectionModel().selectedRows():
            selectedRows.append(sel.row())
        tmp = self.data_frame.iloc[selectedRows]
        self.zplprint = ZplPrinter(self, tmp['gs1dm'].tolist())
        self.zplprint.show() 


    def accept_actions(self):
        self.btnOk.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)
        self.btnCsvImport.clicked.connect(self.add_from_csv)
        self.btnPdfImport.clicked.connect(self.add_from_pdf)
        self.btnMakeDm.clicked.connect(self.on_make_dm)
        self.btnMakeD_K.clicked.connect(self.on_make_dm_K)
        self.btnZplPrint.clicked.connect(self.on_zplprint)
        self.btnFind.clicked.connect(self.on_find)
        self.btnAgg.clicked.connect(self.on_aggregate)
        self.btnReport.clicked.connect(self.on_report_click)

    def add_KCodes(self,row):
        pass        

    def on_aggregate(self):
        #if self.data_frame['']
        KCodes = []
        k = 0
        for i in range(self.data_frame['gs1dm'].count()):
            KCodes.append(i // int(self.leKCount.text()))
        self.data_frame['K'] = KCodes
        print(self.data_frame)

        self.model = PandasModel(self.data_frame)
        self.tvDmCodes.setModel(self.model)
        self.tvDmCodes.resizeColumnsToContents()
        #self.statusBar().showMessage('ВНИМАНИЕ! В настоящее время ведется работа на совершенствованием данной функции', 0)

    def on_report_click(self):
        if self.leGoodName.text() != '':
            filename = self.leGoodName.text()+'.csv'
        else:
            filename = 'report_dm.csv'
        try:
            self.data_frame.to_csv(filename, index=False, header=False, sep=chr(9), quoting=QUOTE_NONE)
            self.statusBar().showMessage('Сохранение отчета выполнено успешно!', 5000)
        except:
            self.statusBar().showMessage('Сохранение отчета не выполнено!', 5000)

    def on_find(self):
        try:
            self.tvDmCodes.selectRow(self.data_frame[self.data_frame['gs1dm']==self.leFind.text()].index[0])
        except:
            self.statusBar().showMessage('Поиск завершился с ошибкой!', 5000)

    def on_zplprint(self):
        self.zplprint = ZplPrinter(self, self.data_frame['gs1dm'].tolist())
        self.zplprint.show()        

    def accept(self):
        self.close()

    def reject(self):
        # - не предполагает изменения в БД
        self.close()

    def setWidgetData(self):
        self.leOrderNumber.setText(self.number)
        self.leCustomer.setText(self.customer)
        self.leManager.setText(self.manager)
        self.deDateOn.setDate(self.date_on)
        self.leGoodName.setText(self.good)

        sql = 'SELECT STATE FROM dbmarking.ORDER_STATE;'
        self.cbOrderState.addItems(pd.read_sql_query(sql, self.parent.mydb)['STATE'].tolist())
        self.cbOrderState.setCurrentIndex(self.id_state)

        sql = '''SELECT FULL_NAME FROM dbmarking.CATEGORY;'''
        self.cbCategory.addItems(pd.read_sql_query(sql, self.parent.mydb)['FULL_NAME'].tolist())
        self.cbCategory.setCurrentIndex(self.id_category-1)

        if self.good != '':
            sql = 'SELECT id_goods FROM dbmarking.GOODS WHERE NAME = "'+self.good+'";'
            id_good = int(pd.read_sql_query(sql, self.parent.mydb).iloc[0])

            sql = 'SELECT id_order FROM dbmarking.ORDERS WHERE NUMBER = "'+self.number+'";'
            id_order = int(pd.read_sql_query(sql, self.parent.mydb).iloc[0])

            sql = ''' SELECT GS1DM FROM dbmarking.DM WHERE GOODS =''' + str(id_good) +" AND ORDERS = "+ str(id_order) + ";"
            self.data_frame = pd.read_sql_query(sql, self.parent.mydb)
            self.data_frame = self.data_frame.fillna(' ')
            self.data_frame = self.data_frame.rename(columns={'GS1DM' : 'GS1 Datamatrix'})

            self.model = PandasModel(self.data_frame)
            self.tvDmCodes.setModel(self.model)
            self.tvDmCodes.resizeColumnsToContents()
        self.tvDmCodes.show()

    def add_from_csv(self):
        pd.options.mode.copy_on_write = True
        options = QFileDialog.Options()
        #options |= QFileDialog.ExistingFiles   # включение множественного выбора
        options |= QFileDialog.DontUseNativeDialog
        fileNames, _ = QFileDialog.getOpenFileNames(self,"Выбор файлов с кодами...", "","CSV Files (*.csv);;TXT Files (*.txt);;All Files (*)", options=options)
        start = time()
        self.progress_bar.setFixedSize(self.geometry().width() - 120, 16)
        self.progress_bar.show()
        count = 1

        self.data_frame = pd.DataFrame(columns=['gs1dm'])
        for file in fileNames:
            df = pd.read_csv(file, sep='\t', encoding='utf-8', names=['gs1dm'])
            self.data_frame = pd.concat([self.data_frame, df], axis = 0)
            self.progress_bar.setValue(int(count/len(fileNames)*100))
            count += 1 
        else:
            self.progress_bar.setValue(100)
            self.progress_bar.hide()

        self.data_frame = self.data_frame.reset_index()
        del self.data_frame['index']
    
        self.model = PandasModel(self.data_frame)
        self.tvDmCodes.setModel(self.model)
        self.tvDmCodes.resizeColumnsToContents()
        self.tvDmCodes.show()
    
        self.statusBar().showMessage(f'Готово! Время на загрузку кодов: {round(time()-start,2)}сек. Обработано кодов: {self.data_frame["gs1dm"].count()}', 0)


    def add_from_pdf(self):
        self.importPdf = PdfPreview(self)
        self.importPdf.show()
        

    def on_make_dm(self):
        self.makeDmWindow = LayoutDM(self, key='')
        self.makeDmWindow.show()

    def on_make_dm_K(self):
        self.makeDmWindow = LayoutDM(self, key = 'group')
        self.makeDmWindow.show()
        

