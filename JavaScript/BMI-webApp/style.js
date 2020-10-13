function BMI(){
		var w=document.getElementById('w').value;
		var h=document.getElementById('h').value;
		var bmi=w/(h/100*h/100);
		document.getElementById("result").innerHTML="Your BMI is" + bmi;
		}