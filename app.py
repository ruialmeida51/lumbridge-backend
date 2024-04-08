# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 14:49:46 2024

@author: Alex Valadares
"""

from flask import Flask, render_template, request, redirect, url_for
from DB import get_expenses, add_expense, delete_expense

app = Flask(__name__)
app.config["DEBUG"] = True

# Home route
@app.route('/')
def index():
    expenses = get_expenses()
    return render_template('index.html', expenses=expenses)

# Add expense route
@app.route('/add', methods=['POST'])
def add():
    description = request.form['description']
    amount = request.form['amount']
    add_expense(description, amount)
    return redirect(url_for('index'))


# Delete expense route
@app.route('/delete/<int:expense_id>')
def delete(expense_id):
    delete_expense(expense_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000)