dsname = "myDataSource"
url = "<DBURL>"
encryptedPassword = "<EncryptedPassword>"
dsusername = "<UserName>"
targetName = "<TargetName>"
targetType = "<TargetType>"

print "------------------------------------------------------------"
print " Weblogic Datasource creation script"
print "------------------------------------------------------------"
print "Connecting to Admin Server"
connect()
edit()
startEdit()

print "Creating the Datasource"
cd('/')
cmo.createJDBCSystemResource(dsname)


cd('/JDBCSystemResources/'+dsname+'/JDBCResource/'+dsname)
cmo.setName(dsname)
cmo.setDatasourceType('GENERIC')

print "Setting JNDI Name"
cd('/JDBCSystemResources/'+dsname+'/JDBCResource/'+dsname+'/JDBCDataSourceParams/'+dsname)
set('JNDINames',jarray.array([String('jdbc/'+dsname)], String))


print "Setting URL and Driver"
cd('/JDBCSystemResources/'+dsname+'/JDBCResource/'+dsname+'/JDBCDriverParams/'+dsname)
cmo.setUrl(url)
cmo.setDriverName('oracle.jdbc.OracleDriver')


print "Setting Encrypted Password"
set('PasswordEncrypted',encryptedPassword)


print "Setting Username"
cd('/JDBCSystemResources/'+dsname+'/JDBCResource/'+dsname+'/JDBCDriverParams/'+dsname+'/Properties/'+dsname)
cmo.createProperty('user')

cd('/JDBCSystemResources/'+dsname+'/JDBCResource/'+dsname+'/JDBCDriverParams/'+dsname+'/Properties/'+dsname+'/Properties/user')
cmo.setValue(dsusername)

print "Setting Transaction Type"
cd('/JDBCSystemResources/'+dsname+'/JDBCResource/'+dsname+'/JDBCDataSourceParams/'+dsname)
cmo.setGlobalTransactionsProtocol('OnePhaseCommit')

print "Setting Target"
cd('/JDBCSystemResources/'+dsname)
set('Targets',jarray.array([ObjectName('com.bea:Name='+ targetName +',Type=' + targetType)], ObjectName))

print "JDBC DataSource creation completed"
print "------------------------------------------------------------"

save()
activate()
