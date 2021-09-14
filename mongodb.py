import logging
import pymongo
from datetime import date, datetime, timedelta
import urllib 

def insert_user(name, id_user):
    try:
        client = pymongo.MongoClient("mongodb+srv://admin:ne3438co@cluster0.jvfrn.mongodb.net/bot?retryWrites=true&w=majority")
        db = client.bot
        dados = {"name": name, "id_user": id_user}
        db.users.insert_one(dados)
        return True
    except Exception as e:
        print(e)
        return False
    
def insert_channels_groups(id_channels_groups,type,name):
    try:
        client = pymongo.MongoClient("mongodb+srv://admin:ne3438co@cluster0.jvfrn.mongodb.net/bot?retryWrites=true&w=majority")
        db = client.bot
        dados = {"id_channels_groups": id_channels_groups, "type": type,"name":name}
        db.channels_groups.insert_one(dados)
        return True
    except Exception as e:
        print(e)
        return False

def insert(id_telegram, email, username, senha, token):
    try:

        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl

        dados = {"id_telegram": id_telegram, "username": username, 'saldo': 0.14,
                 "email": email, 'senha': senha, 'token': token}
        db.users.insert_one(dados)
        return True
    except Exception as e:
        print(e)
        return False


def insert_pix(id_telegram, txid, status, valor, qrcode, imagemQrcode):
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl

        dados = {"id_telegram": id_telegram, "status": status,
                 "txid": txid, 'valor': valor, "qrcode": qrcode, "imagemQrcode": imagemQrcode}
        db.pix.insert_one(dados)
        return True
    except Exception as e:
        print(e)
        return False


def get_site(name):

    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.bot_tiktok

        result = list(db.sites.find({'name': name}))

        return result
    except Exception as e:
        print(e)
        return []
def update_teste():
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.bot_tiktok
        acao = list(db.contas.find())
        for item in acao:
            db.contas.update_one({"id_site": item['id_site']}, {'$set': {"running": False}}, upsert=False)

    except Exception as e:
        print(e)
        return False
    else:
        True

def update_acao(id_site):
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.bot_tiktok
        acao = list(db.contas.find({"id_site": id_site}))
        db.contas.update_one({"id_site": id_site}, {
                             '$set': {"acao_realizada": int(acao[0]['acao_realizada'])+1}}, upsert=False)

    except Exception as e:
        print(e)
        return False
    else:
        True
def update_running(id_site,runn):
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.bot_tiktok
        db.contas.update_one({"id_site": id_site}, {'$set': {"running": runn}}, upsert=False)

    except Exception as e:
        print(e)
        return False
    else:
        True

def update_data(id_site,data):
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.bot_tiktok
        db.contas.update_one({"id_site": id_site}, {'$set': {"ultima_acao": data}}, upsert=False)

    except Exception as e:
        print(e)
        return False
    else:
        True

def update_zera_acao(id_site):
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.bot_tiktok
        db.contas.update_one({"id_site": id_site}, {
                             '$set': {"acao_realizada": 0}}, upsert=False)

    except Exception as e:
        print(e)
        return False
    else:
        True

def get_conta_one(id_site):
    
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.bot_tiktok
        query = db.contas.find({"id_site":id_site})
        result = list(query)
        return result[0]

    except Exception as e:
        print(e)
        return []

def get_conta():

    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.bot_tiktok
        query = db.contas.find()
        result = list(query)
        dados = []
        for item in result:
            date_atual = datetime.now()
            if date_atual > item['ultima_acao'] and item['running'] == False:
                dados.append(item)
            
        return dados[0]

    except Exception as e:
        print(e)
        return []


def get_services(servidor, name):

    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl

        result = list(db.services.find({'servidor': servidor, "name": name}))

        return result
    except Exception as e:
        print(e)
        return []


def all_services():
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl

        result = list(db.services2.find())

        return result
    except Exception as e:
        print(e)
        return []


def get_service(id_service):

    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl
        res = db.services2.find({"id_service": id_service})
        result = list(res)

        return result
    except Exception as e:
        print(e)
        return []


def get_pix():

    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl

        result = list(db.pix.find({'status': 'aberto'}))

        return result
    except Exception as e:
        print(e)
        return False


def update_pix(txid):

    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl
        db.pix.update_one(
            {'txid': txid}, {'$set': {'status': 'fechado'}}, upsert=False)

        return True
    except Exception as e:
        print(e)
        return False


def update_saldo(id_telegram, saldo):

    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl
        db.users.update_one({'id_telegram': id_telegram}, {
                            '$set': {'saldo': saldo}}, upsert=False)

        return True
    except Exception as e:
        print(e)
        return False


def update_services2(id_service, dados):

    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl
        db.services2.update_one({'id_telegram': id_service}, {
            '$set': dados}, upsert=False)

        return True
    except Exception as e:
        print(e)
        return False


def update_token(id, token):

    try:

        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl

        db.users.update_one({"id_telegram": id}, {
                            '$set': {'token': token}}, upsert=False)

        return True
    except Exception as e:
        return False


def get_token(id):

    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl
        result = list(db.users.find({'id_telegram': id}))
        return result
    except Exception as e:
        print(e)
        return False


def get_id(id):
    try:

        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl

        result = list(db.users.find({'id_telegram': id}))
        return result
    except Exception as e:
        return False


def insert_sms(status, id_telegram, id_service, servidor, id, sms_service_name, country_code, phone):
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl

        dados = {"status": status, "id_telegram": id_telegram, "id_service": id_service, "servidor": servidor, "id": id, "sms_service_name": sms_service_name, 'country_code': country_code,
                 "phone": phone, "msg": ""}

        db.sms.insert_one(dados)
        return True
    except Exception as e:
        print(e)
        return False


def get_sms_pedido(id):
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl
        result = list(db.sms.find({"id": int(id)}))
        return result
    except Exception as e:
        print(e)
        return []


def get_sms(id_telegram):
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl
        result = list(db.sms.find(
            {"id_telegram": id_telegram, 'status': 'aguardando'}))
        return result
    except Exception as e:
        print(e)
        return False


def update_sms(id, status, msg):
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl
        db.sms.update_one(
            {"id": id}, {'$set': {'status': status, 'msg': msg}}, upsert=False)
        return True
    except Exception as e:
        print(e)
        return False


def log_event(id_service, phone):
    try:
        client = pymongo.MongoClient(
            "mongodb://fabiano:Wd4CeFIIrRyM8vUJ7D2YXTKj@95.216.245.14:27017")
        db = client.smsbrl
        teste = db.log_event.create_index("createdAt", expireAfterSeconds=10)
        db.log_event.insert({
            "createdAt": datetime.now(),
            "logEvent": 1,
            "logMessage": "Success!"
        })
        return True
    except Exception as e:
        print(e)
