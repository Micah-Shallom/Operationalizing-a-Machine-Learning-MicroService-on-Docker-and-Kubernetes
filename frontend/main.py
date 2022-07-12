from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('form.html')


@app.route("/predict" , methods=['GET','POST'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/home' to submit form"
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        return render_template('prediction.html',form_data = form_data)
    
if __name__ == "__main__":
    app.run(debug=True)