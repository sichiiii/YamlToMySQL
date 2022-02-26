import yaml, mysql, mysql.connector

from datetime import date
from flask import Flask

app = Flask(__name__)

@app.route('/a')
def a():
    try:
        toys_yaml = open("toys.yaml", 'r')
        input_dict = yaml.load(toys_yaml, Loader=yaml.FullLoader)
        output_dict = {'toys':[]}
        for i in input_dict['toys']:
            delta = date.today() - i['status_updated']
            if int(str(delta).split(' ')[0]) < 8:    #delta.days не работало :\
                output_dict['toys'].append(i)
        if len(output_dict['toys']) > 0:
            toys_table = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='Test'
            )
            toys_cursor = toys_table.cursor()
            for i in output_dict['toys']:
                query= f"""
                    INSERT INTO toys
                    (toy_id, name, status, status_updated)
                    VALUES ( '{i['id']}', '{i['name']}', '{i['status']}', '{i['status_updated']}');
                """
                try:
                    toys_cursor.execute(query)
                except:
                    print('exists')
            toys_table.commit()
        return 'ok'
    except Exception as ex:
        return str(ex)
  
@app.route('/b')
def b():
    try:
        games_yaml = open("games.yaml", 'r')
        input_dict = yaml.load(games_yaml, Loader=yaml.FullLoader)
        output_dict = {'games':[]}
        for i in input_dict['games']:
            delta = date.today() - i['date']
            if int(str(delta).split(' ')[0]) < 8:    #delta.days не работало :\
                output_dict['games'].append(i)
        if len(output_dict['games']) > 0:
            games_table = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='Test'
            )
            games_cursor = games_table.cursor()
            for i in output_dict['games']:
                query= f"""
                    INSERT INTO games
                    (game_id, name, date)
                    VALUES ( '{i['id']}', '{i['name']}', '{i['date']}');
                """
                try:
                    games_cursor.execute(query)
                except:
                    print('exists')
            games_table.commit()
        return 'ok'
    except Exception as ex:
        return str(ex)
  
if __name__ == '__main__':
    app.run()