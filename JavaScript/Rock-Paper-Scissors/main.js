const options = ["Rock", "Paper", "Scissors"];
let computerSelection;
let playerSelection;
let winCounter = 0,
  lossCounter = 0;
function computerPlay() {
  return options[Math.floor(Math.random() * options.length)];
}

function playRound(playerSelection, computerSelection) {
  computerSelection = computerPlay().toLowerCase();
  playerSelection = prompt("Rock,Paper or Scissors?").toLowerCase();

  if (
    (playerSelection === "rock" && computerSelection === "scissors") ||
    (playerSelection === "paper" && computerSelection === "rock") ||
    (playerSelection === "scissors" && computerSelection === "paper")
  ) {
    console.log("You Win " + playerSelection + " beats " + computerSelection);
    winCounter += 1;
    console.log("Current wins: " + winCounter);
  } else if (
    (computerSelection === "rock" && playerSelection === "scissors") ||
    (computerSelection === "paper" && playerSelection === "rock") ||
    (computerSelection === "scissors" && playerSelection === "paper")
  ) {
    console.log("You lose " + computerSelection + " beats " + playerSelection);
    lossCounter += 1;
    console.log("Current losses: " + lossCounter);
  } else if (playerSelection === computerSelection) {
    console.log("Its a draw");
  } else if (winCounter === 3) {
    console.log("You're almost there. Great job!");
  } else if (winCounter === 4) {
    console.log("Just one more round! You got this.");
  } else if (lossCounter === 3) {
    console.log("You're down bad. Get back on your feet!");
  } else if (lossCounter === 4) {
    console.log(
      "You're actually losing to a computer??! Didn't think you were so bad"
    );
  }
}

function game() {
  while (winCounter !== 5 && lossCounter !== 5) {
    playRound(playerSelection, computerSelection);
  }
  if (winCounter === 5) {
    console.log("GG!. You win,awesome!");
  } else if (lossCounter === 5) {
    console.log("L kid you're bad. You lose");
  }
}

game();
