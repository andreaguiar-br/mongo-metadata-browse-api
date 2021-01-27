from connectionSchema import getSchemaCollection

def getDatabases():
    ''' 
    Recupera lista de databases 
    '''

    schemaCollection = getSchemaCollection()
    
    resultSet = schemaCollection.aggregate([
        {"$project":{ "chave":{"$concat":["$nomeServidor",".","$nomeDatabase"]}, "nomeDatabase":1,"nomeServidor":1,"nomeFisico":1}},
        {"$group":{"_id": "$chave", "nomeServidor":{"$first": "$nomeServidor"}, "nomeDatabase":{"$first": "$nomeDatabase" }, "qtColecoes":{"$sum":1}}},
        {"$project":{"_id":0}}])

    resultado = []
    qtReg = 0
    for registros in resultSet:
        # print("Retorno:",registros)
        resultado.append(registros)
        qtReg += 1
    # print(resultado)
    return { 'quantidadeRegistros': qtReg, "registros": resultado }


def getCollections(database: str, servidor: str):

    schemaCollection = getSchemaCollection()
    docMatch = {}
    if database is not None:
        docMatch["nomeDatabase"]=database
    if servidor is not None:
        docMatch["nomeServidor"]=servidor
    # print("docMatch=",docMatch)
    resultSet = schemaCollection.aggregate([
        {"$match":docMatch},
        {"$project":{ "estrutura":0, "_id":0}}])
        # {"$group":{"_id": "$chave", "nomeServidor":{"$first": "$nomeServidor"}, "nomeDatabase":{"$first": "$nomeDatabase" }, "nomeFisico":{"$first": "$nomeDatabase" }}},
        # {"$project":{"_id":0}}])

    resultado = []
    qtReg = 0
    for registros in resultSet:
        # print("Retorno:",registros)
        resultado.append(registros)
        qtReg += 1
    # print(resultado)
    return { 'quantidadeRegistros': qtReg, "registros": resultado }