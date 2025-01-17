# db 세팅, 종류가 추가될 때 사용
# 실행 시, 쿼리가 전부 초기화되므로 주의 (hit 값 초기화됨)
import sqlite3

conn = sqlite3.connect("static/db/food.db")
cursor = conn.cursor()

# 테이블 생성
cursor.execute("DROP TABLE IF EXISTS food")
cursor.execute(
    "CREATE TABLE food( \
    foodname TEXT, \
    korea INT, \
    china INT, \
    western INT, \
    japan INT, \
    etc INT, \
    snack INT, \
    spicy INT, \
    hot INT, \
    cold INT, \
    crispy INT, \
    soup INT, \
    diet INT, \
    vegan INT, \
    meat INT, \
    seafood INT, \
    rice INT, \
    noodle INT, \
    bread INT, \
    alchol INT, \
    hit INT)"
)

# 음식 추가
cursor.execute(
    "INSERT INTO food VALUES \
    ('닭갈비',0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0), \
    ('간장 찜닭',0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,1,0), \
    ('고추장 찜닭',0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0), \
    ('닭볶음탕',0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,1,0), \
    ('간장 불고기',0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0), \
    ('제육볶음(고추장 불고기)',0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0), \
    ('제육덮밥',0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0), \
    ('두루치기',0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0), \
    ('오삼 불고기',0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,0), \
    ('갈비찜',0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,1,0), \
    ('주꾸미 볶음',0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0), \
    ('수육',0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0), \
    ('햄버거',1,1,0,1,1,1,1,2,1,2,1,1,1,0,2,1,1,0,1,0), \
    ('돈까스',1,1,1,0,1,0,1,0,1,2,1,1,1,0,1,1,1,1,1,0), \
    ('후라이드 치킨',1,1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0), \
    ('간장 치킨',0,1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0), \
    ('양념 치킨',0,1,0,1,1,1,0,0,1,1,1,1,1,0,1,1,1,1,1,0), \
    ('피자',1,1,0,1,1,1,1,0,1,2,1,1,0,2,2,1,1,0,1,0), \
    ('황태해장국',0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,0,0), \
    ('육개장',0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0), \
    ('선지국밥',0,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0), \
    ('굴국밥',0,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,0,0), \
    ('콩나물국밥',0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,0), \
    ('돼지국밥',0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0), \
    ('순대국밥',0,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,0,0), \
    ('추어탕',0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0), \
    ('샤브샤브',0,1,1,0,0,1,2,0,1,1,0,1,1,0,2,2,2,1,0,0), \
    ('쌈밥',0,1,1,1,1,1,1,0,1,1,1,1,0,1,2,0,1,1,1,0), \
    ('초밥',1,1,1,0,1,1,1,1,2,1,1,1,1,1,0,0,1,1,1,0), \
    ('매운탕',0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0), \
    ('설렁탕',0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0), \
    ('갈비탕',0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0), \
    ('삼계탕',0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0), \
    ('김치볶음밥',0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,0), \
    ('라볶이',0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,0,1,1,0), \
    ('떡볶이',0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0), \
    ('쫄면',0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,0), \
    ('라면',0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,0,1,0,0), \
    ('라멘',1,1,1,0,1,1,1,0,1,1,0,1,0,2,1,1,0,1,0,0), \
    ('규동',1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0), \
    ('텐동(튀김덮밥)',1,1,1,0,1,1,1,0,1,0,1,1,0,0,2,0,1,1,1,0), \
    ('카츠동',1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0), \
    ('연어덮밥',1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0), \
    ('메밀소바',1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1,0), \
    ('오므라이스',1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0), \
    ('카레',1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,0), \
    ('김밥',0,1,1,1,1,0,1,2,2,1,1,1,0,1,2,0,1,1,1,0), \
    ('곱창,막창,대창',0,1,1,1,1,1,2,0,1,1,1,1,1,1,1,1,1,1,1,0), \
    ('토스트',2,2,2,2,2,0,1,0,1,0,1,1,0,2,1,1,1,0,1,0), \
    ('샌드위치',2,2,2,2,2,0,1,1,2,1,1,1,0,2,1,1,1,0,1,0), \
    ('수제비',0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0), \
    ('비빔국수',0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,0), \
    ('칼국수',0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,1,0,1,0,0), \
    ('잔치국수',0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,1,0,1,1,0), \
    ('콩국수',0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,1,1,0), \
    ('물냉면',0,1,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,1,1,0), \
    ('비빔냉면',0,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,0,1,1,0), \
    ('밀면',0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,0,1,1,0), \
    ('비빔밀면',0,1,1,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,1,0), \
    ('회',0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0), \
    ('훈제 오리고기',2,2,2,2,2,1,1,0,1,2,1,1,1,0,1,0,1,1,1,0), \
    ('양념 오리고기',2,2,2,2,2,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0), \
    ('돼지구이',2,2,2,2,2,1,1,0,1,2,1,1,1,0,1,0,1,1,1,0), \
    ('소고기구이',2,2,2,2,2,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0), \
    ('장어구이',2,2,2,2,2,1,1,0,1,2,1,1,1,1,0,0,1,1,1,0), \
    ('생선구이',2,2,2,2,2,1,1,0,1,2,1,1,1,1,0,0,1,1,1,0), \
    ('육회덮밥',0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,0), \
    ('부대찌개',0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0), \
    ('김치찌개',0,1,1,1,1,1,0,0,1,1,0,1,0,2,1,0,1,1,0,0), \
    ('된장찌개',0,1,1,1,1,1,1,0,1,1,0,1,0,2,1,0,1,1,0,0), \
    ('짜장면',1,0,1,1,1,1,1,2,2,1,1,1,0,1,1,1,0,1,1,0), \
    ('짜장밥',1,0,1,1,1,1,1,2,2,1,1,1,0,1,1,0,1,1,1,0), \
    ('우육면',1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,0,0), \
    ('짬뽕',1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1,0,1,0,0), \
    ('마라탕',1,0,1,1,1,1,0,0,1,1,0,1,1,2,1,0,1,1,1,0), \
    ('우동',2,2,2,2,2,1,1,0,1,1,0,1,0,1,1,1,0,1,0,0), \
    ('탕수육',1,0,1,1,1,1,1,2,2,0,1,1,1,0,1,1,1,1,1,0), \
    ('뼈해장국',0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0), \
    ('감자탕',0,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0), \
    ('토마토 스파게티',1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0), \
    ('까르보나라',1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0), \
    ('로제 스파게티',1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0), \
    ('리조또',1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0), \
    ('빠네 파스타',1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,0,1,0), \
    ('알리오올리오',1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0), \
    ('스테이크',1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0), \
    ('뷔페',2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0), \
    ('비빔밥',0,1,1,1,1,1,2,2,2,1,1,0,0,1,1,0,1,1,1,0), \
    ('알밥',0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0), \
    ('보쌈',0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0), \
    ('족발',0,1,1,1,1,1,1,2,2,1,1,1,1,0,1,1,1,1,1,0), \
    ('양고기',2,2,2,2,2,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0), \
    ('김치찜',0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,1,0), \
    ('해물탕',0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0), \
    ('쌀국수',1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,0,0), \
    ('대게,킹크랩',2,2,2,2,2,1,1,2,2,1,1,1,1,1,0,1,1,1,1,0), \
    ('해물찜',0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0), \
    ('타코야키',1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,0), \
    ('해물파전',0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0), \
    ('와플',1,1,1,1,1,0,1,1,2,0,1,1,0,1,1,1,1,0,1,0), \
    ('닭가슴살',2,2,2,2,2,1,1,2,2,1,1,0,1,0,1,1,1,1,1,0), \
    ('샐러드',2,2,2,2,2,1,1,1,2,1,1,0,0,1,1,1,1,1,1,0), \
    ('타코',1,1,1,1,0,1,1,2,2,1,1,1,1,0,1,1,1,1,1,0), \
    ('수육튀김',0,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0), \
    ('아구찜',0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0), \
    ('닭백숙',0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0), \
    ('오리백숙',0,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0), \
    ('고기만두',0,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0), \
    ('김치만두',0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0), \
    ('새우만두',0,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,0), \
    ('샤오롱바오',1,0,1,1,1,1,1,0,1,1,1,1,1,2,2,1,1,1,1,0), \
    ('철판 쭈꾸미',0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0), \
    ('전골',0,1,1,1,1,1,2,0,1,1,0,1,1,2,2,0,2,1,0,0)"
)
conn.commit()
conn.close()

