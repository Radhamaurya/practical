
import xmlrpc.client


db = "odoo"
username = "admin"
password = "admin"

common = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

if uid:
    print ("Connection Successful")

models = xmlrpc.client.ServerProxy('http://localhost:8069/xmlrpc/2/object')

# create recored
# models.execute_kw(db, uid, password, 'estate.property.type', 'create', [{'name': 'Place'}])

# search record
# to_confirm = models.execute_kw(db, uid, password,'estate.property.type', 'search',[[('name','=','Place')]])
# print ("\n\n to_confrim_id ::: ",to_confirm)

# update recored
# id = models.execute_kw(db, uid, password,'estate.property.type', 'search',[[('name','=','home')]])
# print("search::",id)

# result = models.execute_kw(db, uid, password, 'estate.property.type', 'write', [id, {'name': "HOUSE"}])
# print("RESULT:::", result)

# unlink record
id = models.execute_kw(db, uid, password, 'estate.property.type', 'unlink', [[2]])
print("\n\nunlink::",id)
# check if the deleted record is still in the database
# result = models.execute_kw(db, uid, password,'estate.property.type', 'search', [[['id', '=', id]]])