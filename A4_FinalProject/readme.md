# A4 Final Project Group 22
<p align="center">
William Nielsen - Sebastian Krogh Nielsen - Samuel Daniel Leinum - Patrick Dahlgreen Petersen
</p>
<p align="center">
s183578 - s183603 - s183580 - s183593
</p>


## Summary of the use case
According to BIM UseCase Booklet this tool is based on the Use Case 'Energy Analysis' with a forecast usage in the design phase. 
The goal of the tool is to contribute with an estimate of the ventilation demand in every zone of an building. This will help the building designer by automateing the calculations and to implement it early in the design phase. A full rundown of the use case can be read here: [A3: Use Case](https://github.com/s183578/41934-Advanced-BIM-Group-22/tree/main/A3_UseCase)

## Who is the tool for and how does it work
The tool can be used by both architects and engineers (building designers) who are involved in any design phase of a building project. The tool works by scanning the building and locating each and every room which is defined as a space and then the windows. First off it gathers information about the spaces, in this case: "name", "room number", "level" and "area". From the area the tool then calculates the minimum dimensioning ventilation requirement and writes all of the information into an excel sheet. Next up it gathers information about the windows in form of the "name", "level", "orientation", "height" and "width". The orientation and window area is used within the code to calculate the solar radiation comming in through each window. For every loop the information is written to the same excel just in another sheet. It is important to note that the tool only works with buildings modelled in the IFC format.

## Business and societal value
The intention of the project is to develop a tool for the early design stages. It is a big advantage to know as much as possible in the early phases, which is why the user can benefit of knowing about spaces and requirement of the ventilation system so it can be implemented and taken into account. It will greatly save time in the longer run to know an estimate of ventilation ducts, shafts and the AHU. Hopefully it will prevent too tight spaces for ducts, shafts etc.

The tool can lead to fewer urgent incidents and better space allocation, where money can be spent in other focus areas. Hopefully it can lead to better HVAC solutions that will reduce the energy usage and maintenance need, resulting in more sustainable solutions. And optimized space management which results in an overall better building.

## Requirements for the tool

###  Software and packages
An array of software and packages are needed in order to run the code. Most of it has been documented inside of the code, but here is a recap.
1. Python 3.7
2. ifcopenshell for Python 3.7
3. ifcopenshell.geom
4. xlsxwriter
5. os
6. numpy
7. Microsoft excel

### Files needed
The files needed for the project are all included inside of the repository. Just download it in its entirety and follow the steps in the guide section below.
1. Python code: "main.py".
2. Model file: "Duplex_A_20110907.ifc".
3. Empty folder called "output" in which the excel sheet will be written to.


### Guide in steps
To correctly execute the code and get the desired output, please follow along with the steps provided below:
1. Download the repository as a ZIP file and unpack it somewhere on your computer. For simplicity the example will be on the C drive "C:\".
2. Make sure you have python 3.7 and the required packages installed onto your computer.
3. Open up the command prompt (CMD) by either pressing Windows+R and type "cmd" into the popup box or in the search box on the toolbar search "cmd". To open in administator mode press Ctrl+Shift+Enter or right click "Run as administrator". A black screen should appear.
4. Here navigate to where you unpacked the code folder. For the example it would be done by typing: "cd..\..\code". The line should now say "C:\code>".
5. Now simply write "main.py" and after a couple of seconds, if successful the message "Excel sheet succesfully created! Check your output folder" should appear.
6. Navigate to your output folder and see an excel sheet has been created called "Ventilation and solar radiation.xlsx". Inside here all the extracted information has been written and as a consulting engineer you would now have a good overview of the ventilation rate and the solar radiation comming through the windows.


## Future work
The tool is still very unoptimized and a lot of features we wanted to include in the tool was out of the time scope. If we had more time to develop the tool we would like to have included an option for the user to choose which indoor environment class (IEQ) the building is in and then calculate the ventilation rate based on that. Right now it only shows for IEQ II. The next step would then be to calculate ventilation rate based on other dimensioning factors such as heat loads, where we then would use the solar radiation from the windows. Lastly it would be nice to have an interface attached to the tool so its more user friendly and easier to navigate.


## 2 Minute video
The video is too large to be uploaded onto the Github page. The video has been uploaded to Youtube click [here](https://www.youtube.com/watch?v=Rjm7t6r-z-k)
