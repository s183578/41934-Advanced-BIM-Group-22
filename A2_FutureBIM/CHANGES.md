CHANGES MADE:

For this assignment about FutureBIM we focused on linking the first assignment to this one in terms of being able to caluclate the ventilation rates required to uphold a proper indoor climate accordingly to thresholds from DS/EN16798. 
In the first assignment OpenBIM we used the IFC model alongside with BLENDER to get an insight of how we could approach the problem and it helped us to develop code that could extract the data needed. 
This is how we linked these two assignments together and what we focused on here was to further improve the code for future use and make it more visually available/pleasing by "hacking" the html code.
To run the results simply open up the index.html from the file folder path: HTML-Build-IFC-Converter-main\output\duplex\index.html (preferably with google chrome)

To achieve our goal we needed to make changes to the following four files:
 * HTMLBuild.py (inside of folder: HTML-Build-IFC-Converter-main)
 * html-build.css (inside of folder: HTML-Build-IFC-Converter-main\output\css)
 * index.html (inside of folder: HTML-Build-IFC-Converter-main\output\duplex)
 * html-build.js (inside of folder: HTML-Build-IFC-Converter-main\output\js)
  
The changes vary a lot with everything from small comestic changes to data extraction and to make it easier to identify where code has been changed/made documentation is provided and explained.
The changes in no particular order:

 1. Changed the color from being yellow to blue (line 4-27 in html-build.css)
 2. Added a HTML titel to the index (line 240-246 in html-build.css)
 3. Added a titel to the properties box in the bottom right (line 162-175 in html-build.css)
 4. Changed the general font. (Throughout html-build.css)
 5. In the HTMLBuild.py we added a loop for extracting the information in the bottom left box about spaces. (line 135-159 in HTMLBuild.py)
 6. Added table to display the extracted information from point 5. on the left half of the screen below the building (line 248-258 in html-build.css)
 7. Added longitude and latitude to the properties box (line 16-22 in html-build.js)
 8. Rounded off the elevation to one decimal (line 11-16 in index.html)
 9. Fixed sizes of boxes and allignment to be more symmetrical (line 32-45 in html-build.css)
 10. Changed text from "happy" to "Click on a floor to see the attributes" (line 26 in html-build.js)
 
Future work: 
If we had more time we wanted to implement code that would then take areas of the spaces and then calculate how much ventilation rate is needed to reach each of the the indoor environment classes from 1 to 4 from DS/EN16798
and display it on the html page. 
 