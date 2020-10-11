//init speechSynth API
const synth = window.speechSynthesis;

//DOM Elements
const textForm = document.querySelector('form');
const textInput = document.querySelector('#text-input');
const voiceSelect = document.querySelector('#voice-select');
const rate = document.querySelector('#rate');
const rateValue = document.querySelector('#rate-value');
const pitch = document.querySelector('#pitch');
const pitchValue = document.querySelector('#pitch-value');
const body = document.querySelector('body');

//Browser identifier	
// Firefox 1.0+	
var isFirefox = typeof InstallTrigger !== 'undefined';	
		
// Chrome 1+	
var isChrome = !!window.chrome && !!window.chrome.webstore;

//Init Voices Array
let voices = [];

const getVoices = () => {
    voices = synth.getVoices();

    //loop through voices and create an option for each one
    voices.forEach(voice => {

        //Create an option element
        const option = document.createElement('option');

        //fill option with voice name and language
        option.textContent = voice.name + '('+ voice.lang +')';

        //set needed option attribute
        option.setAttribute('data-lang', voice.lang);
        option.setAttribute('data-name', voice.name);
        voiceSelect.append(option);

    });
}

getVoices();
if(synth.onvoiceschanged !== undefined) {
    synth.onvoiceschanged = getVoices;
} 



/*
//Fix for duplication, run code depending on thebrowser	(if problem occur)
if (isFirefox) {	
    getVoices();
}	
getVoices();	
if (isChrome) {	
    if (synth.onvoiceschanged !== undefined) {	
        synth.onvoiceschanged = getVoices;	
    }	
}
*/


//Speak Function
const speak = () => {

    //check if speaking
    if(synth.speaking) {
        console.error('Already Speaking...');
        return;
    }
    if(textInput.value !== '') {

        // Add background Animation
        body.style.background = '#000000 url(images/wave-blue.gif)';
        body.style.backgroundRepeat = 'repeat-x';
        // body.style.paddingBottom = '30%';
        body.style.backgroundSize = '100% 50%';

        //Get speak text
        const speakText = new SpeechSynthesisUtterance(textInput.value);
        //Speak end
        speakText.onend = e => {
            console.log('Done Speaking...');
            body.style.background = '#000000';
        }

        //speak error
        speakText.onerror = e => {
            console.error('Something went wrong');
        }

        //Selected Voice
        const selectedVoice = voiceSelect.selectedOptions[0].getAttribute('data-name');
        
        // Loop through voices
        voices.forEach(voice => {
            if(voice.name === selectedVoice) {
                speakText.voice = voice;
            }
        });

        //Set Pitch and Rate
        speakText.rate = rate.value;
        speakText.pitch = pitch.value;

        //Speak
        synth.speak(speakText);

    }
};

// EVENT LISTENERS

// text form submit

textForm.addEventListener('submit', e => {
    e.preventDefault();

    //speak
    speak();

    textInput.blur();
});

// Rate Value Change
rate.addEventListener('change', e => (rateValue.textContent = rate.value));

// Pitch Value Change
pitch.addEventListener('change', e => (pitchValue.textContent = pitch.value));

// Voice Select Change
voiceSelect.addEventListener('change', e => speak());
