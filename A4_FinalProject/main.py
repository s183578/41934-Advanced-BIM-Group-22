#ONLY TESTED WITH PYTHON 3.7
#ONLY TESTED WITH IFCOPENSHELL FOR PYTHON 3.7
#Please operate in Comand Prompt

#https://pypi.org/project/install-ifcopenshell-python/0.1.0/
#Really important to have ifcopenshell or else it is not possible to work with the IFC formats.
import ifcopenshell
#.geom includes a library that helps when working with geometry
import ifcopenshell.geom
from ifcopenshell import geom
#pip install XlsxWriter. XlsxWriter is the package responsible to create and handle excel
import xlsxwriter
#os is used to handle local paths
import os
#pip install numpy. Numpy is needed in order to work with arrays, matrixes and vectors.
import numpy as np



#only run this if trying to run the code inside of blender
#------------------------------------------------------------#
#import bpy
#from blenderbim.bim.ifc import IfcStore
#model = IfcStore.get_file()
#------------------------------------------------------------#


#Defines the model to the desired ifc file. Please put the exact model in the folder called "model"
model = ifcopenshell.open('model/Duplex_A_20110907.ifc')


#Please make a folder called "output" in the folder or else no excel sheet can be created 
workbook = xlsxwriter.Workbook('output/Ventilation and solar radiation.xlsx')


#Makes it able to make text bold inside of excel
bold = workbook.add_format({'bold': True})


#This is used to get find the types inside of the ifc file. Its getting used later on
spaces = model.by_type("IfcSpace")
windows = model.by_type("IfcWindow")



#makes spreadsheet in excel. This uses the xlsxwriter package
def makeASheet(ifcType):
        sheet = workbook.add_worksheet('Spaces')
        #writes into a sheet. (row, coloum, data)
        sheet.write(0,0,'Name:',bold)
        sheet.write(0,1,'Number:',bold)
        sheet.write(0,2,'Level:',bold)
        sheet.write(0,3,'Area [m2]:',bold)
        sheet.write(0,4,'IEQ Class:',bold)
        sheet.write(0,5,'Ventilation rate [l/s]:',bold)
        
        #fresh start for the upcomming code, working as a reset
        row =1
        column =1
        for entity in model.by_type(ifcType):
            #this writes the data to the sheet
            #sheet.write(LongName is the actual name and Name is the number linked to the name)
            #float is used so excel knows is a number and not text
            sheet.write(row,0,str(entity.LongName))
            sheet.write(row,column,str(entity.Name))  
            sheet.write(row,column+3,float(2)) 
            #this 'iterates' row so that each time we step down a row.
            #otherwise each new entry would overwrite the previous entry.
            row+=1  

        #reseting the row and column for the upcomming code
        row =1
        column =1
        
        #Gathering information from the IFC file, in this case the what is within spaces
        for space in spaces:
            for definition in space.IsDefinedBy:
                
                ## To support IFC2X3, we need to filter our results.
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                    
                    
                    #Sort by the name of the propertySet and search for the area within the spaces. This loops until all spaces are found.
                    if property_set.Name == "PSet_Revit_Dimensions":
                       for property in property_set.HasProperties:
                            if property.Name == "Area":
                                #finds the value and rounds it to one decimal
                                area = property.NominalValue.wrappedValue
                                area = round(area,1)
                                sheet.write(row,column+2,area)
                                #1.4 is the ventilation rate according to DS 16798 table B.6
                                sheet.write(row,column+4,area*1.4)
                                row+=1

                    #sort by the name of the property
                    if property_set.Name == "PSet_Revit_Constraints":
                        for property in property_set.HasProperties:
                            if property.Name == "Level":
                                space_level = property.NominalValue.wrappedValue
                                sheet.write(row,column+1,space_level)
                                
#end of the loop. Makes a sheet called IfcSpace in which all the information will be stored and showcased in the excel sheet.
makeASheet('IfcSpace')


#makes an empty list and then fills it with the IfcWindow data inside of the ifcmodel
productList = []
for product in model.by_type("IfcWindow"):
    productList.append(product.is_a())
productList = list(set(productList))
productList.sort()

#Functions To define the matrix placement of the window objects.
def a2p(o,z,x):
    y = np.cross(z, x) 
    r = np.eye(4) 
    r[:-1,:-1] = x,y,z 
    r[-1,:-1] = o 
    return r.T
    
def axis2placement(plc): 
    z = np.array(plc.Axis.DirectionRatios if plc.Axis else (0,0,1)) 
    x = np.array(plc.RefDirection.DirectionRatios if plc.RefDirection else (1,0,0)) 
    o = plc.Location.Coordinates 
    return a2p(o,z,x) 
    
def local_placement(plc):
    if plc.PlacementRelTo is None: 
        parent = np.eye(4)
    else:
        parent = local_placement(plc.PlacementRelTo)
    return np.dot(parent, axis2placement(plc.RelativePlacement))


#now makes a new sheet as previously.
def makeASheet(ifcType):
        sheet = workbook.add_worksheet("Windows")
        sheet.write(0,0,'Name:',bold)
        sheet.write(0,1,'Level:',bold)
        sheet.write(0,2,'Orientation:',bold)
        sheet.write(0,3,'Height[m]:',bold)
        sheet.write(0,4,'Width[m]:',bold)
        sheet.write(0,5,'Area [m2]:',bold)
        sheet.write(0,6,'Solar radiation [W]:',bold)
        arealist = []
        row =1
        column =1
        
        #loops the code and writes all the entity names one row below each other
        for entity in model.by_type(ifcType):
            sheet.write(row,0,str(entity.Name))
            row+=1
       
        #reseting row and coloumns for the upcomming data   
        row =1
        column =1
        
        
        #Gathering information from the IFC file, in this case the windows
        for window in windows:
            #get property sets attached to windows through IsDefinedBy"
            for definition in window.IsDefinedBy:
                
                #To support IFC2X3, we need to filter our results.
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                    
                    
                    #Sort by the name of the propertySet and gets the height of windows and writes it to the sheet
                    if property_set.Name == "PSet_Revit_Type_Dimensions":
                       for property in property_set.HasProperties:
                            if property.Name == "Height":
                                height = property.NominalValue.wrappedValue
                                height = round(height,1)
                                sheet.write(row,column+2,height)
                                
                    #Sort by the name of the propertySet and gets the width of windows, calculate the area and write it to the sheet
                    if property_set.Name == "PSet_Revit_Type_Dimensions":
                        for property in property_set.HasProperties:
                            if property.Name == "Width":
                                width = property.NominalValue.wrappedValue
                                width = round(height,1)
                                sheet.write(row,column+3,width)
                                area = width*height
                                arealist.append(area)
                                sheet.write(row,column+4,area)
                                row+=1
                                
                    #Sort by the name of the propertySet and gets the level of windows and writes it to the sheet          
                    if property_set.Name == "PSet_Revit_Constraints":
                        for property in property_set.HasProperties:
                            if property.Name == "Level":
                                window_level = property.NominalValue.wrappedValue
                                sheet.write(row,column,window_level)
                         
                        #makes a list that is getting used later on that stores the orientation of the windows.
                        for product in productList:
                            if product in productList:
                                orientationlist = []
                                i=1
                                
                                #loops for every window and get its placement in vector form. It is then transposed.
                                for entity in model.by_type(product):
                                    m = local_placement(entity.ObjectPlacement)
                                    entity_matrix = np.matrix([
                                        [m[0][0], m[1][0], m[2][0], 0],
                                        [m[0][1], m[1][1], m[2][1], 0],
                                        [m[0][2], m[1][2], m[2][2], 0],
                                        [m[0][3], m[1][3], m[2][3], 1]])
                                    entity_matrix.transpose()
                                    
                                    #if-else statement is used to correspond the vectors into orientations and write them to the sheet
                                    if m[0][0] > 0:
                                        Orientation = "North"
                                        orientationlist.append("North")
                                    elif m[0][0] < 0:
                                        Orientation = "South"
                                        orientationlist.append("South")
                                    elif m[1][0] > 0:
                                        Orientation = "West"
                                        orientationlist.append("West")
                                    else:
                                        Orientation = "East"
                                        orientationlist.append("East")
                                    sheet.write(i,column+1,str(Orientation)) 
                                    i+=1
                                    
        #we take the length of the area list and loops it for all of the orientations. The solar radiation factor is then multiplied on.
        for i in range(len(arealist)):
            if orientationlist[i] == "North":
                solarirradiance = round(arealist[i]*175,0)
            elif orientationlist[i] == "South":
                solarirradiance = round(arealist[i]*790,0)
            else:
                solarirradiance = round(arealist[i]*710,0)
            sheet.write(i+1,column+5,float(solarirradiance)) 
          
makeASheet('IfcWindow')

# it is important to close the workbook afterwards
workbook.close()

#When this print message gets shown to the console an excel file has succesfully been written.
print("Excel sheet succesfully created! Check your output folder")
