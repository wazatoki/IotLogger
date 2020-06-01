from infrastructure import flaskSetup
import repositories
import gateway

app = flaskSetup.app

if __name__ == '__main__':
    app.run(debug=True)