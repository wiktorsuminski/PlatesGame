
from flask import Flask, render_template, request, session, url_for, redirect
import random
import string

app = Flask(__name__)
app.secret_key = "TestowyKlucz"
random.seed(1)
plateDistricts = {'BI': 'białystok', 'BS': 'suwałki', 'BL': 'łomża', 'BAU': 'powiat augustowski', 'BIA': 'powiat białostocki', 'BBI': 'powiat bielski',
                  'BGR': 'powiat grajewski', 'BHA': 'powiat hajnowski', 'BKL': 'powiat kolneński', 'BMN': 'powiat moniecki', 'BSE': 'powiat sejneński',
                  'BSI': 'powiat siemiatycki', 'BSK': 'powiat sokólski', 'BSU': 'powiat suwalski', 'BWM': 'powiat wysokomazowiecki', 'BZA': 'powiat zambrowski',
                  'BLM': 'powiat łomżyński', 'CB': 'bydgoszcz', 'CG': 'grudziądz', 'CT': 'toruń', 'CW': 'włocławek', 'CAL': 'powiat aleksandrowski',
                  'CBR': 'powiat brodnicki', 'CBY': 'powiat bydgoski', 'CCH': 'powiat chełmiński', 'CGD': 'powiat golubsko-dobrzyński', 'CGR': 'powiat grudziącki',
                  'CIN': 'powiat inowrocławski', 'CLI': 'powiat lipnowski', 'CMG': 'powiat mogileński', 'CNA': 'powiat nakielski', 'CRA': 'powiat radziejowski',
                  'CRY': 'powiat rypiński', 'CSE': 'powiat sępoleński', 'CSW': 'powiat świecki', 'CTR': 'powiat toruński', 'CTU': 'powiat tucholski', 'CWA': 'powiat wąbrzeski',
                  'CWL': 'powiat włocławski', 'CZN': 'powiat żniński', 'DJ': 'jelenia góra', 'DL': 'legnica', 'DB': 'wałbrzych', 'DW': 'wrocław', 'DBL': 'powiat bolesławiecki',
                  'DDZ': 'powiat dzierżoniowski', 'DGR': 'powiat górowski', 'DGL': 'powiat głogowski', 'DJA': 'powiat jaworski', 'DJE': 'powiat jeleniogórski', 'DKA': 'powiat kamiennogórski',
                  'DKL': 'powiat kłodzki', 'DLE': 'powiat legnicki', 'DLB': 'powiat lubański', 'DLU': 'powiat lubiński', 'DLW': 'powiat lwówecki', 'DMI': 'powiat milicki',
                  'DOL': 'powiat oleśnicki', 'DOA': 'powiat oławski', 'DPL': 'powiat polkowicki', 'DSR': 'powiat średzki', 'DST': 'powiat strzeliński', 'DSW': 'powiat świdnicki',
                  'DTR': 'powiat trzebnicki', 'DBA': 'powiat wałbrzyski', 'DWL': 'powiat wołowski', 'DWR': 'powiat wrocławski', 'DZA': 'powiat ząbkowicki', 'DZG': 'powiat zgorzelecki',
                  'DZL': 'powiat złotoryjski'

                  }


def plateNumberGenerator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


score = int()


@app.route('/', methods=["GET", "POST"])
def home():
    global score
    lastPlateDistrict = session.get('lastPlateDistrict', None)
    if request.form.get('userAnswer'):
        userAnswer = request.form.get('userAnswer')
        if lastPlateDistrict != None:
            if userAnswer == plateDistricts[lastPlateDistrict.split(' ', 1)[0]]:
                userAnswer = 'Dobrze'
                score += 1
                del plateDistricts[lastPlateDistrict.split(' ', 1)[0]]
            else:
                userAnswer = "Źle"
    else:
        if lastPlateDistrict == None:
            userAnswer = ''
        else:
            userAnswer = 'Źle'
    if len(plateDistricts) > 0:
        newPlateDistrict = random.choice(list(plateDistricts.items()))
        newPlate = newPlateDistrict[0]+" "+plateNumberGenerator()
        session['lastPlateDistrict'] = newPlate
        return render_template('index.html', newPlate=newPlate, userAnswer=userAnswer, score=score, newPlateDistrict=newPlateDistrict)
    else:
        wynik = "Koniec gry"
        newPlate = wynik
        return render_template('index.html', newPlate=newPlate, userAnswer=userAnswer, score=score)


@app.route('/clear')
def clear():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
