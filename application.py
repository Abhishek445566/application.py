from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
  def index2():
    return render_template("index.html")
    
@app.route("/services")
  def service():
    return return_template("service.html")
  
  @app.route("/more")
  def more():
    return return_template("more.html")

