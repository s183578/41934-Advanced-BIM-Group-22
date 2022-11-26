''' written by Tim McGinley 2022 '''

import ifcopenshell
import os.path
import time

def modelLoader(name):

    ''' 
        load the IFC file 
    '''
    
    model_url = "model/"+name+".ifc"
    start_time = time.time()

    if (os.path.exists(model_url)):
        model = ifcopenshell.open(model_url)
        print("\n\tFile    : {}.ifc".format(name))
        print("\tLoad    : {:.2f}s".format(float(time.time() - start_time)))
        
        start_time = time.time()
        writeHTML(model,name)
        print("\tConvert : {:.4f}s".format(float(time.time() - start_time)))
        
    else:
        print("\nERROR: please check your model folder : " +model_url+" does not exist")

def writeHTML(model,name):

    ''' 
        write the HTML entities 
    '''
    
    # parent directory - put in setting file?
    parent_dir = "output/"
    # create an HTML file to write to
    if (os.path.exists("output/"+name))==False:
        path = os.path.join(parent_dir, name)
        os.mkdir(path)
    
    f_loc="output/"+name+"/index.html"
    f = open(f_loc, "w")
    cont=""
    
    # ---- START OF STANDARD HTML
    cont+=0*"\t"+"<html>\n"
    # ---- ADD HEAD
    cont+=1*"\t"+"<head>\n"
    # ---- ADD HTMLBUILD CSS - COULD ADD OTHERS HERE :)
    cont+=2*"\t"+"<link rel='stylesheet' href='../css/html-build.css'></link>\n"
    # ---- ADD HTMLBUILD CSS - COULD ADD OTHERS HERE :)
    cont+=2*"\t"+"<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css' integrity='sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu' crossorigin='anonymous'>"
    # ---- ADD HTMLBUILD JS - COULD ADD OTHERS HERE :)
    cont+=2*"\t"+"<script src='../js/html-build.js'></script>\n"
    # ---- JQUERY - IT WOULD BE CRAZY NOT TO
    cont+=2*"\t"+"<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.js'></script>\n"
    # ---- CLOSE HEAD
    cont+=1*"\t"+"</head>\n"
    # ---- ADD BODY
    cont+=1*"\t"+"<body onload=\"main()\">\n"  
    # ---- ADD TITEL
    cont+=1*"\t"+"<h1 id='projectTitle'></h1>"
    
    # ---- ADD CUSTOM HTML FOR THE BUILDING HERE
    cont+=writeCustomHTML(model)
    
    # ---- CLOSE BODY AND HTML ENTITIES
    cont+=1*"\t"+"</body>\n"   
    cont+=0*"\t"+"</html>\n"

    # ---- WRITE IT OUT
    f.write(cont)
    f.close()

    # ---- TELL EVERYONE ABOUT IT
    print("\tSave    : "+f_loc)

def writeCustomHTML(model):

    ''' 
        write the custom HTML entities 
    '''
    
    custom=""
    site_elev = 0 # variable for to store the elevation of the site
    
    # ---- DEFINE THE MODEL
    
    custom+=2*"\t"+"<model->\n"
    
    # ---- ADD PROJECT CUSTOM ENTITY
    project = model.by_type('IfcProject')[0]
    custom+=3*"\t"+"<project- name=\"{d}\">\n".format(d=project.LongName) # ---- Removed 8?
    
    # it looks like it would make sense to use the DOM here and append stuff to it...
    
   
        
        
    
    
    
    
    # ---- ADD SITE CUSTOM ENTITY
    site = model.by_type('IfcSite')[0]
    site_elev = site.RefElevation
    custom+=4*"\t"+"<site- lat=\"{}\" long=\"{}\" elev=\"{}\">\n".format(site.RefLatitude,site.RefLongitude,site_elev )

    # ---- ADD BUILDING CUSTOM ENTITY
    custom+=5*"\t"+"<building->\n"
    
   
    
    # ---- ADD FLOOR CUSTOM ENTITIES
    floors = model.by_type('IfcBuildingStorey')
    floors.sort(key=lambda x: x.Elevation, reverse=True)
   
    
    # ---- CLASSIFY THE FLOORS AS LOWER, GROUND OR UPPER AND WRITE TO CUSTOM ENTITIES
    custom+= classifyFloors(floors,site_elev)
    
   
    
    
    # ---- CLOSE BUILDING
    custom+=5*"\t"+"</building->\n"
    
    
    
    # ---- CLOSE SITE AND PROJECT
    custom+=4*"\t"+"</site->\n"
    custom+=3*"\t"+"</project->\n"
      # ---- ADD SPACE CUSTOM ENTITY
    
#---------------------------------------------------------------------------------------------------------------------------------------------------#    
    # HERE GROUP 22 MADE OWN CODE TO GET THE LEVEL, AREA AND SPACEE LONGNAME OF SPACES IN THE BUILDING
    custom+=4*"\t"+"<spaces-> <h4>Spaces</h4> <table><th>Space</th><th>Level</th><th>Area</th>\n"
    spaces = model.by_type('IfcSpace')
    for space in spaces: # ---- FOR EVERY SPACE, GIVE THEM NEW NAMES
        space_LongName = space.LongName
        space_name = space.Name
        for definition in space.IsDefinedBy: # ---- FIND THE PROPERTIES FOR EACH SPACES
            if definition.is_a('IfcRelDefinesByProperties'):
                property_set = definition.RelatingPropertyDefinition
                if property_set.Name == "PSet_Revit_Dimensions": # ---- IF THE PROPERTY IS DIMENSIONS
                    for property in property_set.HasProperties:
                        if property.Name == "Area":  # ---- SAVE THE AREA
                            space_area = property.NominalValue.wrappedValue
                if property_set.Name == "PSet_Revit_Constraints": # ---- IF THE PROPERTY IS CONSTRAINTS
                    for property in property_set.HasProperties:
                        if property.Name == "Level": # ---- SAVE LEVEL OF THE SPACE
                            space_level = property.NominalValue.wrappedValue
        
        # ---- SAVE AS AN ARRAY AND SAVES INTO THE "CUSTOM STRING" TO BE ABLE TO DISPLAY THE DATA INSIDE THE TABLE OF THE FRONT PAGE
        #custom+=5*"\t"+"<space- longName=\'{}\' name=\'{}\' area=\'{}\' level=\'{}\'>{}, {}, Area: {}m<sup>2</sup> <br>\n".format(space_LongName,space_name,space_area,space_level,space_LongName, space_level, round(float(space_area),1))
        custom+=5*"\t"+"<tr><td>{}</td><td>{}</td><td>{}m<sup>2</sup></td></tr>\n".format(space_LongName,space_level,round(float(space_area),1))
        #custom+=5*"\t"+"</space->\n"
    custom+=4*"\t"+"</table></spaces->\n"
#---------------------------------------------------------------------------------------------------------------------------------------------------#  


    # ---- END OF MODEL ENTITY
    custom+=2*"\t"+"</model->\n"
    
    # ---- ADD VIEWS.
    custom+=2*"\t"+"<view->\n"
    
    # ---- ADD PLAN.
    custom+=3*"\t"+"<plan-></plan->\n"
    
    # ---- ADD PROPERTIES ETC.
    custom+=3*"\t"+"<props-></props->\n"
    
    # ---- CLOSE VIEWS
    custom+=2*"\t"+"</view->\n"
    
    # ---- RETURN THE CUSTOM HTML
    return custom

def classifyFloors(floors,site_elev):

    '''
    another way after arranging them would be to split them into above and below ground floor sets.
    '''
    
    floor_entities = ''
    
    # these are interesting and probably should be output somwhere - maybe to the building data?
    lower_floors = sum(f.Elevation < 0.1 for f in floors)
    level = len(floors)-lower_floors
    
    for floor in floors:
        # check if floor is lower than elevation...
        type = "floor_upper"
        if ( site_elev-.1 <= floor.Elevation <= site_elev+.1):
            type = "floor_ground"
        elif (site_elev < floor.Elevation):
            type = "floor_upper"
        else:
            type = "floor_lower"
           
        # THE SPAN STUFF SHOULD BE DEALT WITH IN JS...
        
        floor_entities+=6*"\t"+"<floor- class=\""+type+"\" name='{}'  level='{}' elev=\"{}\" >{}<span class=\"floor_stats\">{}</span> </floor->\n".format(floor.Name, level, floor.Elevation,floor.Name, round(float(floor.Elevation),3))     
        level-=1
        if (type == "floor_ground"):
            floor_entities+=6*"\t"+"<ground-></ground->\n"
            
    return floor_entities
