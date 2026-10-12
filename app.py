from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    elevnavn="Henry"
    alder=17
    klasse="2IMI"
    return render_template("index.html",navn=elevnavn, klasse=klasse, alder=alder)

@app.route("/kurs")
def kurs():
    kurs = request.form.get('kurs')
    kursliste=["python","flask", "javascript","linux"]
    return render_template("kurs.html", kursliste=kursliste)

@app.route("/kontakt", methods=["GET", "POST"])
def kontakt():
    if request.method == "POST":
        navn = request.form["navn"]
        fag = request.form["fag"]
        alder = request.form["alder"]
        kjonn = request.form["kjonn"]

        return render_template(
            "resultat.html", 
            navn=navn,
            fag=fag, 
            alder=alder,
            kjonn=kjonn
        )
    return render_template("kontakt.html")

@app.route("/fag")
def fag():
    fagliste = ["python","flask", "HTML", "CSS" ]
    return render_template("fag.html", fag=fagliste)

@app.route("/profil")
def profil():
    return render_template("")

@app.route("/prosjekter")
def prosjekter():
    return render_template("")



if __name__ == "__main__":
    app.run(debug=True)