from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat 

# Instantiate the flask class
app = Flask(__name__)

class Homepage(MethodView):

    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):

    def get(self):
        #Initialize the bill form
        bill_form = BillForm()
        return render_template('bill_form_page.html', billform=bill_form)
    
    def post(self):
        # extract the data that user inputs
        billform = BillForm(request.form)

        amount = float(billform.amount.data)
        period = billform.period.data

        name1 = billform.name1.data
        days_in_house1 = float(billform.days_in_house1.data)

        name2 = billform.name2.data
        days_in_house2 = float(billform.days_in_house2.data)

        # initialize the Bill object
        the_bill = flat.Bill(amount, period,)
        flatmate1 = flat.Flatmate(name1, days_in_house1)
        flatmate2 = flat.Flatmate(name2, days_in_house2)

        #return f"{flatmate1.name} pays {flatmate1.pays(the_bill, flatmate2)}"
        return render_template('bill_form_page.html',
                               result=True,
                               billform = billform,
                                name1 = flatmate1.name,
                                amount1 = flatmate1.pays(the_bill,flatmate2),
                                name2 = flatmate2.name,
                                amount2 = flatmate2.pays(the_bill, flatmate1))

class ResultsPage(MethodView):

    def post(self):
        # extract the data that user inputs
        billform = BillForm(request.form)

        amount = float(billform.amount.data)
        period = billform.period.data

        name1 = billform.name1.data
        days_in_house1 = float(billform.days_in_house1.data)

        name2 = billform.name2.data
        days_in_house2 = float(billform.days_in_house2.data)

        # initialize the Bill object
        the_bill = flat.Bill(amount, period,)
        flatmate1 = flat.Flatmate(name1, days_in_house1)
        flatmate2 = flat.Flatmate(name2, days_in_house2)

        #return f"{flatmate1.name} pays {flatmate1.pays(the_bill, flatmate2)}"
        return render_template('results.html',
                         name1 = flatmate1.name,
                         amount1 = flatmate1.pays(the_bill,flatmate2),
                         name2 = flatmate2.name,
                         amount2 = flatmate2.pays(the_bill, flatmate1))

class BillForm(Form):
    # to create the label and textbox, we need to use StringField class
    amount = StringField("Bill Amount: ", default="100")
    period = StringField("Bill Period: ", default="August 2023")
    name1 = StringField("Name: ", default="A")
    days_in_house1 = StringField("days_in_house1: ", default=24)

    name2 = StringField("Name: ", default="B")
    days_in_house2 = StringField("days_in_house2: ", default=22)

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=Homepage.as_view('home_page'))
app.add_url_rule('/bill_form_page', view_func=BillFormPage.as_view('bill_form_page'))

# if we are showing the result in the same page as bill form page
#app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))



# only to see the changes
app.run(debug=True)
#app.run()