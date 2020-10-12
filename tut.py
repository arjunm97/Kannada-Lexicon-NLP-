from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/nf/')                                       #nf = Noun Inflextion
def nf():
	return render_template('nf.html')

@app.route('/ns/')
def ns():
	return render_template('ns.html')

@app.route('/pf/')
def pf():
	return render_template('pf.html')

@app.route('/ps/')
def ps():
	return render_template('ps.html')

@app.route('/vf/')
def vf():
	return render_template('vf.html')

@app.route('/vs/')
def vs():
	return render_template('vs.html')

@app.route('/nf1', methods=['POST'])
def nf1():
	wo = request.form['word']
	df = pd.read_excel (r'noun_rules.xlsx') 
	df2=pd.read_csv(r"lexicon.csv")
	X = df2.iloc[:, 0].values
	Y = df2.iloc[:, 3].values
	x=list(X)
	y=list(Y)
	z = x.index(wo)
	category=y[z]#Change here when sql database is available
	o = category
	o = int(o)
	#####Got the word,category
	df.reset_index(inplace=True)
	p=df.loc[ o , : ]
	p=list(p)
	p.pop(0)
	p.pop(0)
	p.pop(0)

	

	inflex_morh=list()
	for i in p:
	    new_word=wo+i
	    inflex_morh.append(new_word)
	    
	return inflex_morh
	#print (df)
	#return render_template('npf.html',nam='ಅವನು')

@app.route('/ns1', methods=['POST'])
def ns1():
	wo = request.form['word']
	df = pd.read_excel (r'noun_rules.xlsx') 
	df2=pd.read_csv(r"lexicon.csv")
	X = df2.iloc[:, 0].values
	Y = df2.iloc[:, 3].values
	x=list(X)
	y=list(Y)
	z = x.index(wo)
	category=y[z]#Change here when sql database is available
	o = category[0]
	o = int(o)
	#####Got the word,category
	df.reset_index(inplace=True)
	p=df.loc[ o , : ]
	p=list(p)
	print(p)
	p.pop(0)
	p.pop(0)
	p.pop(0)

	inflex_morh=list()
	for i in p:
	    new_word=wo+i
	    inflex_morh.append(new_word)

	specific=["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12","P13","14"]
	cat = request.form['category']
	index=specific.index(cat)
	return inflex_morh[index]
	    

@app.route('/pf1', methods=['POST'])
def pf1():
	x = request.form['word']
	return render_template('npf.html',nam='ಅವನು')

@app.route('/ps1', methods=['POST'])
def ps1():
	x = request.form['word']
	return "WOrd"+x

@app.route('/vf1', methods=['POST'])
def vf1():
	x = request.form['word']
	return "WOrd"+x

@app.route('/vs1', methods=['POST'])
def vs1():
	x = request.form['word']
	return "WOrd"+x

if __name__ == '__main__':
	app.run(debug = True)