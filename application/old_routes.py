from application import app
from flask import render_template, request, flash
import json
from application.models.models import Customer


@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        """
        dict_prop = request.values
       # for key, val in dict_prop.items():
            #print('{}: {}'.format(key, val))
            #print(key)
        dict_prop = dict(dict_prop)
        for k, v in dict_prop.items():
            print('{}: {}'.format(k, v))
        #print(dict_prop['MST'])

        req_js = request.get_json()
        for key, val in req_js.items():
            #print('{}: {}'.format(key, val))
            print(key)
            for k, v in val.items():
                print('{}: {}'.format(k, v))
       """
        return render_template('test.html', Company='TL_ServerWellID')
    with open(r"application\static\test.json", "r") as f:
        customers = dict(json.load(f))
        customers = [i for i in customers]

    return render_template('30_09.html', data=request.args, customers=customers)


@app.route('/add_customers', methods=['post', 'get'])
def add_customers():
    if request.method == 'POST':
        customer_to_add = request.form.get('customer_to_add')
        print(customer_to_add)
        with open(r"application\static\test.json", "r") as f:
            customers = dict(json.load(f))
            customers[customer_to_add] = []
        with open(r"application\static\test.json", "w") as f:
            json.dump(customers, f)
        flash('Заказчик {} успешно добавлен'.format(customer_to_add))

    with open(r"application\static\test.json", "r") as f:
        customers = dict(json.load(f))
        customers = [i for i in customers]
    return render_template('add_customers.html', customers=customers)


@app.route('/all_customers', methods=['post', 'get'])
def all_customers():
    with open(r"application\static\test.json", "r") as f:
        customers = dict(json.load(f))
        customers = [i for i in customers]
        return render_template('all_customers.html', customers=customers)


@app.route('/customer_page', methods=['post', 'get'])
def customer_page():
    customer = request.args.get('customer')
    if request.method == 'POST':
        customer = request.form.get('customer')
        field = request.form.get('field')
        with open(r"application\static\test.json", "r") as f:
            customers = dict(json.load(f))
            fields = customers[customer]
            fields.append(field)
            customers[customer] = fields
        with open(r"application\static\test.json", "w") as f:
            json.dump(customers, f)
        flash('Месторождение {} успешно добавлено'.format(field))
    with open(r"application\static\test.json", "r") as f:
        customers = dict(json.load(f))
        fields = [field for field in customers[customer]]
    return render_template('customer_page.html', fields=fields, customer=customer)


@app.route('/get_json', methods=['GET', 'POST'])
def get_json():
    with open(r"application\static\test.json", "r") as f:
        customers = dict(json.load(f))
        customer = request.json['customer']
        customer_to_show = customers[customer]
    return json.dumps(customer_to_show)


@app.route('/customer/<customer_name>')
def customer(customer_name):
    customer = Customer.query.filter_by(name=customer_name).first_or_404()
    fields = customer.fields
    return render_template('test_db.html', customer=customer, fields=fields)


@app.route('/customers')
def customers():
    customers_list = Customer.query.all()
    return render_template('customer_list.html', customers_list=customers_list)


@app.route('/customers')
def customers():
    customers_list = Customer.query.all()
    return render_template('customer_list.html', customers_list=customers_list)




