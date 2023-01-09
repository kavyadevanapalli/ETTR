# This is a sample Python script.

from flask import Flask, request, jsonify, render_template


app = Flask(__name__)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

@app.route('/snow_ettr_more/',methods=['POST'])
def snow_ettr_more():
    print('@@@@@@@@@@@@@ Testing the code for SOAP API !@@@@@@@@@@@@@@@@@')
    print(request)
    args=request.get_json()
    print(args)
    case_number = args['queryResult']["parameters"]["any"]
    return {"fulfillmentText": "2 hrs"}

if __name__ == "__main__":
    #app.run(debug=True, host='0.0.0.0', port=5000)
    app.run(debug = True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
