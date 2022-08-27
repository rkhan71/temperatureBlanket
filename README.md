# temperatureBlanket
A webpage that uses an API to get historical weather data and display it through different colors in a similar manner to a knitted temperature blanket.

I initially got this idea when I saw a TikTok of someone knitting a blanket using different colors of wool to represent the avergae temperature of each day over the course of a year. Apparently this is a common thing people do and it is called a Temperature Blanket. I thought it would be really cool to use an API to get data for the average daily temperature of anywhere in the world for decades. Then this data could be used to print temperature blankets on the screen, visually showing the change in temperature across seasons and even the change in the seasons over multiple years. 

At the time I was not aware of the cost involved in using APIs. Even though the data I want is available it is very expensive, so the web app cannot display as much information as I initially hoped it would. I am using Visual Crossing Weather API which gives me access to the average daily temperature for anywhere in the world. However, I can only access the records for 1000 days per day. 

Using the web app is very simple, a user simply submits a city and a date range through a form and then a temperature blanket is generated. The color key can be changed through a form that shows up with the temperature blanket as well. New colors can be inputted through any mode that is acceptable in CSS. The name of the city can be submitted in any form as the API is able to interpret it most of the time.

When the user submits the initial form an API request is generated and the data is put into an array in Python. Then I use Jinja to loop through the array and assign a class to a div with a height of 10px depending on the temperature in the array. The color of the div is decided by the class in the CSS stylesheet colors.css in the static folder. So to change the color key I use JavaScript to alter the style sheet. One issue with this is that the colors reset once the page is reloaded so a user can't have the colors they want for multiple different temperature blankets without repeatedly changing the colors. This is something I want to figure out. 

The design of the web app is still very basic as I have worked mostly on the back end. In all my other web apps I use CSS frameworks, but with this one, I want to try and use CSS "manually" and see what I can do. 
