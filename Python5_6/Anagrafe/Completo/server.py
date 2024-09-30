from flask import Flask, json, request
from myjson import JsonSerialize,JsonDeserialize


# lListaCampil = ["nome", "cognome", "data nascita", "codice fiscale"]
# if campoRicevutoDalClient in lListaCampi:
    
sFileAnagrafe = "./anagrafe.json"
api = Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    #prendi i dati della richiesta
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type=="application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        print("Ricevuto " + sCodiceFiscale)
        #carichiamo l'anagrafe
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale not in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            JsonSerialize(dAnagrafe,sFileAnagrafe)
            jResponse = {"Error":"000", "Msg": "ok"}
            return json.dumps(jResponse),200
        else:
            jResponse = {"Error":"001", "Msg": "codice fiscale gia presente in anagrafe"}
            return json.dumps(jResponse),200
    else:
        return "Errore, formato non riconosciuto",401
    #controlla che il cittadino non è gia presente in anagrafe
    #rispondi

@api.route('/get_cittadino', methods=['POST'])
def StampaCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type=="application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        print("Ricevuto " + sCodiceFiscale)
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale in dAnagrafe:
            cittadino = dAnagrafe[sCodiceFiscale]
            return json.dumps(cittadino),200
        else:
            jResponse = {"Error":"001", "Msg": "cittadino non trovato"}
            return json.dumps(jResponse),200
    else:
        return "Errore, formato non riconosciuto",401

@api.route('/mod_cittadino', methods=['POST'])
def ModCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type=="application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        print("Ricevuto " + sCodiceFiscale)
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale in dAnagrafe:
            dAnagrafe[sCodiceFiscale] = jRequest
            JsonSerialize(dAnagrafe,sFileAnagrafe)
            jResponse = {"Error":"000", "Msg": "ok"}
            return json.dumps(jResponse),200
        else:
            jResponse = {"Error":"001", "Msg": "cittadino non trovato"}
            return json.dumps(jResponse),200
    else:
        return "Errore, formato non riconosciuto",401

@api.route('/del_cittadino', methods=['POST'])
def DelCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if content_type=="application/json":
        jRequest = request.json
        sCodiceFiscale = jRequest["codice fiscale"]
        print("Ricevuto " + sCodiceFiscale)
        dAnagrafe = JsonDeserialize(sFileAnagrafe)
        if sCodiceFiscale in dAnagrafe:
            del dAnagrafe[sCodiceFiscale]
            JsonSerialize(dAnagrafe,sFileAnagrafe)
            jResponse = {"Error":"000", "Msg": "ok"}
            return json.dumps(jResponse),200
        else:
            jResponse = {"Error":"001", "Msg": "cittadino non trovato"}
            return json.dumps(jResponse),200
    else:
        return "Errore, formato non riconosciuto",401

api.run(host="127.0.0.1", port=8080)