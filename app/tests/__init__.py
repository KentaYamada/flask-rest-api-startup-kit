from app import app


# set testing configuration
app.config.from_object('app.config.testing.TestingConfig')

# create test client
test_client = app.test_client()
