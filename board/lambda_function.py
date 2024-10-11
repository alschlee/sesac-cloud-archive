import datetime
import json
import sys
import pymysql

config = {
    "host": "myrds.#####.ap-northeast-2.rds.amazonaws.com", # RDS 엔드포인트
    "port": 3306, # 포트
    "database": "sampledb", # 데이터베이스 이름
    "user": "admin", # 사용자 이름
    "password": "password" # 비밀번호
}


try:
    conn = pymysql.connect(**config)    
except Exception as e:
    print("ERROR: Could not connect to MariaDB")
    sys.exit()  


print("SUCCESS: Connection to RDS MariaDB instance succeeded")


def json_default(value):
    if isinstance(value, datetime.date):
        return value.strftime('%Y-%m-%d')
    raise TypeError('not JSON serializable')


# event = { "title": "제목", "contents": "내용", "user": "사용자 이름" }
def lambda_handler(event, context):
    print(event)


    with conn.cursor() as cur:
        query = "INSERT INTO t_board(title, contents, created_id, created_dt) VALUES(%s, %s, %s, CURRENT_TIMESTAMP)"
        cur.execute(query, (event["title"], event["contents"], event["user"]))
        conn.commit()
       
        select_query = "SELECT * FROM t_board"
        cur.execute(select_query)
        result = cur.fetchall()


        return {
            "statusCode": 200,
            "body": "SUCCESS",
            "data": json.dumps(result, default=json_default, ensure_ascii=False)}

