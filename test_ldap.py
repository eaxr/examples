import sys
from ldap3 import Server, Connection, ObjectDef, AttrDef, Reader, Writer, ALL

ldapServer = sys.argv[1]
ldapDN = sys.argv[2]
ldapUser = sys.argv[3]
ldapPass = sys.argv[4]
ldapBaseDN = sys.argv[5]
ldapSearch = sys.argv[6]
ldapLogin = ldapDN + '\\' + ldapUser

host = Server(ldapServer)
connection = Connection(host, ldapLogin, ldapPass)
connection.open()

if connection.bind():
    print('Connected')
else:
    print('Not Connected')
    print(connection.result)

connection.search(ldapBaseDN, "(givenName={})".format(ldapSearch))
print(connection.entries)
