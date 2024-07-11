from flask import Flask, render_template
import markdown
from database import CatalogDB
import json

db = CatalogDB("catalog.sqlite")
db.init_table()

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.template_filter()
def humanize_lang(lang):
    if lang == "zh":
        return "中文"
    elif lang == "en":
        return "英文"
    return lang

@app.template_filter()
def markup(text):
    if text is None:
        return None
    return markdown.markdown(text)

@app.template_filter()
def fromjson(text):
    if text is None:
        return None
    return json.loads(text)

@app.route("/<string:home_id>/")
def home_index(home_id):
    try:
        with db.get_con() as c:
            res = c.execute("SELECT * FROM game WHERE home_id = :home_id", {
                "home_id": home_id
            })
            return render_template('index.jinja.html', home_id=home_id, game=res)
    except Exception as e:
        print("Error in db: " + str(e))
    return render_template('index.jinja.html', home_id=home_id, game=[])

if __name__ == "__main__":
    app.run(port="5000")