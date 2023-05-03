from flask import Flask, render_template, request, redirect, url_for, flash
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.debug = True

# This will store the results in memory
results = []

# UX improvements:
# 1. Made it so you can press enter/return to go to the next question
# 2. Made it so the text box is auto-selected when you press next
# 3. Made the format of the results table less cluttered and easier to read via bootstrap styling
# 4. Add a button on the thank you page to start a new entry, also made the thank you page a
# new route
# 5. Added a "wipe data" button on the results.html page
# 6. Made it so if you decide to change back to deposit after selecting valid, the gift card
# number and pin are removed
# 7. Added a button to go to the results table on the thank you page and a
# button to go back to the survey on the results table


@app.route('/', methods=['GET', 'POST'])
def seller_onboarding_form():
    if request.method == 'POST':
        form_data = {
            'store_name': request.form['store_name'],
            'balance': request.form['balance'],
            'selling_price': request.form['selling_price'],
            'network': request.form['network'],
            'receiving_address': request.form['receiving_address'],
            'preference': request.form['preference'],
            'card_number': request.form['card_number'],
            'card_pin': request.form['card_pin'],
            'email': request.form['email']
        }
        results.append(form_data)
        return redirect('/thank-you')

    return render_template('form.html')


@app.route('/results')
def results_page():
    return render_template('results.html', results=results)


@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')


if __name__ == '__main__':
    app.run(port=5001)
