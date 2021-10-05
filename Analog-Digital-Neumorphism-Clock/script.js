// Made by Nitin Kushwaha

const hr = document.querySelector("#hr");
const min = document.querySelector("#min");
const sec = document.querySelector("#sec");
const clockd = document.getElementById("clock-d");
const clocka = document.getElementById("clock-a");
let h,m,s;
let d;

setInterval(() => {
    const day = new Date();
    h = day.getHours();
    m = day.getMinutes();
    s = day.getSeconds();

    hr.style.transform = `rotate(${h*30 + m/2}deg)`;
    min.style.transform = `rotate(${m*6 + s/10}deg)`;
    sec.style.transform = `rotate(${s*6}deg)`;

    setday();
    addzero();
    clockd.textContent = h + ":" + m + ":" + s + " " + d ;

    if(window.innerHeight==screen.height){
        change.style.display="none";
        theme.style.display="none";
    }
    else{
        change.style.display="block";
        theme.style.display="block";
    }
},100);

function addzero(){
    if(h<10){
        h = "0" + h;
    }
    if(m<10){
        m =  "0" + m;
    }
    if(s<10){
        s =  "0" + s;
    }
}

function setday(){
    if(h>12){
        h = h - 12;
        d = "PM";
    }
    else{
        if(h==0){
            h=12;
        }
        d = "AM";
    }
}

const change = document.querySelector("#change");

function toggleClock(e){
    let target = e.target;

    if(target.textContent == "Digital"){
        document.querySelector(".flip-card-inner").classList.add("flip");
        target.textContent = "Analog";
    }
    else{
        document.querySelector(".flip-card-inner").classList.remove("flip");
        target.textContent = "Digital";
    }
}

change.addEventListener("click",toggleClock);

const theme = document.querySelector("#theme");

function toggleTheme(e){
    let target = e.target;

    reset(e);

    if(target.textContent == "Light"){
        target.textContent = "Dark";
        document.body.classList.remove("theme-dark");
        document.body.classList.add("theme-light");
    }
    else{
        target.textContent = "Light";
        document.body.classList.remove("theme-light");
        document.body.classList.add("theme-dark");
    }

}

theme.addEventListener("click",toggleTheme);

/*-------------settings--------------*/

/*------gear------*/
const settingWindow = document.querySelector("#setting-window")
const setting = document.querySelector("#setting-icon");

setting.addEventListener("click", function(){
    setting.classList.toggle("rotate");
    settingWindow.classList.toggle("show");
});

/*------setting window------*/

const setSize = document.querySelector("#size");
const sizeLabel = document.querySelector("label")

const setBackground = document.querySelector("#background");

const setShadowBlur = document.querySelector("#shadow-blur");
const setShadowColor = document.querySelector("#shadow-color");

const setHrHandColor = document.querySelector("#hr-color");
// const setHrHandColorText = document.querySelector("#hr-color-text");
const setMinHandColor = document.querySelector("#min-color");
// const setMinHandColorText = document.querySelector("#min-color-text");
const setSecHandColor = document.querySelector("#sec-color");
// const setSecHandColorText = document.querySelector("#sec-color-text");

const setBorderWidth = document.querySelector("#border-width");
const setBorderColor = document.querySelector("#border-color");

/*------size------*/
// let caSize = document.querySelector("#clock-a").clientHeight;

//size
setSize.addEventListener("input",()=>{
    clocka.style.transform = `scale(${setSize.value})`;
    clockd.style.transform = `scale(${setSize.value})`;
    sizeLabel.textContent = setSize.value;
});

//backgroundcolor
setBackground.addEventListener("input",()=>{
    document.querySelector(".flip-card-front").style.backgroundColor = 
    document.querySelector(".flip-card-back").style.backgroundColor =
    clockd.style.backgroundColor =
    document.body.style.backgroundColor = 
    setBackground.value;
});

//shadow
setshadow=()=>{
    clocka.style.boxShadow = `-8px -8px 15px rgba(255,255,255,0.05), 
    inset -8px -8px 15px rgba(255,255,255,0.05),
    20px 20px 20px rgba(0, 0, 0, 0.3), 
    inset 20px 20px 20px rgba(0, 0, 0, 0.3),
    0px 0px ${setShadowBlur.value}px ${setShadowColor.value}`;

    clockd.style.boxShadow = `-8px -8px 15px rgba(255,255,255,0.05), 
    inset -8px -8px 15px rgba(255,255,255,0.05),
    20px 20px 20px rgba(0, 0, 0, 0.3), 
    inset 20px 20px 20px rgba(0, 0, 0, 0.3),
    0px 0px ${setShadowBlur.value}px ${setShadowColor.value}`;
}

setShadowBlur.addEventListener("input",setshadow);
setShadowColor.addEventListener("input",setshadow);

//Hand color 
setHrHandColor.addEventListener("input",()=>{
    document.querySelector("#h").style.backgroundColor = setHrHandColor.value;
});

setMinHandColor.addEventListener("input",()=>{
    document.querySelector("#m").style.backgroundColor = setMinHandColor.value;
});

setSecHandColor.addEventListener("input",()=>{
    document.querySelector("#s").style.backgroundColor = setSecHandColor.value;
});

//Border
setborder=()=>{
    clocka.style.border = `${setBorderWidth.value}px solid ${setBorderColor.value}`;
    clockd.style.border = `${setBorderWidth.value}px solid ${setBorderColor.value}`;
}

setBorderWidth.addEventListener("input",setborder);
setBorderColor.addEventListener("input",setborder);

//reset
function reset(e){
    if(e.target.textContent == "Light"){
        document.querySelector(".flip-card-front").style.backgroundColor =
        document.querySelector(".flip-card-back").style.backgroundColor =
        clockd.style.backgroundColor =
        document.body.style.backgroundColor = "#d1dae3";
    }
    else{
        document.querySelector(".flip-card-front").style.backgroundColor =
        document.querySelector(".flip-card-back").style.backgroundColor =
        clockd.style.backgroundColor =
        document.body.style.backgroundColor = "#202020";
    }

    clocka.style.boxShadow ="";
    clockd.style.boxShadow ="";

    document.querySelector("#h").style.backgroundColor = "";
    document.querySelector("#m").style.backgroundColor = "";
    document.querySelector("#s").style.backgroundColor = "";

    clocka.style.border = "";
    clockd.style.border = "";
}