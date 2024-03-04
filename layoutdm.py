from PyQt5.QtWidgets import QMainWindow, QFileDialog, QProgressBar
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt # нужна константа Qt.KeepAspectRatio для изменения размеров с сохранением пропорций
from PIL import Image, ImageDraw, ImageFont
from time import time
import layoutui
import os
import treepoem



class LayoutDM(QMainWindow, layoutui.Ui_LayoutWindow):
    def __init__(self, parent, **kwargs) -> None:
        super().__init__(parent)
        self.setupUi(self)  # Это для инициализации  дизайна
        self.parent = parent
        self.options = parent.options
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0,100)
        self.statusBar().addPermanentWidget(self.progress_bar)
        self.progress_bar.hide()
        if 'key' in kwargs:
            self.subfolder = kwargs['key']
        else:
            self.subfolder = ''

        self.leLabelWidth.setText('236')
        self.leLabelHeight.setText('236')
        self.leBack.setText(self.options['LABEL']['back'])
        self.leLeft.setText(str(self.options['LABEL']['left']))
        self.leTop.setText(str(self.options['LABEL']['top']))
        self.leWidth.setText(str(self.options['LABEL']['width']))
        self.leHeight.setText(str(self.options['LABEL']['height']))
        self.cbText.setChecked = self.options['LABEL']['label']
        self.sbFontSize.setValue(self.options['LABEL']['font_size'])
        self.cbTextRotate.setCurrentText(str(self.options['LABEL']['label_rotate']))
        self.cbTextAllign.setCurrentText(str(self.options['LABEL']['label_align']))
        self.leTextLeft.setText(str(self.options['LABEL']['label_left']))
        self.leTextTop.setText(str(self.options['LABEL']['label_top']))
        '''self.gbZpl.setChecked = self.options['ZPL']['zpl']
        self.cbDMHeight.setCurrentText(str(self.options['ZPL']['code_size']))
        self.cbDMQuality.setCurrentText(str(self.options['ZPL']['code_quality']))
        self.cbDMRotate.setCurrentIndex(self.options['ZPL']['code_rotation'])'''

        self.accept_actions()

    def accept_actions(self):
        self.btnOk.clicked.connect(self.accept)
        self.btnCancel.clicked.connect(self.reject)
        self.btnOpenBack.clicked.connect(self.on_openBack_click)
        self.btnPreView.clicked.connect(self.on_preview_click)
        self.btnDefault.clicked.connect(self.on_default_click)
        self.cbText.toggled.connect(self.on_text_check)

    def on_text_check(self):
        self.leSampleText.setEnabled(self.cbText.isChecked())
        self.sbFontSize.setEnabled(self.cbText.isChecked())
        self.cbTextRotate.setEnabled(self.cbText.isChecked())
        self.cbTextAllign.setEnabled(self.cbText.isChecked())
        self.leTextLeft.setEnabled(self.cbText.isChecked())
        self.leTextTop.setEnabled(self.cbText.isChecked())

    def save_image_code(self, row):
        print(row['gs1dm'])

    def generate_gs1dm(self, gs1dm, version='26x26', textinclude=False, save=False, show=False):
        # Generate datamatrix
        datamatrix = treepoem.generate_barcode(
            barcode_type='datamatrix',
            data=f"^FNC1{gs1dm}",
            options={"parsefnc": True, "parse": True, "format": "square", "version": version, "includetext": textinclude})
        
        # Resize datamatrix to desired size
        #dm_size_px = (196, 196)
        dm_size_px = (int(self.leWidth.text())-4,int(self.leHeight.text())-4)
        datamatrix = datamatrix.resize(dm_size_px, Image.NEAREST)

        # Create white picture  
        #picture_size_px = (200, 200)
        picture_size_px = (int(self.leWidth.text()),int(self.leHeight.text()))
        picture = Image.new('L', picture_size_px, color='white')

        # Position the datamatrix
        barcode_position_px = (2, 2)
        picture.paste(datamatrix, barcode_position_px)

        # Draw picture for placing texts on it
        #draw = ImageDraw.Draw(picture)

        # Store font for the texts
        #ocrb_font = ImageFont.truetype("sources/fonts/arialnb.ttf", 12)
        # Draw texts on the Picture
        #datamatrix_text_position_px = (10,15)
        #draw.text(datamatrix_text_position_px, "This is a GS1 DataMatrix", fill='black', font=ocrb_font)
        #welcome_text_position_px = (35,180)
        #draw.text(welcome_text_position_px, gs1dm[:gs1dm.find('93')], fill='black', font=ocrb_font)

        # Save the image
        if save:
            picture.save("datamatrix.png")
        if show:
            picture.show()

    def gs1dm_df(self,row):
        self.progress_bar.setFixedSize(self.geometry().width() - 120, 16)
        self.progress_bar.show()
        dm_size_px = (int(self.leWidth.text())-4,int(self.leHeight.text())-4)
        barcode_position_px = (2, 2)

        picture_size_px = (int(self.leWidth.text()),int(self.leHeight.text()))
        picture = Image.new('L', picture_size_px, color='white')

        dm_size_px = (int(self.leWidth.text())-4,int(self.leHeight.text())-4)
        barcode_position_px = (2, 2)

        picture_size_px = (int(self.leWidth.text()),int(self.leHeight.text()))
        picture = Image.new('L', picture_size_px, color='white')

        datamatrix = treepoem.generate_barcode(
                barcode_type='datamatrix',
                data=f"^FNC1{row['gs1dm']}",
                options={"parsefnc": True, "parse": True, "format": "square", "version": "26x26", "includetext": False})
        datamatrix = datamatrix.resize(dm_size_px, Image.NEAREST)
        picture.paste(datamatrix, barcode_position_px)

 
        return picture

    def accept(self):

        start = time()
        self.progress_bar.setFixedSize(self.geometry().width() - 120, 16)
        self.progress_bar.show()

        self.save_config()
        if self.options['MAIN']['output']:
            if not(os.path.exists(os.path.join(self.options['MAIN']['output'], self.parent.leGoodName.text(), self.subfolder)) or os.path.isdir(os.path.join(self.options['MAIN']['output'], self.parent.leGoodName.text(), self.subfolder))):
                os.mkdir(os.path.join(self.options['MAIN']['output'], self.parent.leGoodName.text(), self.subfolder))
            fname = os.path.join(self.options['MAIN']['output'],self.parent.leGoodName.text())
        else:
            if not(os.path.exists(os.path.join(os.getcwd(), self.parent.leGoodName.text(), self.subfolder)) or os.path.isdir(os.path.join(os.getcwd(), self.parent.leGoodName.text(), self.subfolder))):
                os.mkdir(os.path.join(os.getcwd(), self.parent.leGoodName.text(), self.subfolder))
            fname = os.path.join(os.getcwd(), self.parent.leGoodName.text())
        print(fname)
        if self.subfolder == 'group':
            codes = self.parent.data_frame_K['gs1dm'].tolist()
        else:
            codes = self.parent.data_frame['gs1dm'].tolist()
        count = 1
        
        dm_position_px = (int(self.leLeft.text()), int(self.leTop.text()))
        dm_size_px = (int(self.leWidth.text()),int(self.leHeight.text()))

        try: 
            back = Image.open(self.options['LABEL']['back'])#.convert("L")
            background = True
        except:
            back = Image.new("L", (int(self.leLabelWidth.text()), int(self.leLabelWidth.text())), 255)
            background = False

        #picture=back
        for code in codes:
            #back.show()
            picture = Image.new('L', (back.size), color=255)    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if background:
                #picture = back
                picture.paste(back, (0,0))
            #picture.show()
            label = self.validator(code)
            datamatrix = treepoem.generate_barcode(
                barcode_type='datamatrix',
                data=f"^FNC1{label}",
                options={"parsefnc": True, "parse": True, "format": "square", "version": "26x26", "includetext": False})
            datamatrix = datamatrix.resize(dm_size_px, Image.NEAREST)
            picture.paste(datamatrix, dm_position_px)
            
            
            
            if self.cbText.isChecked(): 
                font = ImageFont.truetype('sources/fonts/arialnb.ttf', int(self.sbFontSize.text()))
                #fontimage = Image.new('L', (font.font.getsize(label[16:label.find('9')])[0][0], sum(font.getmetrics())))   ##########
                draw = ImageDraw.Draw(picture)
                
                #ImageDraw.Draw(fontimage).text((0, 0), label[16:label.find('9')], fill=255, font=font)
                #ImageDraw.Draw(fontimage).text((0, 0), label[16:label.find('9')], fill=0, font=font)
                #!!!!fontimage = fontimage.rotate(int(self.cbTextRotate.currentText()), resample=Image.BICUBIC, expand=True)
                #picture.paste(mask=fontimage, box=(int(self.leTextLeft.text()), int(self.leTextTop.text())), im=0)
                
                draw.text((int(self.leTextLeft.text()), int(self.leTextTop.text())), label[16:label.find('9')], fill='black', font=font)

            picture.save(os.path.join(fname, str(count).zfill(len(str(len(codes))))+'.png'), optimize=True, quality=80)

            count += 1
            self.progress_bar.setValue(int(count/len(codes)*100))

        self.progress_bar.hide()
        self.parent.statusBar().showMessage(f'Готово! Время на подготовку кодов: {round(time()-start,2)}сек. Обработано кодов: {len(codes)}', 0)
        self.close()
    
    def validator(self, code):
        if '' not in code:
            return code[:25]+''+code[25:] 
        else:
            return code  
        

    def reject(self):
        self.close()

    def on_openBack_click(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","PNG files (*.png);;JPG files (*.jpg);;All Files (*)", options=options)
        if fileName:
            self.options['LABEL']['back'] = fileName
            self.leBack.setText(fileName)
        self.on_preview_click()

    def on_preview_click(self):
        barcode_size_px = (int(self.leWidth.text()), int(self.leHeight.text()))
        barcode_position_px = (int(self.leLeft.text()), int(self.leTop.text()))
        try: 
            back = Image.open(self.options['LABEL']['back'])#.convert("L")
            self.leLabelWidth.setText(str(back.size[0]))
            self.leLabelHeight.setText(str(back.size[1]))
        except:
            back = Image.new("RGB", (int(self.leLabelWidth.text()), int(self.leLabelWidth.text())), (255,255,255))#.convert("L")
        #label_size_px = (int(self.leLabelWidth.text()), int(self.leLabelWidth.text()))
        code = '01012345678901221999999993XXXX'
        datamatrix = treepoem.generate_barcode(
                barcode_type='datamatrix',
                data=f"^FNC1{code}",
                options={"parsefnc": True, "parse": True, "format": "square", "version": "26x26", "includetext": False})
        datamatrix = datamatrix.resize(barcode_size_px, Image.NEAREST)
        
        
        back.paste(datamatrix, barcode_position_px)
        if self.cbText.isChecked():   #Проверить на чистом Datamatrix
            label = self.leSampleText.text()
            font = ImageFont.truetype('sources/fonts/arialnb.ttf', int(self.sbFontSize.text()))
            fontimage = Image.new('L', (font.font.getsize(label)[0][0], sum(font.getmetrics())))   ##########
            ImageDraw.Draw(fontimage).text((0, 0), label, fill=255, font=font)
            fontimage = fontimage.rotate(int(self.cbTextRotate.currentText()), resample=Image.BICUBIC, expand=True)
            back.paste(mask=fontimage, box=(int(self.leTextLeft.text()), int(self.leTextTop.text())), im=0)
                    
        
        back.save('tmp.png')
        pixmap = QPixmap('tmp.png')
        pixmap = pixmap.scaled(self.lbImage.width(), self.lbImage.height(), Qt.KeepAspectRatio)
        self.lbImage.setPixmap(pixmap)
        self.lbImage.show()

    def on_default_click(self):
        self.leLabelWidth.setText('236')
        self.leLabelHeight.setText('236')
        self.leBack.setText('')
        self.leLeft.setText('80')
        self.leTop.setText('80')
        self.leWidth.setText('100')
        self.leHeight.setText('100')
        self.cbText.setChecked = False
        self.sbFontSize.setValue(18)
        self.cbTextRotate.setCurrentText('0')
        self.cbTextAllign.setCurrentText('0')
        self.leTextLeft.setText('80')
        self.leTextTop.setText('80')
        #self.gbZpl.setChecked = False
        #self.cbDMHeight.setCurrentText('6')
        #self.cbDMQuality.setCurrentText('ECC 200')
        #self.cbDMRotate.setCurrentText('0')

    def save_config(self):
        self.options['LABEL']['back'] = self.leBack.text()
        self.options['LABEL']['left'] = int(self.leLeft.text())
        self.options['LABEL']['top'] = int(self.leTop.text())
        self.options['LABEL']['width'] =int(self.leWidth.text())
        self.options['LABEL']['height'] = int(self.leHeight.text())
        self.options['LABEL']['label'] = bool(self.cbText.isChecked()) 
        self.options['LABEL']['font_size'] = int(self.sbFontSize.value())
        self.options['LABEL']['label_rotate'] = int(self.cbTextRotate.currentText())
        self.options['LABEL']['label_align'] = int(self.cbTextAllign.currentText())
        self.options['LABEL']['label_left'] = int(self.leTextLeft.text())
        self.options['LABEL']['label_top'] = int(self.leTextTop.text())
        
        #self.options['ZPL']['zpl'] = bool(self.gbZpl.isChecked()) 
        #self.options['ZPL']['code_size'] = int(self.cbDMHeight.currentText())
        #self.options['ZPL']['code_quality'] = self.cbDMQuality.currentText()
        #self.options['ZPL']['code_rotation'] = int(self.cbDMRotate.currentText())

        self.parent.options = self.options
