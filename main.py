from flask import Flask,jsonify,render_template,request
from flask_restplus import reqparse, abort, Api, Resource,apidoc
import csv
import json
import datetime as dt
import random
from flask_api import status

def get_csv():
    p = './static/dailyweather.csv'
    f = open(p, 'r')
    return list(csv.DictReader(f))

my_dict=get_csv()

app = Flask(__name__)
api = Api(app,version='1.0', title='REST API Weather Forecasting',
    description='SWAGGER UI')

parser = reqparse.RequestParser()
parser.add_argument('DATE')
parser.add_argument('TMAX')
parser.add_argument('TMIN')

@api.documentation
def custom_ui():
    return apidoc.ui_for(api)

#@api.doc(params={'id':'An ID'})
# shows a single todo item and lets you delete a todo 


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class historical(Resource):
    def get(self):
        #my_dict = get_csv()
        my_list=[]
        for value in my_dict:             
          temp_dict = {"DATE":value['DATE']}
          #print(temp_dict) 
          my_list.append(temp_dict) 
        return my_list 
     
    def post(self):
        args = parser.parse_args() 
        for i in range(len(my_dict)):
           if my_dict[i]['DATE'] == args['DATE']:
                my_dict[i].update(args) 
                temp_list ={'DATE':args['DATE']}
                return temp_list, 201
        my_dict.append(args)
        temp_list ={'DATE':args['DATE']}
        return temp_list, 201
class historical_two(Resource):   
    def get(self, date):
        # call a function, pass it the date
       # abort_if_todo_doesnt_exist(todo_id)
       #my_dict=get_csv()
       my=[]
       for value in my_dict:
           if value['DATE'] == date:
                 temp_dict ={"DATE":value['DATE'],"TMAX":float(value['TMAX']),"TMIN":float(value['TMIN'])}
                 #my.append(temp_dict)
                 return temp_dict, 200
       abort(404, message="Todo {} doesn't exist".format(date))
      
    def delete(self, date):
        #abort_if_todo_doesnt_exist(todo_id)
       # my_dict = get_csv()
        for i in range(len(my_dict)):
            if my_dict[i]['DATE']==date:
                del my_dict[i]
                return '', 204
class forecast(Resource):
     def get(self,date):
        my_list=[]
        for i in range(len(my_dict)):
         if my_dict[i]['DATE']==date:
            j=1
            count = len(my_dict) - i
            temp_dict = {"DATE":my_dict[i]['DATE'],"TMAX":float(my_dict[i]['TMAX']),"TMIN":float(my_dict[i]['TMIN'])}
            my_list.append(temp_dict)             
            while j < 7 :
              if count >1:
                  temp_dict = {"DATE":my_dict[i+j]['DATE'],"TMAX":float(my_dict[i+j]['TMAX']),"TMIN":float(my_dict[i+j]['TMIN'])}
                  my_list.append(temp_dict)
                  j=j+1
                  count =len(my_dict)-(i+j)
              else:                        
                  tmp_date = dt.datetime.strptime(date, '%Y%m%d')
                  tmp_date =str((tmp_date+dt.timedelta(days=j)).strftime('%Y%m%d'))
                  tmp_tmax=random.randint(-30,100)
                  tmp_tmin = random.randint(-1,80)
                  temp_dict={"DATE":tmp_date,"TMAX":float(tmp_tmax),"TMIN":tmp_tmin}
                  my_list.append(temp_dict)
                  j=j+1
            return my_list
        j=0
        while j < 7 :
                  tmp_date = dt.datetime.strptime(date, '%Y%m%d')
                  tmp_date =str((tmp_date+dt.timedelta(days=j)).strftime('%Y%m%d'))
                  tmp_tmax=random.randint(-30,100)
                  tmp_tmin = random.randint(-1,80)
                  temp_dict={"DATE":tmp_date,"TMAX":tmp_tmax,"TMIN":tmp_tmin}
                  my_list.append(temp_dict)
                  j=j+1
        return my_list

##               
## Actually setup the Api resource routing here
##

@app.route('/forecast_weather/')
def forecast_():
      return render_template('interactive1.html')


@app.route('/back_pro')
def get_():
     date = request.args.get('date_',0,type=str)
     my_list=[]
     for i in range(len(my_dict)):
         if my_dict[i]['DATE']==date:
            j=1
            count = len(my_dict) - i
            my_list.append(my_dict[i])
            while j < 5 :
              if count >1:
                  my_list.append(my_dict[i+j])
                  j=j+1
                  count =len(my_dict)-(i+j)
              else:                        
                  tmp_date = dt.datetime.strptime(date, '%Y%m%d')
                  tmp_date =str((tmp_date+dt.timedelta(days=j)).strftime('%Y%m%d'))
                  tmp_tmax=random.randint(-30,100)
                  tmp_tmin = random.randint(-1,80)
                  temp_dict={"DATE":tmp_date,"TMAX":tmp_tmax,"TMIN":tmp_tmin}
                  my_list.append(temp_dict)
                  j=j+1
            return jsonify(result=my_list)
     j=0
     while j <5 :
                  tmp_date = dt.datetime.strptime(date, '%Y%m%d')
                  tmp_date =str((tmp_date+dt.timedelta(days=j)).strftime('%Y%m%d'))
                  tmp_tmax=random.randint(-30,100)
                  tmp_tmin = random.randint(-1,80)
                  temp_dict={"DATE":tmp_date,"TMAX":tmp_tmax,"TMIN":tmp_tmin}
                  my_list.append(temp_dict)
                  j=j+1
     return jsonify(result=my_list)

api.add_resource(historical, '/historical/')
api.add_resource(historical_two,'/historical/<string:date>')
api.add_resource(forecast,'/forecast/<string:date>')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)

