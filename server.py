from flask import Flask,render_template,redirect,request
import csv
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<username>')
def blog(username):
    return render_template(username)

def savingMethod(data):
    with open('./Database.csv','w', newline='') as csvfile:
        
        li=['Email','Number','Name','Message']
        spamwriter = csv.DictWriter(csvfile, fieldnames=li)
        spamwriter.writeheader()
        spamwriter.writerow(({'Email': data['email'], 'Number': data['number'],'Name':data['Name'],'Message':data['Message']}))

      
@app.route('/submit', methods=['POST', 'GET'])
def blog2():
    if(request.method == 'POST'):
        try:
            data=request.form.to_dict()
            savingMethod(data)
            return render_template('thankyu.html', name=data['Name'])
        except:
            return "something went run, its exception"
    else:
        return 'something went wrong'
    

