from flask import Flask, render_template, request, redirect
import datetime
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data, time):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},\t{subject},\t{message}, \t{time}')

def write_to_csv(data, time):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message,time])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            time = datetime.datetime.now()
            write_to_file(data, time)
            return redirect('/thankyou.html')
        except:
            return redirect('/submit_form.html')
    else:
        return 'Something went wrong. Try again!'

if __name__ == '__main__':
    app.run()

