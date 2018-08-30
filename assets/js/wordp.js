
		function show2() {
		$(document).ready(function(){
var isHidden = $('#mmi').is(':hidden');
if(isHidden) {
var person = prompt("Please enter password", "");
if (person == 'becomp') {
$('#myDropdown').show();
$('#myDropdown').data('clicked',true);
}
}
});
		}
		
$('body').click(function(evt){
		var isHidden = $('#mmi').is(':hidden'); 
		if(!isHidden) {
			if(evt.target.id == '#mmi0' || evt.target.id == '#mmi' || evt.target.id == '#mmi2' || evt.target.id == '#mmi3' || evt.target.id == '#mmi4' || evt.target.id == '#mmi5' || evt.target.id == '#mmi6' || evt.target.id == 'clicky') {
	   
			}
			else {
					$('#myDropdown').hide();
			}
		}

});
