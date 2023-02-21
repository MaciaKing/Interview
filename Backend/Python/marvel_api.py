
import requests
import json
import database
import hashlib
import time


def escape_values(string_to_scape):
    '''
    Escape the values ' for the insert in database on postgresql
    '''
    return string_to_scape.replace("'", "\'")


if __name__ == '__main__':
    ts = 1
    public_key = "b6d14e00e9a9f68e94900531a34ae1df"
    private_key = "6bfba275a878af3f173b91a0f255c07950e6ba95"

    # Generar un hash MD5 usando las claves pública y privada
    #md5_hash = hashlib.md5()
    #hash_value = hashlib.md5((timestamp + private_key + public_key).encode('utf-8')).hexdigest()
    #hash_value = md5_hash.hexdigest()
    # 16bfba275a878af3f173b91a0f255c07950e6ba95b6d14e00e9a9f68e94900531a34ae1df
    hash = "b6f3d6c96a1e61cafed3dcb9b158bfc7"

    # URL para solicitar una lista de personajes de Marvel
    url = 'http://gateway.marvel.com/v1/public/characters?ts={}&apikey={}&hash={}'.format(  ts, public_key, hash)

    # Realizar la solicitud HTTP
    response = requests.get(url)
    if response.status_code != 200:
        print("Error en la solicitud")
        exit()

    # Obtener los datos de la respuesta en formato JSON
    data = json.loads(response.text)

    all_inserts = []

    # Imprimir la lista de personajes
    for i in data['data']['results']:
        name = escape_values(i['name'])
        description = escape_values(i['description'])
        comics = i['comics']['available']
        series = i['series']['available']
        thumbnail = i['thumbnail']['path'] + "." + i['thumbnail']['extension']

        all_inserts.append("INSERT INTO hero (name, n_comics, n_series, thumbnail) VALUES ('{}', {}, {}, '{}')".format(
            name,  comics, series, thumbnail))

# print(all_inserts)
db = database.Database("macia", "maica", "localhost", "marvel")
final_insert = db.join_all_inserts(all_inserts)
print(final_insert)
db.make_insert_database([final_insert+";"])
