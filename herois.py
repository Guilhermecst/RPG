
# Essa classe só representa uma exception com
#novo nome. Não mexa dentro dela.
# Escreva os imports (acima dela)
# E suas funcoes (depois dela)

from sqlalchemy import create_engine
from sqlalchemy.sql import text

class HeroiNaoExisteException(Exception):
    pass

#escreva suas funcoes aqui

#iniciar conexão
engine = create_engine('sqlite:///rpg.db')


'''
Ex1
O arquivo herois deve conter uma função heroi_existe
Ela recebe uma id de herói e consulta no banco para ver
se o herói em questão existe. Ela retorna True
se ele existe, False caso contrário
'''

def heroi_existe(id):
        with engine.connect() as con:
            statement = text("""SELECT * FROM Heroi WHERE id = :id""") 
            rs = con.execute(statement, id=id) 
            heroi = rs.fetchone()                  
            if heroi == None:                       
                return False
            return True

'''
Ex2
O arquivo herois deve conter uma funcao 
consultar_heroi.
ela recebe uma id de heroi e retorna 
um dicionario com todos os dados do heroi
(por exemplo, a chave 'nome' conterá o valor
da coluna 'nome' associada a essa id).

se receber uma id invalida, a funcao levanta 
uma HeroiNaoExisteException 
'''           

def consultar_heroi(id):
    with engine.connect() as con:
        statement = text("""SELECT * FROM Heroi WHERE id = :id""") 
        rs = con.execute(statement, id=id) 
        heroi = rs.fetchone()                 
        if heroi == None:                       
            raise HeroiNaoExisteException
        return dict(heroi) 
