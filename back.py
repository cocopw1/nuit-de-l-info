import flask
import csv
def addincsv(url,content:str):
    file = open(url,mode='a')
    file.write(content+'\n')
def import_csv(url_file, delimiter) :
    with open(url_file, newline='', encoding='utf-8') as csvfile :
        file = csv.reader(csvfile, delimiter=delimiter)
        list_list = []
        for row in file :
            list_list.append(row)
    return list_list
def suprligne(url, n):
    f = open(url,"r+")
    d = f.readlines()
    f.seek(0)
    for i in range(len(d)):
        
        if i != n:
            f.write(d[i])
    f.truncate()
    f.close()
app = flask.Flask(__name__)
@app.route('/ibijeu',methods=['GET'])
def ibijeu():
  a= open("ibijeu.html","r",encoding='utf-8')
  return a.read()
oi = import_csv("user.csv",";")
users =[]
for i in oi:
  if oi[0]not in users:
    users.append(oi[0])
for i in users:
  print(i)
  @app.route("/"+i[0],methods=['GET'])
  def userspage():
    mst = []
    global i
    for j in oi:
      if j[0]==i:
        if j[1] not in mst:
          mst.append(j[1])
    a = open('./index.html',encoding='utf-8')
    j = import_csv("mst.csv",";")
    for h in range(len(j)):
      try:
        if j[h][0] not in mst:
          j.pop(h)
      except:
        None
    n =''
    for g in j:
        n +='''
  <div class="card">
    <div class="card__image-holder">
      <img class="card__image" src="'''+str(g[4])+'''" alt="'''+g[1]+'''" />
    </div>
    <div class="card-title">
      <a href="#" class="toggle-info btn">
        <span class="left"></span>
        <span class="right"></span>
      </a>
      <h2>
          '''+g[1]+'''
          <small>description :</small>
      </h2>
    </div>
    <div class="card-flap flap1">
      <div class="card-description">
        '''+g[3]+'''
      </div>
      <div class="card-flap flap2">
        <div class="card-actions">
          <a href= "'''+g[5]+'''" class="btn">Read more</a>
        </div>
      </div>
    </div>
  </div>
  '''
    return a.read().replace("{{content}}",n)
    
@app.route('/',methods=['GET'])
def index():
    a = open('./index.html',encoding='utf-8')
    i = import_csv("mst.csv",";")
    n =''
    for g in i:
        n +='''
  <div class="card">
    <div class="card__image-holder">
      <img class="card__image" src="'''+str(g[4])+'''" alt="'''+g[1]+'''" />
    </div>
    <div class="card-title">
      <a href="#" class="toggle-info btn">
        <span class="left"></span>
        <span class="right"></span>
      </a>
      <h2>
          '''+g[1]+'''
          <small>description :</small>
      </h2>
    </div>
    <div class="card-flap flap1">
      <div class="card-description">
        '''+g[3]+'''
      </div>
      <div class="card-flap flap2">
        <div class="card-actions">
          <a href= "'''+g[5]+'''" class="btn">Read more</a>
        </div>
      </div>
    </div>
  </div>
  '''
    a =a.read().replace("{{content}}",n)
    return a
if(__name__=='__main__'):
    app.run(host="0.0.0.0")