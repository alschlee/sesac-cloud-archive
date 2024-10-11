import datetime
import json
import sys
import pymysql
import os

config = {
    "host": os.environ['RDS_HOST'], # RDS 엔드포인트 주소
    "port": os.environ['RDS_PORT'], # 포트
    "database": os.environ['RDS_DATABASE'], # 데이터베이스 이름
    "user": os.environ['RDS_USER'], # 사용자 이름
    "password": os.environ['RDS_PASSWORD'], # 비밀번호
    "cursorclass": pymysql.cursors.DictCursor
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


# 조회할 게시판 번호를 받아서 해당 게시판의 정보를 조회
# event = { "boardIdx": 1 }
def lambda_handler(event, context):
    print(event)


    with conn.cursor() as cur:
        select_query = "SELECT board_idx, title, contents, hit_cnt, created_dt, created_id FROM t_board WHERE board_idx = %s"
        cur.execute(select_query, (event["boardIdx"],))
        result = cur.fetchone()


        return {
            "statusCode": 200,
            "body": "SUCCESS",
            "data": json.dumps(result, default=json_default, ensure_ascii=False)}

