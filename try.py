# Printer status: ready, printing, error, and offline
# write function for green-ready, blue-printing, red-error, gray-anything

def printer_status(status_):
    return {'READY':'green',
            'PRINTING':'blue',
            'ERROR':'red'}.get(str(status_).upper(),'gray')

print(printer_status(input('Enter Printer Status: ')))