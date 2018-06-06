from flask import Flask,render_template, request,redirect

app=Flask(__name__)

@app.route('/')
def index():
	fruits=['apple', 'orange','banana']
	return render_template('index.html', fruits=fruits)
@app.route('/home')
def home():
	
	return render_template('home.html')
@app.route('/login',methods=["post","get"])
def login():
	error = None
	if request.method =='POST':
		if request.form['email'] !='1999@gmail.com' or request.form['password'] !='chair':
	  		error = 'Email or password does not match'

		else:
	 		return redirect('/home')
		return render_template('login.html',error=error)
	return render_template('login.html')




if __name__=='__main__':
	app.jinja_env.globals.update(chr=chr)
	app.run(host="0.0.0.0",port=8000,debug=True, threaded=True)





























