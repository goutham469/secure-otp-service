const { error } = require('console')
const exp=require('express')
const { stderr } = require('process')
const app=exp()
const {exec} = require('child_process')
const cors=require('cors')

require("dotenv").config()

app.use(exp.json())
app.use(cors())

app.get('',(req,res)=>{
    res.send({message:"hello, welcome to OTP generator API, its free to use , to acces this resource Contact : UPPUNURI GOUTHAM REDDY ,IT-C,VNR VJIET"})
})

app.get('/getOtp/:email',(req,res)=>{
    console.log(req.params.email)

    let SENDER_MAIL = process.env.SENDER_MAIL;
    let SENDER_KEY = process.env.SENDER_KEY;

    const pythonScript = `python otp.py ${req.params.email} ${SENDER_MAIL} ${SENDER_KEY}`;

    exec(pythonScript,(error,stdout,stderr)=>{
        if(error)
        {
            res.send({message:`email received : ${req.params.email}`,paylod:0,status:"F",errorMessage:error})
        }
        else
        {
            console.log(SENDER_MAIL)
            console.log(SENDER_KEY)
            res.send({message:`email received : ${req.params.email}`,paylod:stdout,status:"T"})
        }
    })
    
})




app.listen(4000,()=>{console.log("server running on port 4000...")})
