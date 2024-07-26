
from flask import Flask, request, render_template
from flaskext.wtf import Form, TextField, validators

app = Flask(__name__)

app.config['SECRET_KEY'] = 'topsecret'

class FlashcardForm(Form):
    saying = TextField('Saying', [validators.Required()])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FlashcardForm(request.form)
    if request.method == 'POST' and form.validate():
        saying = form.saying.data
        translation = translate_to_dutch(saying)
        return render_template('index.html', form=form, translation=translation)
    else:
        return render_template('index.html', form=form)

def translate_to_dutch(saying):
    # Placeholder translation logic
    return "Vertaling"

if __name__ == "__main__":
    app.run()
