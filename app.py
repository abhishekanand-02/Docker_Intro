from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name'] 
        return render_template_string('''
            <h1>Welcome, {{ name }}! 🎉</h1>
            <p>We're glad to have you here! 😊</p>
            <a href="/">Go back</a>
        ''', name=name)
    
    return '''
        <form method="POST">
            <label for="name">Enter your name:</label><br>
            <input type="text" id="name" name="name" required><br><br>
            <input type="submit" value="Submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
