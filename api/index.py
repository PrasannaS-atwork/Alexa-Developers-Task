import random
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stone Paper Scissors</title>

    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
        }

        .game {
            width: 90%;
            max-width: 600px;
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(10px);
            padding: 35px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
        }

        h1 {
            margin-bottom: 10px;
        }

        .subtitle {
            margin-bottom: 30px;
            opacity: 0.85;
        }

        .choices {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
            margin-bottom: 30px;
        }

        button {
            border: none;
            padding: 14px 25px;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            background: white;
            color: #333;
            transition: 0.2s;
        }

        button:hover {
            transform: translateY(-3px);
            background: #f1f1f1;
        }

        .result {
            min-height: 120px;
            margin: 20px 0;
        }

        .result h2 {
            margin-bottom: 10px;
        }

        .scores {
            display: flex;
            justify-content: space-around;
            margin-top: 25px;
            padding: 20px;
            background: rgba(0, 0, 0, 0.15);
            border-radius: 12px;
        }

        .score-box {
            font-size: 18px;
        }

        .score {
            display: block;
            font-size: 30px;
            font-weight: bold;
            margin-top: 5px;
        }

        .reset {
            margin-top: 25px;
            background: #ff6b6b;
            color: white;
        }

        .reset:hover {
            background: #ff5252;
        }
    </style>
</head>

<body>

<div class="game">

    <h1>🎮 Stone Paper Scissors</h1>

    <p class="subtitle">
        Choose your move and play against the computer!
    </p>

    <div class="choices">
        <button onclick="play('stone')">🪨 Stone</button>
        <button onclick="play('paper')">📄 Paper</button>
        <button onclick="play('scissors')">✂️ Scissors</button>
    </div>

    <div class="result" id="result">
        <h2>Make your choice!</h2>
        <p>Let's see who wins.</p>
    </div>

    <div class="scores">
        <div class="score-box">
            👤 You
            <span class="score" id="userScore">0</span>
        </div>

        <div class="score-box">
            🤖 Computer
            <span class="score" id="computerScore">0</span>
        </div>
    </div>

    <button class="reset" onclick="resetGame()">Reset Game</button>

</div>

<script>
    let userScore = 0;
    let computerScore = 0;

    async function play(choice) {

        const response = await fetch("/api/play", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                choice: choice
            })
        });

        const data = await response.json();

        if (data.error) {
            return;
        }

        userScore = data.user_score;
        computerScore = data.computer_score;

        document.getElementById("userScore").textContent = userScore;
        document.getElementById("computerScore").textContent = computerScore;

        document.getElementById("result").innerHTML = `
            <h2>${data.message}</h2>
            <p>You chose <strong>${data.user_choice}</strong></p>
            <p>Computer chose <strong>${data.computer_choice}</strong></p>
        `;
    }

    async function resetGame() {

        const response = await fetch("/api/reset", {
            method: "POST"
        });

        const data = await response.json();

        userScore = 0;
        computerScore = 0;

        document.getElementById("userScore").textContent = "0";
        document.getElementById("computerScore").textContent = "0";

        document.getElementById("result").innerHTML = `
            <h2>Game Reset!</h2>
            <p>Choose your move to start again.</p>
        `;
    }
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/api/play", methods=["POST"])
def play():

    data = request.get_json()

    user_choice = data.get("choice")

    choices = ["stone", "paper", "scissors"]

    if user_choice not in choices:
        return jsonify({"error": "Invalid choice"}), 400

    computer_choice = random.choice(choices)

    # Scores are stored using the Flask session-like
    # approach below through cookies would be preferable,
    # but for this simple project we use global variables.
    global user_score, computer_score

    try:
        user_score
        computer_score
    except NameError:
        user_score = 0
        computer_score = 0

    if user_choice == computer_choice:
        message = "It's a Draw! 🤝"

    elif (
        (user_choice == "stone" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "stone")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        user_score += 1
        message = "You Win! 🎉"

    else:
        computer_score += 1
        message = "Computer Wins! 🤖"

    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "message": message,
        "user_score": user_score,
        "computer_score": computer_score
    })


@app.route("/api/reset", methods=["POST"])
def reset():

    global user_score, computer_score

    user_score = 0
    computer_score = 0

    return jsonify({
        "message": "Game reset successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)
