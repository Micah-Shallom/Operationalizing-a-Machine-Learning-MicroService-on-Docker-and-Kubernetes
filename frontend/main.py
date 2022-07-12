from flask import Flask, render_template, request , session

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    if request.method == 'GET':
        # return f"The URL /data is accessed directly. Try going to '/home' to submit form"
        return render_template('form.html' , title="Home")
    if request.method == 'POST':
        form_data = request.form
        data = []
        for key, value in dict(form_data).items():
            data.append((key, {"0": value}))

        prep_data = dict(data)

        session['prep_data'] = prep_data
    return render_template('form.html' , title="Home")


@app.route("/predict" , methods=['GET','POST'])
def data():
    form_data = session.get('prep_data')
    print(form_data)
    return render_template('prediction.html', form_data = form_data)
    
if __name__ == "__main__":
    app.run(debug=True)