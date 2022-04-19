from flask import Flask, render_template
app = Flask(__name__)    


@app.route('/')
def basic():
    return render_template('8x8.html')

@app.route('/4')
def four():
    return render_template('8x4.html')

@app.route('/<int:y>/<int:x>')
def usercontrol(x,y):
    return render_template('index.html', x=x, y=y)




if __name__=="__main__":   
    app.run(debug=True)  