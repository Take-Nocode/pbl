import datetime
from plyer import notification
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def sample():
    #ファイルから情報を読み込む
    f = open("test.text",'r',encoding='utf-8')
    line = f.readline()
    infos=[]
    while line:
        line=line.rstrip('\n').split(',')
        infos.append({'name':line[0],'expiration_date_str':line[1]})
        line=f.readline()
    #期日が現在の日時より前の物を消去する
    delis=[]
    deli=0
    for info in infos:  
        product_name = info['name']
        expiration_date_str = info['expiration_date_str']
            # 期日をdatetimeオブジェクトに変換
        expiration_date = datetime.datetime.strptime(expiration_date_str, "%Y-%m-%d")
            # 期日が現在の日時よりも後であれば消去するのでindexを保存
        if expiration_date < datetime.datetime.now():
            delis.append(deli)
        deli+=1
    if delis:
        for j in range(len(delis)):
            del infos[delis[len(delis)-j-1]]        
    Infos=[]
    for info in infos:
        Info=info['expiration_date_str'].rstrip('\n').split('-')
        Infos.append({'NAME':info['name'],'YEAR':Info[0],'MONTH':Info[1],'DAY':Info[2]})
    
    f=open("test.text",'w',encoding='utf-8')
    f.write('')
    f.close()
    f=open("test.text",'a',encoding='utf-8')
    for i in range(len(infos)):
        f.write(infos[i]['name']+','+infos[i]['expiration_date_str']+'\n')
    f.close()
            # 消耗品の情報を格納するリスト
    products = []

    #ファイルから情報を読み込む
    f = open("test.text",'r',encoding='utf-8')
    line = f.readline()
    infos=[]
    while line:
        line=line.rstrip('\n').split(',')
        infos.append({'name':line[0],'expiration_date_str':line[1]})
        line=f.readline()
    

    for info in infos:  
        product_name = info['name']
        expiration_date_str = info['expiration_date_str']
            # 期日をdatetimeオブジェクトに変換
        expiration_date = datetime.datetime.strptime(expiration_date_str, "%Y-%m-%d")
            # 期日が現在の日時よりも後であればproductsに追加
        if expiration_date >= datetime.datetime.now():
            # 消耗品の情報をリストに追加
            products.append({"name": product_name, "expiration_date": expiration_date})



    # 現在の日時を取得
    current_date = datetime.datetime.now()

    # 通知メッセージの設定
    for product in products:
        message = f"{product['name']}の期限が近づいています！"


        # 期日までの残り日数を計算
        remaining_days = (product["expiration_date"] - current_date).days
        one_week = datetime.timedelta(days=7)
        week_before = product["expiration_date"] - one_week
        
                # 消耗品の期限の1日前を計算
        one_day = datetime.timedelta(days=1)
        previous_day = product["expiration_date"] - one_day
        
        if  current_date > week_before:
            if current_date != previous_day:
                notification.notify(
                    title=f"{product['name']}の期限が近づいています",
                    message=f"{remaining_days+1}日後に期限が迫っています！",
                    timeout=10
                )



        # 消耗品の期限の1日前が現在の日時であれば通知を送る
        if previous_day == current_date:
            notification.notify(
                title=f"{product['name']}の期限が明日です",
                message=message,
                timeout=10
            )
    Infos=[]
    for info in infos:
        Info=info['expiration_date_str'].rstrip('\n').split('-')
        Infos.append({'NAME':info['name'],'YEAR':Info[0],'MONTH':Info[1],'DAY':Info[2]})
    
    f=open("test.text",'w',encoding='utf-8')
    f.write('')
    f.close()
    f=open("test.text",'a',encoding='utf-8')
    for i in range(len(infos)):
        f.write(infos[i]['name']+','+infos[i]['expiration_date_str']+'\n')
    f.close()
    
    return render_template("home2.html",infos=Infos)




@app.route("/", methods=["GET", "POST"])
def disp():
    if request.method == "GET":
        return render_template("home2.html")
    
    if request.method == "POST":
        print('POSTデータを受け取ったので処理します。')
        NAME = request.form['name']
        YEAR = request.form['year']
        MONTH = request.form['month']
        DAY = request.form['day']
        f = open('test.text', 'a', encoding='utf-8')
        product_name = NAME
        expiration_date_str = YEAR+'-'+MONTH+'-'+DAY
        data = product_name+','+expiration_date_str+'\r'
        f.write(data)
        f.close()
    
        
        # 消耗品の情報を格納するリスト
    products = []

    #ファイルから情報を読み込む
    f = open("test.text",'r',encoding='utf-8')
    line = f.readline()
    infos=[]
    while line:
        line=line.rstrip('\n').split(',')
        infos.append({'name':line[0],'expiration_date_str':line[1]})
        line=f.readline()
    


        # 期日をdatetimeオブジェクトに変換
    expiration_date = datetime.datetime.strptime(expiration_date_str, "%Y-%m-%d")
        # 期日が現在の日時よりも後であればproductsに追加
    if expiration_date >= datetime.datetime.now():
        # 消耗品の情報をリストに追加
        products.append({"name": product_name, "expiration_date": expiration_date})
# 現在の日時を取得
    current_date = datetime.datetime.now()

    # 通知メッセージの設定
    for product in products:
        message = f"{product['name']}の期限が近づいています！"


        # 期日までの残り日数を計算
        remaining_days = (product["expiration_date"] - current_date).days
        one_week = datetime.timedelta(days=7)
        week_before = product["expiration_date"] - one_week
        print(remaining_days,week_before,current_date)
                # 消耗品の期限の1日前を計算
        one_day = datetime.timedelta(days=1)
        previous_day = product["expiration_date"] - one_day
        
        if  current_date > week_before:
            if current_date != previous_day:
                notification.notify(
                    title=f"{product['name']}の期限が近づいています",
                    message=f"{remaining_days+1}日後に期限が迫っています！",
                    timeout=10
                )



        # 消耗品の期限の1日前が現在の日時であれば通知を送る
        if previous_day == current_date:
            notification.notify(
                title=f"{product['name']}の期限が明日です",
                message=message,
                timeout=10
            )



    Infos=[]
    for info in infos:
        Info=info['expiration_date_str'].rstrip('\n').split('-')
        Infos.append({'NAME':info['name'],'YEAR':Info[0],'MONTH':Info[1],'DAY':Info[2]})
    
    f=open("test.text",'w',encoding='utf-8')
    f.write('')
    f.close()
    f=open("test.text",'a',encoding='utf-8')
    for i in range(len(infos)):
        f.write(infos[i]['name']+','+infos[i]['expiration_date_str']+'\n')
    f.close()
    return render_template("home2.html",infos=Infos)

@app.route('/submit_data', methods=['POST'])
def submit_data():
    button=request.form['submit_button']
    

    print('選択されたボタン',button)
    return f"取り消し機能は未実装です"

if __name__=='__main__':
    app.run(debug=True)


