from sqlalchemy import create_engine


def conexionDB():

    '''
    establece la conexion con la base de datos y retorna esta conexion
    para poder hacer uso libre de esta en los metodos de la API
    '''

    engine = create_engine("mysql+pymysql://root:K0tpopAmmbwax1XfGPKz"+
        "@containers-us-west-151.railway.app:7171/railway")
    conexion = engine.connect()
    return conexion


def motor():

    '''
    Este metodo crea el motor de trabajo de la base de datos para
    poder realizar la interaccion con esta misma
    '''

    engine = create_engine("mysql+pymysql://root:K0tpopAmmbwax1XfGPKz"+
        "@containers-us-west-151.railway.app:7171/railway")
    return engine
