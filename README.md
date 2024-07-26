## Flask Application Design for Creating an Australian to Dutch Flashcard Translator

### HTML Files

**index.html:**
- This HTML file will serve as the main page of the application, displaying the flashcards and a form for user input.
- The HTML content should include:
  - A header section with a title like "Australian to Dutch Flashcards."
  - A div element to display the flashcards, initially hidden.
  - A form with an input field for the user to enter an Australian saying or expression.
  - A submit button labeled "Translate to Dutch."

### Routes

**app.py:**

```
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
        # Translation logic here
        translation = translate_to_dutch(saying)
        return render_template('index.html', form=form, translation=translation)
    else:
        return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()
```

**Explanation:**

- The `app.py` file defines the Flask application and its routes.
- The `FlashcardForm` class defines the form for user input.
- The `/` route handles both GET and POST requests.
- For GET requests, it renders the `index.html` page with an empty form.
- For POST requests, it validates the form input and calls the `translate_to_dutch` function to translate the Australian saying to Dutch.
- The translation is then displayed in the `index.html` page.