class Loggable():
    def __init__(self):
        self.title = '' 
    def log(self):
        print('log message from ' + self.title)

class Connection():
    def __init__(self):
        self.server = ''
    def connect(self):
        print('Connecting to database on ' + self.server)

def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item, Loggable):
        item.log()

class SqlDatabase(Connection, Loggable):
    def __init__(self):
        self.title = 'Sql Connection Demo'
        self.server = 'Some_server'

sql_connection = SqlDatabase()
framework(sql_connection)

class JustLog(Loggable):
    def __init__(self):
        self.title = 'Just Logging'


onlylog = JustLog()
framework(onlylog)