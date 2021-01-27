'''
Utilitários para conexão com o Mongo usado para armazenar e recuperar os schemas identificados pelo monitor
'''
import logging
import os
import pymongo
import pprint
# import connection

#####################################################################
## Funções
#####################################################################
# def getConnection() -> pymongo.MongoClient :
#     ''' Retorna a conexão com o MongoDB utilizado para ser monitorado '''
#     return _conexao

def getSchemaDBConnection() -> pymongo.MongoClient :
    ''' Retorna a conexão com o MongoDB utilizado para ser monitorado '''
    return _conexaoSchemaDB

def getSchemaCollection() -> pymongo.collection:
    ''' Retorna a coleção usada para armazenamento de schemas, para operações de I/O '''
    return _conexaoSchemaDB["mdbmmd"]["colecaoMongoV3"] 

def _conectMetadataDB( ) -> pymongo.MongoClient:
    ''' 
        Conecta e retorna a conexão com o servidor mongoDB a ser usado para gravar os Metadados dos Schemas
    '''
 
    # logging = logging.getLogger(__name__)
    # TODO: pegar o servidor mongo a partir de variavel ambiente os.environ['CHANGE_STREAM_DB']
    # username = urllib.parse.quote_plus('root')
    # password = urllib.parse.quote_plus('mongopass')
    _usernameSchemaDB = "root"
    _passwordSchemaDB = "mongopass"

    logging.debug('*** Conectando [SCHEMA_DB] -> mongodb://%s:*******@%s/admin?retryWrites=true',_usernameSchemaDB,_mongoServerSchemaDB)
    # print('*** Conectando [SCHEMA_DB]..',"mongodb://"+_usernameSchemaDB+":'password'@"+_mongoServerSchemaDB+"/admin?retryWrites=true")
    # client = pymongo.MongoClient("mongodb://root:mongopass@127.0.0.1/admin?retryWrites=true")
    # client = pymongo.MongoClient("mongodb://root:mongopass@"+os.environ['CHANGE_STREAM_DB']+"/admin?retryWrites=true")

    return pymongo.MongoClient(
        host = _mongoServerSchemaDB, # <-- IP and port go here
        serverSelectionTimeoutMS = 6000, # 3 second timeout
        username=_usernameSchemaDB,
        password=_passwordSchemaDB,
        authSource='admin', # TODO Mudar para o BD do schema, após criação de usuário específico autorizado para atualizar esse database/colleciton
        authMechanism='SCRAM-SHA-256')



##############################################################
# EXECUÇÃO INICIAL
##############################################################




logging.info("*"*40)
logging.info ("*** Configurando a Conexão ")
logging.info ("*"*40)


if not 'SCHEMA_DB' in os.environ:
    logging.error('Variável de ambiente SCHEMA_DB não localizada')
    raise OSError('Variável de ambiente SCHEMA_DB não localizada')

# Identificação das configurações de conexão
_mongoServerSchemaDB = os.environ['SCHEMA_DB'] 
logging.info ("*** SCHEMA_DB=%s",_mongoServerSchemaDB)

_conexaoSchemaDB = _conectMetadataDB()


print('\n',"*"*60,'\n **        MongoDB Server Information [SCHEMA_DB]         ***\n',"*"*60)
pprint.pprint(_conexaoSchemaDB.server_info())