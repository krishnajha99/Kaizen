#import twitterAPI
import os
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from flask import Flask, render_template, flash, url_for , redirect , config, Markup, Response
from Forms import Submissionform    
from flask_wtf.csrf import CsrfProtect
#csrf = CsrfProtect()

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-ever-guess'
    
app = Flask(__name__)
app.config.from_object(Config)
#csrf.init_app(app)
@app.route("/", methods=['GET','POST'])
def template():
	return render_template('template.html')
	
@app.route("/home", methods=['GET','POST'])           
def home():
	form = Submissionform()
	if form.validate_on_submit():
		flash('Ticker Submited :  {}'.format(form.text.data))
		try:
			if form.submit.data == True:
				ts = TimeSeries(key='FSFW64CYZLUB5O4C',output_format='pandas')
				data, meta_data = ts.get_intraday(symbol=form.text.data,interval='1min', outputsize='full')
				data = data.reindex(index=data.index[::-1])
				values = data['4. close']
				labels = list(data.index)
				legend = form.text.data
				return render_template('chart.html',values=values,labels=labels,legend=legend)
			if form.monthly.data == True:
				ts = TimeSeries(key='FSFW64CYZLUB5O4C',output_format='pandas')
				data, meta_data = ts.get_monthly(symbol=form.text.data)
				print(data)
				data = data.reindex(index=data.index[::-1])
				values = data['4. close']
				labels = list(data.index)
				legend = form.text.data
				return render_template('chart.html',values=values,labels=labels,legend=legend)
			if form.download.data == True:
				ts = TimeSeries(key='FSFW64CYZLUB5O4C',output_format='pandas')
				data, meta_data = ts.get_intraday(symbol=form.text.data,interval='1min', outputsize='full')
				
				csv = data.to_csv()
				#print(csv)
				return Response(
				csv,
				mimetype="text/csv",
				headers={"Content-disposition":
					"attachment; filename=data.csv"})
		except:
			flash('Enter Valid Ticker!')
	else:
		flash_errors(form)
	return render_template('home.html',form=form)
	
def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')   

@app.route('/chart', methods=['GET', 'POST'])
def chart():
	if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
		return render_template('template.html')
	return render_template('chart.html')

    
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5000)
 
