from website import create_app

app = create_app()

# Will only run the app if you open it directly instead of oppening it
# every time we import the app ( Only runs the webserver if we run this file directly)
if __name__ == '__main__':
    app.run(debug=True)
