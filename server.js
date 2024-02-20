const { error } = require('console')
const exp=require('express')
const { stderr } = require('process')
const app=exp()
const {exec} = require('child_process')

app.use(exp.json())

app.get('',(req,res)=>{
    res.send({message:"hello, welcome to OTP generator API, its free to use , to acces this resource Contact : UPPUNURI GOUTHAM REDDY ,IT-C,VNR VJIET"})
})

app.get('/getOtp/:email',(req,res)=>{
    console.log(req.params.email)

    const pythonScript = `python otp.py ${req.params.email}`;

    exec(pythonScript,(error,stdout,stderr)=>{
        if(error)
        {
            res.send({message:`email received : ${req.params.email}`,paylod:0,status:"F"})
        }
        else
        {
            res.send({message:`email received : ${req.params.email}`,paylod:String(stdout).substring(0,6),status:"T"})
        }
    })
    
})


app.listen(4000,()=>{console.log("server running on port 4000...")})