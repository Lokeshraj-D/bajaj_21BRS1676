from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/bfhl", methods = ["POST", "GET"])
def get_res():
    if(request.method=="GET"):
        user_data={
            "operation_code" :1
        }
        return jsonify(user_data), 200
    
    datareq = request.get_json()

    data = datareq["data"]

    user_data={"is_success": True, 
                "user_id" : "lokeshraj_d_24032004",
                "email": "lokeshraj@xyz.com",
                "roll_number": "21BRS1676",
                }

    numbers = []
    alphabets = []
    highest_lowercase_alphabet = ""

    for ele in data:
        if (ele.isdigit()):
            numbers.append(ele)
            continue
        if(ele==""):
            continue
        alphabets.append(ele)
        if (ord(ele)>=97 and ord(ele)<=122):
            if(highest_lowercase_alphabet==""):
                highest_lowercase_alphabet=ele
            else:
                highest_lowercase_alphabet = ele if ord(ele) > ord(highest_lowercase_alphabet) else highest_lowercase_alphabet

    user_data["numbers"] = numbers
    user_data["alphabets"] = alphabets
    user_data["highest_lowercase_alphabet"] = [highest_lowercase_alphabet]

    return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(debug = True)