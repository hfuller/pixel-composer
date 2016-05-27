$(document).ready(function() {

	$("#status").html("Working");

	function pullSettings() {
		console.log("Pulling settings");

		$.getJSON("/settings").done(function(data) {
			console.log(data);
			console.log("Setting mode to " + data.mode);
			$('#mode').val(data.mode);
			$('#length').val(data.length);
			$('#pattern-length').val(data.pattern_length);

			$("select,input").prop('disabled',false);
		}).fail(function() {
			$("select,input").prop('disabled',true);
			$("#status").html("Problem pulling settings. Try reloading the page?");
		});

	}

	$("select,input").change(function() {
		//visual
		if ( $('input#mode').val() == "repeat" ) {
			$("#pattern-label").fadeIn(250);
		} else {
			$("#pattern-label").fadeOut(250);
		}
		//state
		var data = {
			mode: $('select#mode').val(),
			pattern_length: $('input#pattern-length').val(),
			length: $('input#length').val()
		};
		console.log(data);
		$.post({
			url: "/settings",
			data: data
		}).always(function() {
			pullSettings();
		});
	});

	//startup
	pullSettings();
	$("#status").html("");

});
