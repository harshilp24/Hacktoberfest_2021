const input = document.querySelector("#inp");
const backspaceBtn = document.querySelector(".backspace");

let buffer = "0";
let previousOperator = null;
let runningTotal = 0;
const numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]; // for sec. reason

const clearInput = () => {
  buffer = 0;
  result = 0;
  previousOperator = null;
  rerender();
};

function rerender() {
  input.value = buffer;
}

function handleInput(value) {
  if (isNaN(parseInt(value))) handleSymbol(value);
  else handleNumber(value);
  rerender();
}

function handleSymbol(value) {
  switch (value) {
    case "C":
      clearInput();
      break;
    case "=":
      if (previousOperator === null) return;
      flushOperation(parseInt(buffer));
      previousOperator = null;
      buffer = "" + runningTotal;
      runningTotal = 0;
      break;
    case "←":
      if (buffer.length === 1) buffer = "0";
      else buffer = buffer.substring(0, buffer.length - 1);
      break;
    default:
      if (value === "0") return false;
      handleMath(value);
      break;
  }
}

function handleNumber(value) {
  if (!numList.includes(parseInt(value)) || value === "0") return false;
  if (buffer === 0) buffer = value;
  else buffer += value;
}

function handleMath(value) {
  const intBuffer = parseInt(buffer);
  if (runningTotal === 0) runningTotal = intBuffer;
  else flushOperation(intBuffer);
  previousOperator = value;
  buffer = "0";
}

function flushOperation(intBuffer) {
  switch (previousOperator) {
    case "+":
      runningTotal += intBuffer;
      break;
    case "-":
      runningTotal -= intBuffer;
      break;
    case "×":
      runningTotal *= intBuffer;
      break;
    case "÷":
      runningTotal /= intBuffer;
      break;
    default:
      return false;
  }
}

function init() {
  input.readOnly = true;
  document.querySelector(".inputs").addEventListener("click", (e) => {
    handleInput(e.target.innerText);
  });
  clearInput();
}
init();
