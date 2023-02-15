from flask import Flask, request, render_template, redirect
from rules import chad_rules
from fractions import Fraction

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

weight: int = 187

def process_rules(raw_rules):
    rules = []

    for rule in raw_rules:
        exercise, reps, fraction_of_bodyweight, identifier = rule
        if fraction_of_bodyweight:
            f = Fraction.from_float(fraction_of_bodyweight).limit_denominator()
            numerator, denominator = f.numerator, f.denominator
        else:
            numerator, denominator = None, None

        rules.append(
            (exercise, reps, numerator, denominator, identifier)
        )

    return rules

rules = process_rules(chad_rules['upper'])
print(rules)

# TODO: login and signup page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        weight = int(request.form['weight'])
        return redirect('/upper')
    return render_template('index.html')

@app.route('/upper', methods=['GET', 'POST'])
def upper_body():
    if request.method == 'POST':
        print(request.form)
    return render_template('upper-body.html', weight=weight, rules=rules)

# app.run(port=5000)