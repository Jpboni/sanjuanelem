import argparse
import datetime
import sys, os

class CertificatePrinterArguments:
  def __init__(self):
    parser = argparse.ArgumentParser(description='Input data to print the certificate')
    parser.add_argument("--first", help='Enter your first name: ', default = "NULL")
    parser.add_argument("--last", help='Enter your last name: ',  default = "NULL")
    parser.add_argument("--date", help='Enter date of completion in mm/dd/yyyy format: ', default = "NULL")
    parser.add_argument("--inFile", help='Input file path use "\\dir\\dir\\f.jpg"', default = "\\\\\\")
    parser.add_argument("--xtext", help='Positioning of name x coordinate: ', default = 450)
    parser.add_argument("--ytext", help='Positioning of name y coordinate: ', default = 320)
    parser.add_argument("--xdate", help='Positioning of date x coordinate: ', default = 275)
    parser.add_argument("--ydate", help='Positioning of date x coordinate: ', default = 735)
    parser.add_argument("--tFont", help='Font type for text: ', default = "arial.ttf")
    parser.add_argument("--sizeText", help='Font size for text: ', default = 50)
    parser.add_argument("--dFont", help='Font type for date', default = "arialbd.ttf")
    parser.add_argument("--sizeDate", help='Font size for date: ', default = 25)
    parser.add_argument("--RED", help='color value for RED ', default = 0)
    parser.add_argument("--GREEN", help='color value for GREEN ', default = 0)
    parser.add_argument("--BLUE", help='color value for BLUE ', default = 0)
    
    
    args = parser.parse_args()
    self.first =  args.first
    self.last = args.last
    self.date = args.date
    self.inFile = args.inFile
    self.xtext = int(args.xtext)
    self.ytext = int(args.ytext)
    self.xdate = int(args.xdate)
    self.ydate = int(args.ydate)
    self.tFont = args.tFont
    self.sizeText = int(args.sizeText)
    self.dFont = args.dFont
    self.sizeDate = int(args.sizeDate)
    self.RED = int(args.RED)
    self.GREEN = int(args.GREEN)
    self.BLUE = int(args.BLUE)
    
    if self.first =="NULL":
        self.first = str(input("Enter first name: "))
    if self.last=="NULL":
        self.last = str(input("Enter Last name: "))
    if self.date=="NULL":
        today = datetime.datetime.now()
        self.date = today.strftime("%m/%d/%Y")
  def Name(self):
    name = self.first+" "+self.last
    return ( name.title())
    
  def OutputFile(self):
    OutFile = self.date[:2]+self.date[3:5]+self.date[6:]+"_"+self.first+"_"+self.last+"_"+os.path.basename(self.inFile)
    return OutFile
    