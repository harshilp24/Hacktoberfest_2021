const options = ["Rock", "Paper", "Scissors"];
let computerSelection;
const buttons = document.querySelectorAll(".player-button");
const message = document.querySelector(".message");
const scoreMessage = document.querySelector(".score-message");
let playerSelection;
let winCounter = 0,
  lossCounter = 0;
function computerPlay() {
  return options[Math.floor(Math.random() * options.length)];
}

function playRound(playerSelection, computerSelection) {
  if (
    (playerSelection === "rock" && computerSelection === "scissors") ||
    (playerSelection === "paper" && computerSelection === "rock") ||
    (playerSelection === "scissors" && computerSelection === "paper")
  ) {
    scoreMessage.textContent =
      "You Win. " +
      (playerSelection.charAt(0).toUpperCase() + playerSelection.substring(1)) +
      " beats " +
      (computerSelection.charAt(0).toUpperCase() +
        computerSelection.substring(1));
    winCounter += 1;
  } else if (
    (computerSelection === "rock" && playerSelection === "scissors") ||
    (computerSelection === "paper" && playerSelection === "rock") ||
    (computerSelection === "scissors" && playerSelection === "paper")
  ) {
    scoreMessage.textContent =
      "You lose. " +
      (computerSelection.charAt(0).toUpperCase() +
        computerSelection.substring(1)) +
      " beats " +
      (playerSelection.charAt(0).toUpperCase() + playerSelection.substring(1));
    lossCounter += 1;
  } else if (playerSelection === computerSelection) {
    scoreMessage.textContent = "Its a draw";
  }
}

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    const playerImage = button.querySelector(".player-image");

    playerSelection = playerImage.alt.toLowerCase();
    computerSelection = computerPlay().toLowerCase();
    playClickSound();
    playRound(playerSelection, computerSelection);
    changePlayerButtonBackground();
    changeComputerButtonBackground();
    displayMessage();
    displayScore();
  });
});

function displayMessage() {
  if (winCounter === 3) {
    message.textContent = "You're almost there. Great job!";
  } else if (winCounter === 4) {
    message.textContent = "Just one more round! You got this.";
  } else if (lossCounter === 3) {
    message.textContent = "You're down bad. Get back on your feet!";
  } else if (lossCounter === 4) {
    message.textContent =
      "You're actually losing to a computer?! Didn't think you were so bad.";
  }
  if (winCounter === 5) {
    const winSound = document.querySelector(".win-sound");
    winSound.play();
    loadFinalMessage("You Win, Great Job! Do you want to play again?");
  }
  if (lossCounter === 5) {
    const lossSound = document.querySelector(".loss-sound");
    lossSound.play();
    loadFinalMessage("You Lose, Unlucky! Would you like to try again?");
  }
}

function playClickSound() {
  const clickSound = document.querySelector(".click-sound");
  clickSound.play();
}

function displayScore() {
  document.querySelector(".player-score").textContent = winCounter;
  document.querySelector(".computer-score").textContent = lossCounter;
}

function loadFinalMessage(winLossMessage) {
  document.querySelector("main").remove();
  document.querySelector("header").remove();
  const para = document.createElement("p");
  const resetButton = document.createElement("button");
  const body = document.querySelector("body");
  para.textContent = winLossMessage;
  resetButton.textContent = "Play Again";
  body.appendChild(para);
  body.appendChild(resetButton);
  resetButton.classList.toggle("reset-btn");
  para.classList.toggle("final-message");
  resetButton.addEventListener("click", () => {
    setTimeout(function () {
      location.reload();
    }, 100);
  });
}

function changePlayerButtonBackground() {
  const playerRock = document.querySelector(".player-rock");
  const playerPaper = document.querySelector(".player-paper");
  const playerScissors = document.querySelector(".player-scissors");
  if (playerSelection === "paper") {
    playerPaper.style.backgroundColor = "#8685ef";
    playerScissors.style.backgroundColor = "rgb(51, 51, 51)";
    playerRock.style.backgroundColor = "rgb(51, 51, 51)";
  } else if (playerSelection === "rock") {
    playerRock.style.backgroundColor = "#8685ef";
    playerScissors.style.backgroundColor = "rgb(51, 51, 51)";
    playerPaper.style.backgroundColor = "rgb(51, 51, 51)";
  } else if (playerSelection === "scissors") {
    playerScissors.style.backgroundColor = "#8685ef";
    playerPaper.style.backgroundColor = "rgb(51, 51, 51)";
    playerRock.style.backgroundColor = "rgb(51, 51, 51)";
  }
}

function changeComputerButtonBackground() {
  const computerRock = document.querySelector(".computer-rock");
  const computerPaper = document.querySelector(".computer-paper");
  const computerScissors = document.querySelector(".computer-scissors");
  if (computerSelection === "paper") {
    computerPaper.style.backgroundColor = "#FF83B1";
    computerScissors.style.backgroundColor = "rgb(51, 51, 51)";
    computerRock.style.backgroundColor = "rgb(51, 51, 51)";
  } else if (computerSelection === "rock") {
    computerRock.style.backgroundColor = "#FF83B1";
    computerScissors.style.backgroundColor = "rgb(51, 51, 51)";
    computerPaper.style.backgroundColor = "rgb(51, 51, 51)";
  } else if (computerSelection === "scissors") {
    computerScissors.style.backgroundColor = "#FF83B1";
    computerRock.style.backgroundColor = "rgb(51, 51, 51)";
    computerPaper.style.backgroundColor = "rgb(51, 51, 51)";
  }
}
