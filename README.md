                                                            ABOUT PROJECT

The project is implemented in Django framework (using DRF). The reason for chosing Django were as follows.

# The task was to simply create 3 API's and Django provides a very cleand and simple way to create API's quickly and efficiently.

# The data in CSV seems to be information about railways systems. This might mean that scalability might required in the future as well. One of the other advantages with Django is that it provides good scalability.

As per my knowledge base, Second option after Django was Phoenix Framework (Used with Elixir) but elixir is primarilty used to make Fault tolerant and concurrent systems and that did not seemed to be the requirements of the task at that time.

                                                            ASSUMPTIONS

As of now, there is no User model in the projet and hence there is no authentication mechanism.So, everyone is allowed to make access our API's. Adding a security mechanims should not be a problem though.

                                                        STEPS TO RUN PROJECT.

# Please download python 3.7.9 from here https://www.python.org/downloads/release/python-379/

# Go to the root dir of the project (where the requirements.txt file is present) and run this command pip install -r requirements.txt. This will install all the required dependencies that this project requires.

# python manage.py makemigrations

# python manage.py migrate

# python manage.py runserver

                                                        API'S

The project mainly consists of 4 API's which are as follows

# rail_info/csv/import/ => Used to import records in the RainInfo model from the csv which should have a similar structure as the one which was shared.

# getall/ => Used to get all the RailInfo records from the table. Returns a list of JSON

# search?station=abc => Used to search records where station = "abc". Returns a list of JSON

# distance?from=a&to=b => Used to return a distance between 2 stations. Returns an integer value.

To get a better idea of API's please refer to the postman collection added in the root directory of the project.
