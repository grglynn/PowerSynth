import sys, csv
from PySide.QtGui import *

app = QApplication(sys.argv)
self = QWidget()

with open('input_data.csv', mode = 'w') as input_data:
    input_writer = csv.writer(input_data, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    name, ok = QInputDialog.getText(self, "PowerSynth", """Please Enter the Name of the User""")
    if ok:
        gpa, ok = QInputDialog.getDouble(self, "PowerSynth", """Please Enter the GPA of the User""")
        if ok:
            school, ok = QInputDialog.getText(self, "PowerSynth", """Please Enter the School of the User""")
            input_writer.writerow([name, gpa, school])
            app.exit()
        else:
            app.exit()

    else:
        app.exit()

sys.exit()