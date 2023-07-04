from flask import Flask, request

app= Flask(__name__)

#Route

@app.route("/")
def welcome():
    return "Hello world"


@app.route('/aboutus')
def aboutus():
    return "We are ineuron"

@app.route('/demo',methods=['POST'])
def math_operation():
    if(request.method=='POST'):
        operation= request.json['operation']
        num1= request.json['num1']
        num2= request.json['num2']
        result=num1 + num2

        return "The operation is {} and the result is {}".format(operation,result)

@app.route('/multiply',methods=['POST'])
def multiply_operation():
    if(request.method=='POST'):
        operation= request.json['operation']
        num1= request.json['num1']
        num2= request.json['num2']
        result=num1 * num2

        return "The operation is {} and the result is {}".format(operation,result)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5001)
    