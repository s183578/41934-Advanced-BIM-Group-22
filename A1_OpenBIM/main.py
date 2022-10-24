import ifcopenshell
import xlsxwriter

#only run this if trying to run the code inside of blender
#import bpy
#from blenderbim.bim.ifc import IfcStore

#Defines the model to the ifc file. Please put this exact model in a folder called "model"
model = ifcopenshell.open('model/Duplex_A_20110907.ifc')
#model = IfcStore.get_file()

#Please make a folder called "output" in your code folder or else no excel sheet can be created 
workbook = xlsxwriter.Workbook('output/Property pullout.xlsx')

#Makes it able to make text bold inside of excel
bold = workbook.add_format({'bold': True})

#This is used to get find the Space type inside of the ifc file. Its getting used later on
spaces = model.by_type("IfcSpace")

#makes spreadsheet in excel. This uses the xlsxwriter package
def makeASheet(ifcType):
        sheet = workbook.add_worksheet(ifcType)
        #writes into a sheet. (row, coloum, data)
        sheet.write(0,0,'Name:',bold)
        sheet.write(0,1,'Number:',bold)
        sheet.write(0,2,'Area:',bold)
        row =1
        column =1
        for entity in model.by_type(ifcType):
            # this writes the data to the sheet
            # sheet.write(LongName is the actual name and Name is the number linked to the name)
            sheet.write(row,0,str(entity.LongName))
            sheet.write(row,column,str(entity.Name))  
            
            # this 'iterates' row so that each time we step down a row.
            # otherwise each new entry would overwrite the previous entry.
            row+=1  

        #Gathering information from the IFC file, in this case the area
        for space in spaces:
            space.Name
            ## get property sets attached to beams through IsDefinedBy"
            for definition in space.IsDefinedBy:
                
                ## To support IFC2X3, we need to filter our results.
                if definition.is_a('IfcRelDefinesByProperties'):
                    property_set = definition.RelatingPropertyDefinition
                    
                    
                    ## Sort by the name of the propertySet
                    if property_set.Name == "PSet_Revit_Dimensions":
                       for property in property_set.HasProperties:
                            
                            #print(property)
                            ## sort b the name of the property
                            if property.Name == "Area":
                                #For now this is very hardcoded and optimization will be made later on. 
                                area = property.NominalValue.wrappedValue
                                sheet.write(row-21,column+1,area)
                                row+=1

#end of the loop. Makes a sheet called IfcSpace in which all the information will be stored.
makeASheet('IfcSpace')


#This next section is a progress to be continued on. For now it calculates the beams but we might convert it into walls very soon.
total_beam_length = 0
for entity in model.by_type("IfcBeam"):
    #we need to get the attributes
   for relDefinesByProperties in entity.IsDefinedBy:
        for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
            #and then get the attribute we are looking for
            if prop.Name == 'Length':
                #add the length to the total length
                total_beam_length += prop.NominalValue.wrappedValue
                total_beam_length = round(total_beam_length,2)
 
#follows the same structure as above when writing sheets into excel.
def makeASheet(ifcType):
        sheet = workbook.add_worksheet(ifcType)
        # define which row you want to start writing at.
        sheet.write(0,0,'Name:',bold)
        sheet.write(0,1,'Quantity:',bold)
        row =1
        column =1
        for entity in model.by_type(ifcType):
            # this writes the data to the sheet
            # sheet.write(row, column, data)
            sheet.write(row,0,str(entity.Name))
            sheet.write(row,column,str(total_beam_length)+" meter")
            # this 'iterates' row so that each time we step down a row.
            # otherwise each new entry would overwrite the previous entry.
            row+=1

#end of the loop. Makes a sheet called IfcBeam in which all the information will be stored.    
makeASheet('IfcBeam')
# it is important to close the workbook afterwards
workbook.close()

#When this print message gets shown to the console an excel file has succesfully been written.
print("Excel sheet succesfully created! Check your folder")

