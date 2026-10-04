<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Python Guessing Game</title>
    <link rel="stylesheet" href="https://pyscript.net" />
    <script type="module" src="https://pyscript.net"></script>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; padding: 30px; background-color: #282c34; color: white; }
        .game-card { background: #333842; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); display: inline-block; min-width: 300px; }
        input { padding: 12px; font-size: 18px; width: 80px; text-align: center; border-radius: 6px; border: none; margin: 10px; }
        button { padding: 12px 24px; font-size: 16px; font-weight: bold; background-color: #00bcd4; color: white; border: none; border-radius: 6px; cursor: pointer; transition: 0.2s; }
        button:hover { background-color: #0097a7; }
        #resetBtn { background-color: #ff5722; display: none; margin-top: 10px; }
        #resetBtn:hover { background-color: #e64a19; }
        .stats { display: flex; justify-content: space-around; margin-bottom: 20px; font-weight: bold; font-size: 16px; }
        #gameOutput { font-size: 18px; margin: 20px 0; font-weight: bold; min-height: 24px; }
    </style>
</head>
<body>

    <div class="game-card">
        <h2>🔢 Secret Number Game</h2>
        
        <div class="stats">
            <span id="attemptsCount">🎯 Guesses: 0</span>
            <span id="bestScore">🏆 Best: --</span>
        </div>

        <p>I am thinking of a number between 1 and 100. Can you guess it?</p>
        
        <input type="number" id="guessInput" min="1" max="100" placeholder="50">
        <br>
        <button py-click="check_guess">Submit Guess</button>
        <br>
        <button id="resetBtn" py-click="restart_game">Play Again</button>

        <div id="gameOutput">Good luck!</div>
    </div>

    <!-- Links directly to your live GitHub file -->
    <script type="py" src="https://githubusercontent.com"></script>

</body>
</html>
