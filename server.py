from flask import Flask, render_template, url_for, request, redirect
app=Flask(__name__)
import csv


#@app.route('/<user>/<int:post_id>')
#def hello_world(user=None, post_id=None):
	#print(url_for('static', filename='favicon.ico'))
	#return render_template('index.html', name=user, post_id= post_id)#will read url
@app.route('/')
def main():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode= 'a') as database:
		email= data['email']
		subject= data['subject']
		message= data['message']
		file= database.write(f'\n{email},{subject}, {message}')
def write_to_csv(data):
	with open('datbase.csv', mode= 'a', newline="") as database2:
		email= data['email']
		subject= data['subject']
		message= data['message']
		csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting= csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data= request.form.to_dict()
			write_to_file(data)
			write_to_csv(data)
			print(data)
			return redirect('thankyou.html')
		except:
			return 'did not save'
	else:
		return 'something went wrong'




#@app.route('/index.html')
#def home():
	#return render_template('index.html')


#@app.route('/project.html')
#def projects():
    #return render_template('project.html')

#@app.route('/components.html')
#def components():
    #return render_template('components.html')   