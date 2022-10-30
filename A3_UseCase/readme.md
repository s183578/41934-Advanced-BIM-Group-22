# A3 Use Case group 22

## 3A: Analyse use case
1. Goal: <br />
The goal of this use case is to give the architects and engineers a quick and easy overview of the ventilation needs in different rooms of the building.
2. Model Use (Bim Uses): <br />
This section is based on the "BIM UseCase booklet" source material page 2.
	* The use cases is cost estimation, phase planning, design coordination, Space manegement, Buidling System Analysis
	* The BIM uses is to quanitify and size of ventilation.
	* The use phases for the project would be in the planing stages.

## 3B: Propose a (design for a) tool / workflow
3. Process: <br />
The process of this use case has been modelled in a BPMN diagram. Please refer to the uploaded .svg file for this diagram.
5. description of the process: <br />
The tool / workflow works by calculating the required ventilation rate in each room based on the floor area. This works as according to DS/EN 16798 table B.6 it is possible to calculate an estimate of the ventilation need based on the floor area. There are however four different indoor classes and the ventilation rate is different according to the type of building/room, so for the code it should be implemented such that the user chooses beforehand what category and what type of building space needs to be calculated.


## 3C: Information exchange
5. Information Exchange: <br />
The information exchange is documented in the excel file: "Group22_Information_Exchange.xls". It should be noted that the some of thhe model element breakdown categories are marked in a red color, and this is meant as a  "nice to have but not nessecary". Only the IE tab has been filled out. 
7. IFC: <br />
From the information exchange sheet the following (main) elements were identified:
	* Floor construction
	* Exterior walls
	* Exterior windows
	* Exterior louvers and vents
	* Interior partition (interior walls)

The floor construction element in the Ifc format is the entity IfcSlab and this element is the primary focus point in the code as it is possible from the slabs to gather a majority of the information that is needed in order to calculate a ventilation rate. 

Exterior walls is collected from the Ifc file and the entity is called IfcWallStandardCase (or IfcWall). The walls are needed for the u-value and cardinal orientation (solar radiation).

Exterior windows is collected from the Ifc and entity is called IfcWindow. From the windows the needed information is: total u-value, g-value, size/area and cardinal orientation (solar radiation). 

Exterior louvers and vents are only needed if shading is used on the exterior windows and here they are not always taken from the Ifc files. It can be nessecary to get the shading coefficients according to methods from DS/EN 410.

For interior partition what is needed here are the interior wall elements from the Ifc file. Similarly to the exterior walls these are also called IfcWallStandardCase. The interior walls are mainly used to enclose the spaces and to get a volume of the rooms. They are assumed adiabatic meaning no u-value, heat transfer and such.


## 3D: Value What is the potential improvement offered by this tool?
7. Describe the business value: <br />
It brings a massive increase in value to any business that would use this. The focus of the project is to try develop on the early design stages. It's a very big advantance to know as much as you can in the early design phases so you can implement the information as early as possible. It's will greatly save time in the longer run that the ventilation shafts and AHU already have an easy and rough estimate.
9. Describe the societal value: <br />
It would save a lot of money, that could be used to plant trees. Hopefully it would make for more optimal HVAC solutions that would reduce the energy useage and maintenance. 


## 3E: Delivery
9. Your tool/workflow: <br />
It would make it easy to calculate the ventilation loads and to implement them in the early design fase.
11. Delivery: <br />
The tool will be made on iterations on an IFC model with all the needed data in it. We will start from top to acces the overall entities such as walls, windows, etc. Then we will try to pull out properties of the entities containing amount (volume, area, weight, etc.) and then material names.







