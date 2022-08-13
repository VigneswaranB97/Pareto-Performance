files = ['Applications Development.json',
         'Applications Maintenance.json',
         'Mainframe services.json',
         'Managed Services.json',
         'Service Desk.json',
         'Support.json']

with open('supplier_details.json', "w") as outfile:
    outfile.write('{}'.format('\n'.join([open(f, "r").read() for f in files])))
