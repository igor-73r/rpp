from db_init import *
import cherrypy


class MyWebService:
    def __init__(self, table=Total):
        self.table = table

    @cherrypy.expose
    def index(self):
        print(self.table)
        objects = get_data(self.table)

        template = ("""
            <html>
            <head>
                <title>lab6</title>
            </head>
            <body>
                <form method="post" action="/change_table">
                <input type="submit" name="table" value=Area>
                <input type="submit" name="table" value=Position>
                <input type="submit" name="table" value=PrecipitationType>
                <input type="submit" name="table" value=Precipitation>
                <input type="submit" name="table" value=Total>
                
                <h1>{0}</h1>
                <table border="1" width="600" style="border-collapse:collapse;">
                {1}
                </table>

            </body>
            </html>
        """).format(self.table.__name__, objects)
        return template

    @cherrypy.expose
    def change_table(self, table):
        match table:
            case "Area":
                self.table = Area
            case "Position":
                self.table = Position
            case "Precipitation":
                self.table = Precipitation
            case "PrecipitationType":
                self.table = PrecipitationType
            case "Total":
                self.table = Total
        raise cherrypy.HTTPRedirect('/')


def get_data(table):
    data = table.select().dicts()
    header = '<tr>{0}</tr>'.format(''.join(['<th>{0}</th>'.format(key) for key in data[0].keys()]))
    rows = ''.join(['<tr>{0}</tr>'.format(''.join(['<td>{0}</td>'.format(value) for value in row.values()])) for row in data])
    return '{0}{1}'.format(header, rows)


if __name__ == '__main__':
    cherrypy.quickstart(MyWebService())
