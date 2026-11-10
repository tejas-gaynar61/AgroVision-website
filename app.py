from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

CROPS = {
    "rice": {"rainfall": (100, 300), "ph": (5.0, 7.0), "n": (60, 100)},
    "wheat": {"rainfall": (30, 100), "ph": (6.0, 7.5), "n": (40, 80)},
    "maize": {"rainfall": (50, 150), "ph": (5.5, 7.5), "n": (50, 90)},
    "cotton": {"rainfall": (50, 120), "ph": (5.5, 8.0), "n": (40, 80)},
    "chickpea": {"rainfall": (20, 80), "ph": (6.0, 8.0), "n": (20, 50)},
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json(silent=True) or {}
    try:
        rainfall = float(data["rainfall"])
        ph = float(data["ph"])
        nitrogen = float(data["nitrogen"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Please enter valid numbers in all fields."}), 400

    if not (0 <= rainfall <= 500 and 0 <= ph <= 14 and 0 <= nitrogen <= 200):
        return jsonify({"error": "Check your values: rainfall 0–500 mm, pH 0–14, nitrogen 0–200."}), 400

    ranked = []
    for crop, limits in CROPS.items():
        score = 0
        for key, value in (("rainfall", rainfall), ("ph", ph), ("n", nitrogen)):
            low, high = limits[key]
            score += 1 if low <= value <= high else 0
        ranked.append((score, crop.title()))
    ranked.sort(reverse=True)
    best_score, best_crop = ranked[0]
    return jsonify({
        "crop": best_crop,
        "score": round(best_score / 3 * 100),
        "note": "This is a simple educational rule-based demo, not professional agricultural advice."
    })

if __name__ == "__main__":
    app.run(debug=True)
