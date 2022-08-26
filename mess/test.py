from flask import Flask, render_template
from requesting import PokeGen

app = Flask(__name__)
poke_gen = PokeGen()


@app.route("/")
@app.route("/<name>")
def home(name="uh..., what's your name"):
   
   
   args = {
      "name" : name,
      "img_url" : poke_gen.get_random_poke()
   }
   return render_template('hello.html', **args)

if __name__ == "__main__":
   app.run()
