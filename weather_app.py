from .constants import *
import requests
from .db_config import *
from datetime import datetime, timedelta

class Utils():
    def __init__(self):
        pass
    

    def convert_time_IST(self,time):
        try:
            gmt_time = datetime.strptime(time, "%Y-%m-%dT%H:%M")
            ist_offset = timedelta(hours=5, minutes=30)
            ist_time = gmt_time + ist_offset

            # Format in 12-hour time with AM/PM
            ist_time = ist_time.strftime("%Y-%m-%d %I:%M %p")
            return str(ist_time)
        
        except Exception as e:
            print(f'Error Occurred. Error : {e}')


class Weather_App():
    def __init__(self):
        self.db = db_config()
        self.util = Utils()
    
    
    def get_weather_data(self,latt,logt):
        try:
            url = API.format(latitude=latt,longitude=logt)
            response = requests.get(url)
            return response.json()
        except Exception as e:
            print(f'Error Occurred. Error : {e}')


    def get_location_data(self):
        try:
            
            response = self.db.execute_query(LOCATION_TABLE_SELECT_QUERY)
            return list(response)
        
        except Exception as e:
            print(f'Error Occurred. Error: {e}')

    def process_data(self,data):
        try:
            for i in data:
                response = self.get_weather_data(i[1],i[2])
                time = self.util.convert_time_IST(response['current']['time'])
                tem = response['current']['temperature_2m']
                hum = response['current']['relative_humidity_2m']
                wind = response['current']['wind_speed_10m']
                wind_dir = response['current']['wind_direction_10m']
                rain = response['current']['rain']
                rain = response['current']['rain']
                showers = response['current']['showers']
                isday = response['current']['is_day']
                uv_id_max = response['daily']['uv_index_max'][0]
                max_tem = response['daily']['temperature_2m_max'][0]
                min_tem = response['daily']['temperature_2m_min'][0]

                query = TABLE_INSERT_QUERY.format(table=i[0],time=time,temperature=tem,humidity=hum,windspeed=wind,winddirection=wind_dir,
                                                  rain=rain,showers=showers,is_day=isday,max_temperature=max_tem,min_temperature=min_tem,ux_index_max=uv_id_max)
                # print(query)
                self.db.execute_query(query=query)
                
                print(f'Successfully inserted data to the {i[0]} Table.')

        except Exception as e :
            print(f'Error Occurred. Error : {e}')


class Start_Weather_App():
    def __init__(self):
        we_app = Weather_App()
        db = db_config()
        try:
            print('Starting the Weather Application...')
            # db.initial_table_creation()

            loc_data = we_app.get_location_data()
            pro_data = we_app.process_data(loc_data)
            
            print('The Weather Application Ended Successfully...')
        except Exception as e:
            print(f'Error Occurred. Error : {e}')
        
if __name__ == '__main__':
    pass
#    start = Start_Weather_App()
#  App.weather_app