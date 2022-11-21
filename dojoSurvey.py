from flask import Flask,render_template,request
app = Flask(__name__)
# ------------------------------------------------------------
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process' , methods =['POST'])
def process_form():
    print(request.form)
    return render_template("result.html",name=request.form['name'],location=request.form['location'],langouge=request.form['langouge'],comment=request.form['comment'])
    

# ------------------------------------------------------------
if __name__=='__main__':
    app.run(debug=True)