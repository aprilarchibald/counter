from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = "security"


@app.route('/')
def index():
    if 'count' not in session:
        session['count']=1
    else:
        session['count'] += 1
    return render_template("index.html")

# @app.route('/count', methods=['POST'])
# def add_views():
#     session['count'] += num
#     return redirect ('/')


@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')










if __name__=="__main__":
    app.run(debug=True)
