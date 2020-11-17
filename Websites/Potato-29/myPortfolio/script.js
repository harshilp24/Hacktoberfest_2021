const textE1 = document.querySelector('.rubber-letter');
const text = textE1.textContent;
const letters = text.split('');

let html = '';
const makeSpan = letter => `<span class="rubber-word">${letter}</span>`;
letters.forEach(letter => (html += makeSpan(letter)));

textE1.innerHTML = html;