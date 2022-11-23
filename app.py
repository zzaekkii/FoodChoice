from flask import Flask, request, render_template, redirect, url_for
import sqlite3

# flask app 생성
app = Flask(__name__)

# sqlite3 연결
conn = sqlite3.connect("static/db/food.db", check_same_thread=False)
cursor = conn.cursor()


# 현재 포인터 위치, 즉 어떤 옵션을 선택하고 있는지
global counter
counter = 0

# 옵션 목록
option_list = [
    ["korea", " 한식은 어떠신가요?"],
    ["china", " 중식은 어떠신가요?"],
    ["western", " 양식은 어떠신가요?"],
    ["japan", "일식은 어떠신가요?"],
    ["etc", " 한/중/일/양식 외의 음식도 추천해드릴까요?"],
    ["snack", " 간단하게 분식은 어떠신가요?"],
    ["spicy", " 매콤한 요리는 어떠신가요?"],
    ["hot", " 뜨끈한 요리는 어떠신가요?"],
    ["cold", " 시원한 요리는 어떠신가요?"],
    ["crispy", " 바삭한 요리를 원하시나요?"],
    ["soup", " 국물이 있는 요리를 원하시나요?"],
    ["diet", " 다이어트 중이신가요?"],
    ["vegan", " 비건이신가요?"],
    ["meat", " 고기가 드시고 싶으신가요?"],
    ["seafood", " 해산물이 들어간 음식은 어떠신가요?"],
    ["rice", " 쌀밥이 포함된 메뉴를 원하시나요?"],
    ["noodle", "면요리는 어떠신가요?"],
    ["bread", " 빵이 메인인 음식은 어떠신가요?"],
    ["alchol", " 해장이 필요하신가요"],
]

choice_list = [0 for i in range(19)]

# 결과 추출
def result():
    # 쿼리 생성
    query = "SELECT foodname FROM food WHERE "
    for i in range(0, 19):
        if choice_list[i] == "2":
            query += f"({option_list[i][0]}=0 OR {option_list[i][0]}=1 OR {option_list[i][0]}=2) AND "
        else:
            query += f"{option_list[i][0]}={choice_list[i]} AND "
    query = query[:-5]
    query += " order by hit"
    # print(query)
    cursor.execute(query)

    # 해당하는 결과 없을 때
    try:
        query_result = cursor.fetchone()[0]

        # print(cursor.fetchmany(3))

        # 조회수 확인
        cursor.execute(f"SELECT hit FROM food WHERE foodname='{query_result}'")
        hit = cursor.fetchone()[0]

        # 조회수 추가
        cursor.execute(
            f"UPDATE food SET hit={int(hit)+1} WHERE foodname='{query_result}'"
        )
        conn.commit()

    except:
        query_result = "결과 없음"

    return query_result


# 메인 화면
@app.route("/")
@app.route("/index.html")
def root():
    global counter

    # 포인터 초기화
    counter = 0
    return render_template("index.html")


# 선택 화면 출력
@app.route("/choice/<int:option>")
def choice(option):
    # 선택이 끝날 경우
    if option == 19:
        return render_template("result.html", choice=result())

    else:
        return render_template(
            "choice.html",
            option=option,
            choice=option_list[option][0],
            disc=option_list[option][1],
        )


# 컨트롤러
@app.route("/controller/<option>")
def controller(option):
    global counter

    if option == "back":
        # 음수되는 것 방지
        if counter > 0:
            counter -= 1
        return redirect(url_for("choice", option=counter))

    else:
        choice_list[counter] = option

        # 포인터 위치 옮기기
        counter += 1

        return redirect(url_for("choice", option=counter))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5252")
