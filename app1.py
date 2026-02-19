from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import joblib

# =========================================
# FLASK CONFIG
# =========================================

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# =========================================
# DATABASE MODELS
# =========================================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)
    emotion = db.Column(db.String(100), nullable=False)

# =========================================
# LOAD TRAINED MODEL (FAST STARTUP)
# =========================================

model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_emotion(text):
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]

# =========================================
# HOME
# =========================================

@app.route("/")
def home():
    return """
    <h1>Emotion Sentiment Analysis App </h1> 
    <a href="/signup">Signup</a><br>
    <a href="/signin">Signin</a><br>
    <a href="/feedback">Give Feedback</a><br>
    <a href="/admin">Admin</a>
    """
# <a is anchor tag and href is hyperlink.

# =========================================
# SIGNUP
# =========================================

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "GET":
        return """
        <h2>Signup</h2>
        <form method="post">
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit">
        </form>
        """

    username = request.form.get("username")
    password = request.form.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})


# =========================================
# SIGNIN
# =========================================

@app.route("/signin", methods=["GET", "POST"])
def signin():

    if request.method == "GET":
        return """
        <h2>Signin</h2>
        <form method="post">
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit">
        </form>
        """

    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401


# =========================================
# FEEDBACK
# =========================================

@app.route("/feedback", methods=["GET", "POST"])
def feedback():

    if request.method == "GET":
        return """
        <h2>Feedback</h2>
        <form method="post">
            Username: <input type="text" name="username" required><br>
            Rating: <input type="number" name="rating" required><br>
            Comment: <input type="text" name="comment" required><br>
            <input type="submit">
        </form>
        """

    username = request.form.get("username")
    rating = request.form.get("rating")
    comment = request.form.get("comment")

    # Validate user
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found. Please signup first."}), 400

    emotion = predict_emotion(comment)

    new_feedback = Feedback(
        username=username,
        rating=int(rating),
        comment=comment,
        emotion=emotion
    )

    db.session.add(new_feedback)
    db.session.commit()

    return jsonify({
        "message": "Feedback submitted successfully",
        "predicted_emotion": emotion
    })


# =========================================
# ADMIN
# =========================================

@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "GET":
        return """
        <h2>Admin Login</h2>
        <form method="post">
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit">
        </form>
        """

    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "admin123":

        feedbacks = Feedback.query.all()

        summary = {}
        all_data = []

        for f in feedbacks:
            all_data.append({
                "username": f.username,
                "rating": f.rating,
                "comment": f.comment,
                "emotion": f.emotion
            })

            if f.emotion in summary:
                summary[f.emotion] += 1
            else:
                summary[f.emotion] = 1

        return jsonify({
            "feedback_data": all_data,
            "emotion_summary": summary
        })

    return jsonify({"message": "Invalid admin credentials"}), 401


# =========================================

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
