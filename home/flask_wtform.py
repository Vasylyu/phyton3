from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

app = Flask(__name__)


class RegisrationForm(FlaskForm):
    email = StringField()
    phone = IntegerField()
    name = StringField()
    index = IntegerField()
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegisrationForm()

    if form.validate_on_submit():
        email, phone, comment = form.email.data, form.phone.data, form.comment.data

        return f"Succesfully registreted user {email} with phone +7{phone} and {comment}"

    return f"Invalid input, {form.errors}", 400


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
