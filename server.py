from app import app


if __name__ == '__main__':
    app.config.from_object('app.config.development.DevelopmentConfig')
    app.run()
