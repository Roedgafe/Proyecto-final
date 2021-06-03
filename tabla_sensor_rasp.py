from flask import Flask

import json

app = Flask(__name__)


@app.route('/hello.html')#crea la ruta del servidor creado
def hello():
    return 'Hello, World!'

@app.route('/data.html')#crea la ruta del servidor creado
def data():
    
    base ="""
    <!DOCTYPE html>
        <html>
        <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.24/css/jquery.dataTables.css">
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.24/js/jquery.dataTables.js"></script>
        
        <script>
        $(document).ready( function () {
            $('#table_id').DataTable();
            } );
        </script>
        </head>
        <body>
        %s

        </body>
        </html>
    """
    with open('/home/pi/datos.csv') as fin:
        data = fin.readline()
        text_td = " "
        #print (data)
        for line in fin:
            temp,pres,hum = line.split(",")
            text_td+="<tr> <td>{}</td><td>{}</td><td>{}</td> </tr>".format(temp,pres,hum)
            
        text_data = """
        <table id="table_id" class="display">

        <tr>
         <th scope="col">Temperatura</th>
         <th scope="col">Presion</th>
         <th scope="col">Humedad</th>
         
        </tr>
        <tr>
        {}
        </tr>

        </table>
        """.format(text_td)
        

        
        return base%(text_data)
    
    
@app.route('/get_data.json')#crea la ruta del servidor creado
def get_data():
    response = []
    with open('/home/pi/datos.csv') as fin:
        data = fin.readline()
        
        text_td = " "
        #print (data)
        for line in fin:
            temp,pres,hum = line.split(",")
            response.append([temp,pres,hum])
            
        jsonStr = json.dumps(response)
        return jsonStr
    
    

            
       
        
 


if __name__ == '__main__':
   app.run(host="0.0.0.0")

