import requests,json
import pymysql


con_105 = pymysql.connect(host='140.143.207.92', user='root', passwd='wjx411527', db='tests', port=3306, charset='utf8mb4')
cur_105 = con_105.cursor()
cur_105.execute('CREATE TABLE IF NOT EXISTS hskonline_exam_id (id int not null auto_increment primary key, exam_id varchar(6), level_id varchar(6), title varchar(28), level_title varchar(28) unique)')


for i in range(1,14252):
    url = 'http://api.hskonline.com/v1/exam/exercise?access_token=c9_Mh5xlemaCXAlv5CL7Ae9Hb_Lk_z5s&exam_id={}'.format(str(i))
    response = requests.get(url)
    data = json.loads(response.text)
    exam_id = i
    level_id = data['level_id']
    title = data['title']
    level_title = str(data['level_id']) + '_' + data['title']

    onedata = (exam_id, level_id, title, level_title)
    sql = 'replace into hskonline_exam_id (exam_id, level_id, title, level_title) value (%s,%s,%s,%s)'
    cur_105.execute(sql, onedata)
    con_105.commit()

cur_105.close()
con_105.close()