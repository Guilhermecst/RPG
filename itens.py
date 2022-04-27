
class ItemNaoExisteException(Exception):
    pass


from sqlalchemy import create_engine
from sqlalchemy.sql import text

'''
Ex3
O arquivo itens.py
deve conter uma funcao consultar_item.
ela recebe uma id de item e retorna 
um dicionario com todos os dados do item
(por exemplo, a chave 'nome' conterá o valor
da coluna 'nome' associada a essa id).

se receber uma id invalida, a funcao levanta 
uma ItemNaoExisteException (que voce deverá
criar)

(já fizemos coisa parecida no heroi. Lá, foram
3 testes, agora é um só testando tudo!)
'''

#iniciar conexão
engine = create_engine('sqlite:///rpg.db')

def consultar_item(id):
    with engine.connect() as con:
        statement = text("""SELECT * FROM Item WHERE id = :id""") 
        rs = con.execute(statement, id=id) 
        item = rs.fetchone()              
        if item == None:                       
            raise ItemNaoExisteException
        lista = list(item)
        dicionario = dict(id=lista[0], nome=lista[1], tipo=lista[2], fisico=lista[3], magia=lista[4], agilidade=lista[5], emUso=lista[6])
        return dicionario


def nome_para_id_item(nome_item):
    with engine.connect() as con:
        statement = text("""SELECT id FROM Item WHERE nome = :nome_item""") 
        rs = con.execute(statement, nome_item=nome_item)
        nome = rs.fetchone()
        item_id = nome[0]
    return item_id


def criar_item(tipo, nome,fisico,agilidade,magia):
    with engine.connect() as con:    
        statement = "INSERT INTO Item (tipo, nome, fisico, agilidade, magia, emUso) VALUES (:tipo,:nome,:fisico,:agilidade,:magia, :emUso)"
        con.execute(statement, tipo=tipo, nome=nome, agilidade=agilidade, fisico=fisico, magia=magia, emUso=0)
