from flask import Flask, render_template, request, session, url_for, redirect
from flask_session import Session
import random
import string
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/users_scores.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "testowyklucz"
SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

db = SQLAlchemy(app)


class users_scores(db.Model):
    score_id = db.Column('ScoreID', db.Integer, primary_key=True)
    score_user = db.Column(db.String(100))
    score_score = db.Column(db.String(100))

    def __init__(self, score_user, score_score):
        self.score_user = score_user
        self.score_score = score_score


random.seed(random.randint(0, 999999))
all_plate_districts = {'BI': 'białystok', 'BS': 'suwałki', 'BL': 'łomża', 'BAU': 'powiat augustowski', 'BIA': 'powiat białostocki', 'BBI': 'powiat bielski',
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
                       'DZL': 'powiat złotoryjski', 'EP': 'piotrków trybunalski', 'ES': 'skierniewice', 'EL': 'łódź', 'EBE': 'powiat bełchatowski', 'EBR': 'powiat brzeziński',
                       'EKU': 'powiat kutnowski', 'EOP': 'powiat opoczyński', 'EPA': 'powiat pabianicki', 'EPJ': 'powiat pajęczański', 'EPI': 'powiat piotrkowski', 'EPD': 'powiat poddębicki',
                       'ERA': 'powiat radomszczański', 'ERW': 'powiat rawski', 'ESI': 'powiat sieradzki', 'ESK': 'powiat skierniewicki', 'ETM': 'powiat tomaszowski', 'EWI': 'powiat wieluński',
                       'EWE': 'powiat wieruszowski', 'EZD': 'powiat zduńskowolski', 'EZG': 'powiat zgierski', 'ELA': 'powiat łaski', 'ELE': 'powiat łęczycki', 'ELW': 'powiat łódzki wschodni',
                       'ELC': 'powiat łowicki', 'FG': 'gorzów wielkopolski', 'FZ': 'zielona góra', 'FGW': 'powiat gorzowski', 'FKR': 'powiat krośnieński', 'FMI': 'powiat międzyrzecki',
                       'FNW': 'powiat nowosolski', 'FSD': 'powiat strzelecko-drezdenecki', 'FSU': 'powiat sulęciński', 'FSW': 'powiat świebodziński', 'FSL': 'powiat słubicki',
                       'FWS': 'powiat wschowski', 'FZG': 'powiat żagański', 'FZA': 'powiat żarski', 'FZI': 'powiat zielonogórski', 'GD': 'gdańsk', 'GA': 'gdynia', 'GSP': 'sopot',
                       'GS': 'słupsk', 'GBY': 'powiat bytowski', 'GCH': 'powiat chojnicki', 'GCZ': 'powiat człuchowski', 'GDA': 'powiat gdański', 'GKA': 'powiat kartuski',
                       'GKS': 'powiat kościerski', 'GKW': 'powiat kwidzyński', 'GLE': 'powiat lęborski', 'GMB': 'powiat malborski', 'GND': 'powiat nowodworski', 'GPU': 'powiat pucki',
                       'GST': 'powiat starogardzki', 'GSZ': 'powiat sztumski', 'GSL': 'powiat słupski', 'GTC': 'powiat tczewski', 'GWE': 'powiat wejherowski', 'GWO': 'powiat wejherowski',
                       'KR': 'kraków', 'KK': 'kraków', 'KN': 'nowy sącz', 'KT': 'tarnów', 'KBC': 'powiat bocheński', 'KBA': 'powiat bocheński', 'KBR': 'powiat brzeski', 'KCH': 'powiat chrzanowski',
                       'KDA': 'powiat dąbrowski', 'KGR': 'powiat gorlicki', 'KRA': 'powiat krakowski', 'KLI': 'powiat limanowski', 'KMI': 'powiat miechowski', 'KMY': 'powiat myślenicki',
                       'KNS': 'powiat nowosądecki', 'KNT': 'powiat nowotarski', 'KOL': 'powiat olkuski', 'KOS': 'powiat oświęcimski', 'KPR': 'powiat proszowicki', 'KSU': 'powiat suski',
                       'KTA': 'powiat tarnowski', 'KTT': 'powiat tatrzański', 'KWA': 'powiat wadowicki', 'KWI': 'powiat wielicki', 'LB': 'biała podlaska', 'LC': 'chełm', 'LU': 'lublin',
                       'LZ': 'zamość', 'LBI': 'powiat bialski', 'LBL': 'powiat biłgorajski', 'LCH': 'powiat chełmski', 'LHR': 'powiat hrubieszowski', 'LJA': 'powiat janowski',
                       'LKR': 'powiat kraśnicki', 'LKS': 'powiat krasnostawski', 'LLB': 'powiat lubartowski', 'LUB': 'powiat lubelski', 'LOP': 'powiat opolski', 'LPA': 'powiat parczewski',
                       'LPU': 'powiat puławski', 'LRA': 'powiat radzyński', 'LRY': 'powiat rycki', 'LSW': 'powiat świdnicki', 'LTM': 'powiat tomaszowski', 'LWL': 'powiat włodawski',
                       'LZA': 'powiat zamojski', 'LLE': 'powiat łęczyński', 'LLU': 'powiat łukowski', 'NE': 'elbląg', 'NO': 'olsztyn', 'NBA': 'powiat bartoszycki', 'NBR': 'powiat braniewski',
                       'NDZ': 'powiat działdowski', 'NEB': 'powiat elbląski', 'NEL': 'powiat ełcki', 'NGI': 'powiat giżycki', 'NGO': 'powiat gołdapski', 'NIL': 'powiat iławski',
                       'NKE': 'powiat kętrzyński', 'NLI': 'powiat lidzbarski', 'NMR': 'powiat mrągowski', 'NNI': 'powiat nidzicki', 'NNM': 'powiat nowomiejski', 'NOE': 'powiat olecki',
                       'NOL': 'powiat olsztyński', 'NOS': 'powiat ostródzki', 'NPI': 'powiat piski', 'NSZ': 'powiat szczycieński', 'NWE': 'powiat węgorzewski',
                       'OP': 'opole', 'OB': 'powiat brzeski', 'OGL': 'powiat głubczycki', 'OK': 'powiat kędzierzyńsko-kozielski', 'OKL': 'powiat kluczborski', 'OKR': 'powiat krapkowicki',
                       'ONA': 'powiat namysłowski', 'ONY': 'powiat nyski', 'OOL': 'powiat oleski', 'OPO': 'powiat opolski', 'OPR': 'powiat prudnicki', 'OST': 'powiat strzelecki',
                       'PK': 'kalisz', 'PN': 'konin', 'PL': 'leszno', 'PO': 'poznań', 'PY': 'poznań', 'PCH': 'powiat chodzieski', 'PCT': 'powiat czarnkowsko-trzcianecki', 'PGN': 'powiat gnieźnieński',
                       'PGS': 'powiat gostyński', 'PGO': 'powiat grodziski', 'PJA': 'powiat jarociński', 'PKA': 'powiat kaliski', 'PKE': 'powiat kępiński', 'PKL': 'powiat kolski',
                       'PKN': 'powiat koniński', 'PKS': 'powiat kościański', 'PKR': 'powiat krotoszyński', 'PLE': 'powiat leszczyński', 'PMI': 'powiat międzychodzki', 'PNT': 'powiat nowotomyski',
                       'POB': 'powiat obornicki', 'POS': 'powiat ostrowski', 'POT': 'powiat otrzeszowski', 'PP': 'powiat pilski', 'PPL': 'powiat pleszewski', 'PZ': 'powiat poznański',
                       'PRA': 'powiat rawicki', 'PSR': 'powiat średzki', 'PSE': 'powiat śremski', 'PSZ': 'powiat szamotulski', 'PSL': 'powiat słupecki', 'PTU': 'powiat turecki',
                       'PWA': 'powiat wągrowiecki', 'PWL': 'powiat wolsztyński', 'PWR': 'powiat wrzesiński', 'PZL': 'powiat złotowski', 'PK': 'krosno', 'RP': 'przemyśl',
                       'RZ': 'rzeszów', 'RT': 'tarnobrzeg', 'RBI': 'powiat bieszczadzki', 'RBR': 'powiat brzozowski', 'RDE': 'powiat dębicki', 'RJA': 'powiat jarosławski',
                       'RJS': 'powiat jasielski', 'RKL': 'powiat kolbuszowski', 'RKR': 'powiat krośnieński', 'RLS': 'powiat leski', 'RLE': 'powiat leżajski', 'RLU': 'powiat lubaczowski',
                       'RMI': 'powiat mielecki', 'RNI': 'powiat niżański', 'RPR': 'powiat przemyski', 'RPZ': 'powiat przeworski', 'RRS': 'powiat ropczycko-sędziszowski', 'RZE': 'powiat rzeszowski',
                       'RSA': 'powiat sanocki', 'RST': 'powiat stalowowolski', 'PSR': 'Powiat strzyżowski', 'RTA': 'powiat tarnobrzeski', 'RLA': 'powiat łańcucki', 'SB': 'bielsko-biała',
                       'SY': 'bytom', 'SH': 'chorzów', 'SC': 'częstochowa', 'SD': 'dąbrowa górnicza', 'SG': 'gliwice', 'SJZ': 'jastrzębie-zdrój', 'SJ': 'jaworzno', 'SK': 'katowice', 'SM': 'mysłowice',
                       'SPI': 'piekary śląskie', 'SL': 'ruda śląska', 'SR': 'rybnik', 'SI': 'siemianowice śląskie', 'SO': 'sosnowiec', 'SW': 'świętochłowice', 'ST': 'tychy', 'SZ': 'zabrze', 'SZO': 'żory',
                       'SBE': 'powiat będziński', 'SBI': 'powiat bielski', 'SBL': 'powiat bieruńsko-lędziński', 'SCI': 'powiat cieszyński', 'SCZ': 'powiat częstochowski', 'SGL': 'powiat gliwicki',
                       'SKL': 'powiat kłobucki', 'SLU': 'powiat lubliniecki', 'SMI': 'powiat mikołowski', 'SMY': 'powiat myszkowski', 'SPS': 'powiat pszczyński', 'SRC': 'powiat raciborski',
                       'SRB': 'powiat rybnicki', 'STA': 'powiat tarnogórski', 'SWD': 'powiat wodzisławski', 'SWZ': 'powiat wodzisławski', 'SZA': 'powiat zawierciański', 'SZY': 'powiat żywiecki',
                       'TK': 'kielce', 'TBU': 'powiat buski', 'TJE': 'powiat jędrzejowski', 'TKA': 'powiat kazimierski', 'TKI': 'powiat kielecki', 'TKN': 'powiat konecki', 'TOP': 'powiat opatowski',
                       'TOS': 'powiat ostrowiecki', 'TPI': 'powiat pińczowski', 'TSA': 'powiat sandomierski', 'TSK': 'powiat skarżyski', 'TST': 'powiat starachowicki', 'TSZ': 'powiat staszowski',
                       'TLW': 'powiat włoszczowski', 'WO': 'ostrołęka', 'WP': 'płock', 'WR': 'radom', 'WS': 'siedlce', 'WB': 'warszawa bemowo', 'WA': 'warszawa białołęka', 'WD': 'warszawa bielany',
                       'WE': 'warszawa mokotów', 'WU': 'warszawa ochota', 'WH': 'warszawa praga północ', 'WF': 'warszawa praga południe', 'WW': ['warszawa rembertów', 'warszawa wilanów', 'warszawa włochy'],
                       'WI': 'warszawa śródmieście', 'WJ': 'warszawa targówek', 'WK': 'warszawa ursus', 'WN': 'warszawa ursynów', 'WT': 'warszawa wawer', 'WX': ['warszawa wesoła', 'warszawa żoliborz'],
                       'WY': 'warszawa wola', 'WBR': 'powiat białobrzeski', 'WCI': 'powiat ciechanowski', 'WG': 'powiat garwoliński', 'WGS': 'powiat gostyniński', 'WGM': 'powiat grodzicki',
                       'WGR': 'powiat grójecki', 'WKZ': 'powiat kozienicki', 'WL': 'powiat legionowski', 'WLI': 'powiat lipski', 'WMA': 'powiat makowski', 'WM': 'powiat miński', 'WML': 'powiat mławski',
                       'WND': 'powiat nowodworski', 'WOR': 'powiat ostrowski', 'WOS': 'powiat ostrołęcki', 'WOT': 'powiat otwocki', 'WPI': 'powiat pasieczyński', 'WPR': 'powiat pruszkowski',
                       'WPP': 'powiat pruszkowski', 'WPS': 'powiat pruszkowski', 'WPZ': 'powiat przasnyski', 'WPY': 'powiat przysuski', 'WPU': 'powiat pułtuski', 'WPL': 'powiat płocki',
                       'WPN': 'powiat płoński', 'WRA': 'powiat radomski', 'WSI': 'powiat siedlecki', 'WSE': 'powiat serpecki', 'WSC': 'powiat sochaczewski', 'WSK': 'powiat sokołowski',
                       'WSZ': 'powiat szydłowiecki', 'WZ': 'powiat warszawski zachodni', 'WWE': 'powiat węgrowski', 'WWL': 'powiat wołomiński', 'WV': 'powiat wołomiński',
                       'WWY': 'powiat wyszkowski', 'WZU': 'powiat żuromiński', 'WZW': 'powiat zwoleński', 'WZY': 'powiat żyrardowski', 'WLS': 'powiat łosicki', 'ZK': 'koszalin',
                       'ZSW': 'świnoujście', 'ZS': 'szczecin', 'ZZ': 'szczecin', 'ZBI': 'powiat białogardzki', 'ZCH': 'powiat choszczeńśki', 'ZDR': 'powiat drawski', 'ZGL': 'powiat goleniowski',
                       'ZGY': 'powiat gryficki', 'ZGR': 'powiat gryfiński', 'ZKA': 'powiat kamieński', 'ZKO': 'powiat koszaliński', 'ZKL': 'powiat kołobrzeski', 'ZMY': 'powiat myśliborski',
                       'ZPL': 'powiat policki', 'ZPY': 'powiat pyrzycki', 'ZST': 'powiat stargardzki', 'ZSD': 'powiat świdwiński', 'ZSZ': 'powiat szczecinecki', 'ZSL': 'powiat sławieński',
                       'ZWA': 'powiat wałecki', 'ZLO': 'powiat łobeski'
                       }

plate_chars = list(string.ascii_uppercase+string.digits)
plate_chars.remove('Q')


def plate_number_generator(size=5, chars=plate_chars):
    return ''.join(random.choice(chars) for _ in range(size))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/guess_all', methods=["GET", "POST"])
def guess_all():
    style_color = 'red'
    global all_plate_districts
    game_mode = 'guess_all'
    if request.method == "POST":
        if "username_input" in request.form:
            session['user'] = request.form['username_input']
            session['user_score'] = int()
            session['user_plate_districts'] = all_plate_districts
            session['user_amount_of_plates'] = len(
                session['user_plate_districts'])

        user_last_plate = session.get('user_last_plate_district', None)

        if request.form.get('user_answer'):
            session['user_answer'] = request.form.get('user_answer').lower()
            user_answer = session['user_answer']
            if user_last_plate != None:
                if len(user_last_plate) == 8:
                    user_last_plate_district = user_last_plate.split('\t', 1)[
                        0]
                else:
                    user_last_plate_district = user_last_plate.split(' ', 1)[0]

                if user_answer == session['user_plate_districts'][user_last_plate_district]:
                    user_outcome = 'Dobrze'
                    answer_color = 'lime'
                    session['user_score'] += 1
                    del session['user_plate_districts'][user_last_plate_district]
                elif isinstance(session['user_plate_districts'][user_last_plate_district], list):
                    if user_answer in session['user_plate_districts'][user_last_plate_district]:
                        user_outcome = 'Dobrze'
                        answer_color = 'lime'
                        session['user_score'] += 1
                        del session['user_plate_districts'][user_last_plate_district]
                    else:
                        user_outcome = "Źle"
                        answer_color = 'red'
                else:
                    user_outcome = "Źle"
                    answer_color = 'red'
        else:
            if user_last_plate == None:
                user_outcome = ''
                answer_color = ''
            else:
                user_outcome = 'Źle'
                answer_color = 'red'
        if len(session['user_plate_districts']) > 0:
            new_plate_district = random.choice(
                list(session['user_plate_districts'].items()))
            if len(new_plate_district[0]) == 2:
                new_plate = new_plate_district[0] +\
                    '\t'+plate_number_generator()
            else:
                new_plate = new_plate_district[0]+" "+plate_number_generator()
            session['user_last_plate_district'] = new_plate
            return render_template('game.html', new_plate=new_plate, user_outcome=user_outcome, answer_color=answer_color,
                                   user_score=session['user_score'], newPlateDistrict=new_plate_district, plates_amount=session['user_amount_of_plates'],
                                   game_mode=game_mode, style_color=style_color)
        else:
            new_plate = "Koniec gry"
            return render_template('game.html', new_plate=new_plate, user_outcome=user_outcome, answer_color=answer_color,
                                   user_score=session['user_score'],  plates_amount=session['user_amount_of_plates'],
                                   game_mode=game_mode, style_color=style_color)
    else:
        return render_template('username.html', game_mode=game_mode, style_color=style_color)


@app.route('/guess_on_time', methods=['POST', 'GET'])
def guess_on_time():
    style_color = 'orange'
    global all_plate_districts
    game_mode = 'guess_on_time'
    user_plates_all_districts = all_plate_districts
    if request.method == "POST":
        if "username_input" in request.form:
            session['user'] = request.form['username_input']
            session['user_score'] = int()
            session['user_plate_districts'] = {}
            for _ in range(50):
                add_plate_district_to_districts_list = random.choice(
                    list(user_plates_all_districts.items()))
                del user_plates_all_districts[add_plate_district_to_districts_list[0]]
                session['user_plate_districts'][add_plate_district_to_districts_list[0]
                                                ] = add_plate_district_to_districts_list[1]
                session['user_amount_of_plates'] = len(
                    session['user_plate_districts'])

        user_last_plate = session.get('user_last_plate_district', None)

        if request.form.get('user_answer'):
            session['user_answer'] = request.form.get('user_answer').lower()
            user_answer = session['user_answer']
            if user_last_plate != None:
                if len(user_last_plate) == 8:
                    user_last_plate_district = user_last_plate.split('\t', 1)[
                        0]
                else:
                    user_last_plate_district = user_last_plate.split(' ', 1)[0]

                if user_answer == session['user_plate_districts'][user_last_plate_district]:
                    user_outcome = 'Dobrze'
                    answer_color = 'lime'
                    session['user_score'] += 1
                    del session['user_plate_districts'][user_last_plate_district]
                elif isinstance(session['user_plate_districts'][user_last_plate_district], list):
                    if user_answer in session['user_plate_districts'][user_last_plate_district]:
                        user_outcome = 'Dobrze'
                        answer_color = 'lime'
                        session['user_score'] += 1
                        del session['user_plate_districts'][user_last_plate_district]
                    else:
                        user_outcome = "Źle"
                        answer_color = 'red'
                else:
                    user_outcome = "Źle"
                    answer_color = 'red'
        else:
            if user_last_plate == None:
                user_outcome = ''
                answer_color = ''
            else:
                user_outcome = 'Źle'
                answer_color = 'red'
        if len(session['user_plate_districts']) > 0:
            new_plate_district = random.choice(
                list(dict(session['user_plate_districts']).items()))
            if len(new_plate_district[0]) == 2:
                new_plate = new_plate_district[0] +\
                    '\t'+plate_number_generator()
            else:
                new_plate = new_plate_district[0]+" "+plate_number_generator()
            session['user_last_plate_district'] = new_plate
            return render_template('game.html', new_plate=new_plate, user_outcome=user_outcome, answer_color=answer_color,
                                   user_score=session['user_score'], newPlateDistrict=new_plate_district, plates_amount=session['user_amount_of_plates'],
                                   game_mode=game_mode, style_color=style_color)
        else:
            new_plate = "Koniec gry"
            return render_template('game.html', new_plate=new_plate, user_outcome=user_outcome, answer_color=answer_color,
                                   user_score=session['user_score'], plates_amount=session['user_amount_of_plates'],
                                   game_mode=game_mode, style_color=style_color)
    else:
        return render_template('username.html', game_mode=game_mode, style_color=style_color)


@app.route('/clear')
def clear():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
