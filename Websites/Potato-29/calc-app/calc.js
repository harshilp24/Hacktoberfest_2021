const express = require("express")
const app = express()

const bodyParser = require("body-parser")

app.use(bodyParser.urlencoded({extended: true}))

app.get("/", function(req, res){
    res.sendFile(__dirname + "/bmiCalc.html")
})

app.post("/", function(req, res){
    var height = Number(req.body.h);
    var weight = Number(req.body.w);
    var result = weight/(height * height);
    res.send("the ans is " + result);
})


app.listen(3000, function(){
    console.log("Server started")
})