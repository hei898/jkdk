from jkdk import Jkdk
import os
# import argparse

# parser = argparse.ArgumentParser(description='填入学号和密码')
# parser.add_argument('-c', '--credit', required=True, help='学号')
# parser.add_argument('-p', '--password', required=True, help='密码')

# outputs = parser.parse_args()
# print(f'credit={outputs.credit}, password={outputs.password}')

username_list = os.environ.get('username')
password_list = os.environ.get('password')
key = os.environ.get('key')
province = os.environ.get('province')
city = os.environ.get('city')
position = os.environ.get('position')
city = province+city
myvs_26 = os.environ.get('myvs_26', 2)
jingdu = os.environ.get('jingdu', '113.534090')
weidu = os.environ.get('weidu', '34.813699')

username_list = username_list.split(',')
password_list = password_list.split(",")

for i in range(len(password_list)):
    
    username = username_list[i]
    password = password_list[i]
    
    print(f'username={username}')
    print(f'password={password}')
    print(f'SCKEY={key}')
    print(f'province={province}')
    print(f'city={city}')
    print(f'position={position}')
    print(f'longitude={jingdu}')
    print(f'gratitude={weidu}')

    if key == '':
        key = None
    m = Jkdk(username, password, key, province=province,
             city=city, position=position, myvs_26=myvs_26, jingdu=jingdu, weidu=weidu)
    m.jkdk()
