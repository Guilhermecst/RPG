
class ItemNaoExisteException(Exception):
    pass

'''
Parte 2: Consultas mais complexas
Temos um terceiro arquivo de acesso ao banco, 
chamado itens_do_heroi. Ele está importado
abaixo
Ele representa um relacionamento. Diz quais herois tem quais itens.

Verifique e se familiarize com a tabela ItemDoHeroi do banco de dados
'''
from sqlalchemy import create_engine
from sqlalchemy.sql import text


'''
Ex08
No arquivo itens_do_heroi, crie uma funçao heroi_tem_item.

Ela recebe uma id de heroi, e retorna True se o heroi
possui algum item, false caso contrário

Um heroi 10 tem o item 15 se na tabela itemDoHeroi
temos uma linha com idItem 15 e idHeroi 10
'''

#conexao
engine = create_engine('sqlite:///rpg.db')

def heroi_tem_item(idHeroi):
    with engine.connect() as con:
        statement = text("""SELECT * FROM ItemDoHeroi WHERE id = :idHeroi""") 
        rs = con.execute(statement, idHeroi=idHeroi) 
        itemHeroi = rs.fetchone()
        lista = list(itemHeroi)
        dicionario = dict(id=lista[0], idItem=lista[1], idHeroi=lista[2])
        if idHeroi == dicionario['idHeroi']:
            return True
        else:
            return False                  

'''
Ex09
No arquivo itens_do_heroi,
crie uma função heroi_quantos_itens, que recebe uma
id de heroi e diz quantos itens ele possui
'''

def heroi_quantos_itens(idHeroi):
     with engine.connect() as con:
        statement = text("""SELECT * FROM ItemDoHeroi WHERE idHeroi = :idHeroi""") 
        rs = con.execute(statement, idHeroi=idHeroi) 
        itemHeroi = rs.fetchall()
        lista = list(itemHeroi)
        return len(lista)


'''
Ex10

No arquivo itens_do_heroi,
crie uma funcao itens_do_heroi
Ela recebe a id do heroi e devolve uma lista com dicionarios, um para cada item dele.
Cada dicionário descreve um item 
Por exemplo, se o heroi 3 tem uma varinha com 2 de magia:
Chamar itens_do_heroi.itens_do_heroi(3) 
vai devolver a lista de dicionarios. Um desses dicionarios vai representar a varinha: 
ter chaves "tipo" com valor "varinha" e chave "magia" com valor 2


Dica: é possivel fazer com duas consultas, usando
o python para fazer o meio de campo, mas é mais
interessante e rápido usar um join
'''

def itens_do_heroi(idHeroi):
     with engine.connect() as con:
        statement = text("""SELECT * FROM Item
                            JOIN ItemDoHeroi
                            ON item.id = ItemDoHeroi.idItem
                            WHERE idheroi = :idHeroi""") 
        rs = con.execute(statement, idHeroi=idHeroi)
        itemHeroi = rs.fetchall()
        nova_lista = []
        for i in range(len(itemHeroi)):
            lista = list(itemHeroi[i])
            dicionario = dict(id=lista[0], nome=lista[1], tipo=lista[2], fisico=lista[3], magia=lista[4], agilidade=lista[5], emUso=lista[6])
            nova_lista.append(dicionario)
        return nova_lista

'''
Ex12
Funcao itens em uso por nome do heroi
Crie essa função no arquivo itens_do_heroi
Ela recebe uma string (o nome do heroi) e devolve uma lista (com os itens em uso do heroi)

Cada item é um dicionário descrevendo o item
Recomendo usar um join para fazer a consulta, mas terá que ter cuidado. Se fizer o join de forma desatenta, 
pode ser que os atributos do heroi sobrescrevam os do item (vide teste 12b)
'''

def itens_em_uso_por_nome_do_heroi(nomeHeroi):
    with engine.connect() as con:
        statement = text("""SELECT * FROM Item
                        JOIN ItemDoHeroi
                        ON Item.id = ItemDoHeroi.idItem
                        JOIN Heroi
                        ON ItemDoHeroi.idHeroi = Heroi.id
                        WHERE Heroi.nome = :nomeHeroi""") 
        rs = con.execute(statement, nomeHeroi=nomeHeroi)
        itemHeroi = rs.fetchall()
        nova_lista = []
        for i in range(len(itemHeroi)):
            lista = list(itemHeroi[i])
            dicionario = dict(id=lista[0], nome=lista[1], tipo=lista[2], fisico=lista[3], magia=lista[4], agilidade=lista[5], emUso=lista[6])
            if dicionario['emUso'] == 1:
                nova_lista.append(dicionario)
        return nova_lista


        


                
