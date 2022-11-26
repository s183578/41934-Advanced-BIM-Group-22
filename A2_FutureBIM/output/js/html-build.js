/* written by Tim McGinley 2022 */

// ok in here we need to include a lot of stuff.
// we need a menu... where would this fit?
// we need to start (over)loading stuff into the DOM.
// we need to split the screen into section and plan and KPIs and info - where should this go?


function main() {
	
	// calculate the floors
	const floors = document.getElementsByTagName("floor-");
	let num_floors = floors.length;
	console.log(num_floors);
	
	// add data to the properties box // added more boxes for the extra information we want to display
	$('props-').prepend('Number of floors: '+num_floors);
	$('props-').prepend('Site elevation: '+$('site-').attr('elev')+'<br>');
	$('props-').prepend('Site latitude: '+$('site-').attr('lat')+'<br>');
	$('props-').prepend('<h4>Properties</h4>Site longitude: '+$('site-').attr('long')+'<br>');
	
	$('h1').prepend($('project-').attr('name')+'<br>');
	
	
	// load the plan so we can edit it and changed text from happy
	plan('Click on a floor to see the attributes');
	
	// The .each() method is unnecessary here:
	$( 'floor-' ).each(function() {
	console.log($(this)[0].innerHTML);
		$( this ).on("click", function(){
			//$('plan-').css("background-color","black");
															// add more data we extract
			changePlan('Floor name: ' + $(this).attr('name') + '<br>Level: ' + $(this).attr('level') + '<br>Elevation: ' + $(this).attr('elev'));
			//$( this ).innerHTML
		});
	});
	
	
}

function plan(text) {
jQuery('<div>', {
    id: 'plan',
    class: 'plan',
    title: 'click a floor to see the plan',
	html:text
}).appendTo('plan-');  
	
}

function changePlan(text) {
	$('#plan').html(text);
}





// <project-> - title etc.... | <site-> - also menu? site specific data?
// ---------------------------------------------------------------------
// <building-> - name of the building? this then needs to split in two...
// could also be more views and show a 3d? but maybe left is consistent
// ---------------------------------------------------------------------
// #section                   |               #plan
// this shows the floors      |      this shows a floor in plan         |
// in section                 |                 #plan                   |
//    <floor...->              -----------------------------------------
//                            |                 <properties->           |
// ---------------------------------------------------------------------
