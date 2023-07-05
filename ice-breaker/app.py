from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["GET"])
def process():
    name = request.form["name"]
    # summary_and_facts, interests, ice_breakers, profile_pic_url = ice_break_with(
    #     name=name
    # )
    return jsonify(
        {
            "name": name
        }
    )


if __name__ == "__main__":
    app.run()
