from tests_basile import app

isDebug = __name__ == '__main__'
app.run(host='0.0.0.0', port=5000, debug=isDebug)
