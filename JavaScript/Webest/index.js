//by default the copy text button is hidden
var copyTextButton = document.getElementById("copyText");
copyTextButton.style.display = "none";

// by default the custom param section is disabled
var customParamSection = document.getElementById("customParamBox");
customParamSection.style.display = "none";

//if user selects json radio, then custom section should be removed
var jsonRadio = document.getElementById("json");
jsonRadio.addEventListener("click", () => {
	document.getElementById("jsonBox").style.display = "block";
	document.getElementById("customParamBox").style.display = "none";
});

//if user selects custom param radio, then json section should be removed
var customParamRadio = document.getElementById("custom");
customParamRadio.addEventListener("click", () => {
	document.getElementById("jsonBox").style.display = "none";
	document.getElementById("customParamBox").style.display = "block";
});

// add a new custom param section, when user clicks on + button
var addNewParam = document.getElementById("addParam");
var counter = 1;
addNewParam.addEventListener("click", () => {
	var param = document.getElementById("newParam");
	var newCustomParam = `<div class="form-row my-3">
	<label for="parameter${counter + 1}" style="padding-left: 9%;" class="col-sm-2 col-form-label">Paramter ${counter + 1}</label>
	<div class="col-md-4">
		<input type="text" class="form-control" id="parameter${counter + 1}-key" placeholder="Enter Parameter ${counter + 1} Key">
	</div>
	<div class=" col-md-4">
		<input type="text" class="form-control" id="parameter${counter + 1}-value" placeholder="Enter Parameter ${counter + 1} Value">
	</div>
	<button style="width: 2.3rem;" class="btn btn-primary deleteParam"> - </button>
</div>`;

	var paramToAdd = getDomElementFromString(newCustomParam);
	param.appendChild(paramToAdd);
	counter++;

	var deleteParamSection = document.getElementsByClassName("deleteParam");
	for (var item of deleteParamSection) {
		item.addEventListener("click", (e) => {
			e.target.parentElement.remove();
			counter--;
			if (counter == 0)
				counter = 1;
		});
	}
});

// function to convert to a DOM Element from String
function getDomElementFromString(data) {
	var newDiv = document.createElement("div");
	newDiv.innerHTML = data;
	return newDiv.firstChild;
}

// behavior of "Submit Request" button
var submitResp = document.getElementById("sendJsonResp");
submitResp.addEventListener("click", () => {
	//showing a dummy text to wait until response is fetched
	document.getElementById("getJsonText").value = "Fetching response. Please wait...";

	// fetch the values entered by user
	var urlValue = document.getElementById("inputURL").value;
	var requestRadio = document.getElementsByName("requestType");
	var requestRadioValue = "";
	for (var i = 0; i < requestRadio.length; i++) {
		if (requestRadio[i].checked) {
			requestRadioValue = requestRadio[i].value;
		}
	}

	var contentRadio = document.getElementsByName("contentType");
	var contentRadioValue = "";
	for (var j = 0; j < contentRadio.length; j++) {
		if (contentRadio[j].checked)
			contentRadioValue = contentRadio[j].value;
	}

	// if user selects custom parar radio, collect the data in an obj
	var userText = "";
	if (contentRadioValue == "custom") {
		data = {};
		for (var k = 1; k <= counter; k++) {
			var key = document.getElementById("parameter" + k + "-key").value;
			var value = document.getElementById("parameter" + k + "-value").value;
			data[key] = value;
		}
		userText = JSON.stringify(data);
	} else {
		//  if user selects json radio, get the value from textarea
		userText = document.getElementById("jsonText").value;
	}

	// console.log(userText);
	console.log(contentRadioValue);
	console.log(requestRadioValue);
	console.log(urlValue);
	// console.log(data);
	if (requestRadioValue == "get") {
		fetch(urlValue, {
			method: "GET"
		})
			.then((resp) => resp.text())
			.then((data) => {
				// var jsonData = JSON.parse(data).results;
				//document.getElementById("getJsonText").value = data;
				//var ugly = d
				var obj = JSON.parse(data);
				var pretty = JSON.stringify(obj, undefined, 4);
				document.getElementById('getJsonText').style.backgroundColor = '#0062cc';
				document.getElementById('getJsonText').style.color = '#fff';
				document.getElementById('getJsonText').value = pretty;
				document.getElementById("copyText").style.display = "block";
				// console.log(json.results);
			})
			.catch(function (error) {
				console.log(error);
			});
	} else {
		fetch(urlValue, {
			method: "POST",
			body: userText,
			headers: {
				"Content-type": "application/json; charset=UTF-8"
			}
		})
			.then((resp) => resp.text())
			.then((data) => {
				document.getElementById('getJsonText').style.backgroundColor = '#0062cc';
				document.getElementById('getJsonText').style.color = '#fff';
				document.getElementById("getJsonText").value = data;
				document.getElementById("copyText").style.display = "block";
			})
			.catch(function (error) {
				console.log(error);
			});
	}
});

// only displayed when there is data in the text area
// copies the data to clipboard when user click on Copy Text Button
function onCopy() {
	/* Get the text field */
	var copyText = document.getElementById("getJsonText");

	/* Select the text field */
	copyText.select();
	copyText.setSelectionRange(0, 99999); /*For mobile devices*/

	/* Copy the text inside the text field */
	document.execCommand("copy");
}

// Clears the text area and removes the copy button if there is nothing in URL Input
function onClear() {
	var request = document.getElementsByName("requestType");
	var requestValue = "";
	for (var i = 0; i < request.length; i++) {
		if (request[i].checked) {
			requestValue = request[i].value;
		}
	}
	var urlInputValue = document.getElementById("inputURL").value;
	if (urlInputValue == "") {
		if (requestValue == "post") {
			document.getElementById("jsonText").value = "";
			document.getElementById("getJsonText").value = "";
			document.getElementById('getJsonText').style.backgroundColor = 'white';
			document.getElementById('getJsonText').style.color = 'black';
			document.getElementById("copyText").style.display = "none";
		} else {
			document.getElementById("getJsonText").value = "";
			document.getElementById('getJsonText').style.backgroundColor = 'white';
			document.getElementById('getJsonText').style.color = 'black';
			document.getElementById("copyText").style.display = "none";
		}
	}
}