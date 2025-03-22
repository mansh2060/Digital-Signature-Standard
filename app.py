from flask import Flask, render_template, request
from signature_verification import SignatureVerification

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        n_bits = int(request.form['n_bits'])
        verification = SignatureVerification(text, n_bits)
        first_signature = verification.first_signature
        second_signature = verification.second_signature
        validation_result = verification.output_validation()
        
        return render_template('result.html', text=text, first_signature=first_signature,
                               second_signature=second_signature, validation_result=validation_result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
