# A3 Use Case group 22

### 3A: Analyse use case
1. Goal: Goal of the tool / workflow in one sentence. i.e. to support the user to calculate the total total cost of the project.
 	To give the architects and engineer a quick and easy overview of the ventilation needs.	
2. Model Use (Bim Uses): Please refer initially to the Mapping BIM uses, use cases and processes section in this document.
	The use cases is cost estimation, phase planning, design coordination, Space manegement, Buidling System Analysis
	The BIM uses is to quanitify and size of ventilation.
	The use phases for the project would be in the planing stages.

### 3B: Propose a (design for a) tool / workflow
3. Process: model the process diagram from your use case in BPMN.io please remember to save the .bpmn file and you can save a .svg file that you can insert into your report. 
	Refer to the BPMN file
5. description of the process of your tool / workflow.
	The tool / workflow works by calculating the required airexchange in each room based on the floor area. There are different indoor classes, so this 	  calculation, needs to be performed several times, pr. room.


### 3C: Information exchange
5. Information Exchange: Fill out the excel template with the information for your planned tool / workflow. For this you will need access to the excel, and the Dikon document to help you specify the LOD (LOR,LOG,LOI) for each element you need for you tool / workflow.
	@William
6. IFC: Describe the IFC entities and properties for each of the elements you identified in your information exchange. Describe the data that you need to:
	* Find in the IFC
	* Find in an external sources i.e. BR18
	* Based on assumptions (useful when we don't have the 'real' data that we need for our tool)
	For now, we only need the floor area. IfcSlab is the one we are looking into for now. We need some assumptions for the room height for now, but in the future the room height might be taken from the zone.

### 3D: Value What is the potential improvement offered by this tool?
This is the common question when developing tools and processes as an [intrapreneur]( https://hbr.org/2020/03/why-you-should-become-an-intrapreneur) in a company. You should consider the business and societal value of this tool – does it save time to the company, does it make employees happier / more productive? Could it reduce material use in society?

7. Describe the business value (How does it create value for your business / employer)
	It brings a massive value boost to any business that would use this. The focus of the project is to try develop on the early design stages. It's a very big advantance to know as much as you can in the early design fase so you can impleed the information as early as possible. It's will greatly save time in the longer run that the ventilation shafts and AHU already have a easy and rough gu-esstimate.
8. Describe the societal value (How does it make the world better)
	It would save a lot of money, that could be used to plan trees. Hopefully it would make for more optimal HVAC solutions 

* N.B. If it doesn't do either of these things (ideally it should do both - don't do it!!)


### 3E: Delivery
In this assignment we will focus on the input data that you need for your final tool / workflow. 
9. Your tool/workflow: Description of how your tool / workflow would solve the use case
	It would make it easy to calculate the ventilation loads and to implement them in the early design fase.
10. Delivery: Description of how you would make the tool / workflow - what steps would you go through?
	We need to figure out how to make calculations in the code, and display them with the input.
