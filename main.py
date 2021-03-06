#
from flask import Flask, url_for
from flask_restx import Api
from currentDateTime import currentDateTimeNamespace as nsdt
from timezones import timezonesNamespace as nstz
from calendarFromCurrentAPI import CalendarNamespace as cc

#
app = Flask(__name__)

api = Api(
    title='DateTimeAPI',
    version='1.0',
    description='...'
)

#
api.add_namespace(nsdt)
api.add_namespace(nstz)
api.add_namespace(cc)

#
api.init_app(app)

#
if __name__ == '__main__':
    
    #
    app.run()