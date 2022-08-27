# KeyForecast
A web application to view your desired city's weather details at any moment. 

# Demo

https://user-images.githubusercontent.com/104474913/187048015-99ec43ac-16e1-44bc-a161-21eaf405477b.mov

# Technology 
Python and Django are used to develop the backend of this web application where POST requests are sent to the OpenWeatherMap API and weather data is retrieved. GET requests enable when the city name is typed and searched through the API data. HTML and CSS are used for the basic front end development and JSON loads in the data requested from the API. 

# Usage

If you would like to download my project, these are the steps (may vary a bit depending on your python version and if you are on Windows/Linux/Mac):
        <ol>
        <li>
          Open your terminal and navigate to the directory you wish to store the project and run the following command:
          ```
          git clone https://github.com/dshah1010/key-forecast.git
          ```
       </li>
       <li>
          Create a virtual environment and activate it using the following commands:
          ```
          python3 -m venv venv
          ```
          and
          ```
          source venv/bin/activate
          ```
       </li>
       <li>
          Once you've activated your virtual environment install your python packages by running:
          ```
          pip install -r requirements.txt
          ```
       </li>
       <li> 
          Migrate the project: 
          ```
          python3 manage.py migrate
          ```
       </li>
       <li> 
          Navigate to the directory "manage.py" is and type the following in the terminal to view the application: 
          ```
          python3 manage.py runserver
          ```
       </ol>
       
# What's Next?
In the future, I plan to upgrade the UI and include features such as being able to save certain city weather locations of your choice to view at any time. I can also make it more interactive by having the map of the world and when a particular area is clicked, the program knows the location and automatically displays the information retrieved from the API. 
