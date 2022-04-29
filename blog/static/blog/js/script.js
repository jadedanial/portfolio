function showMenu(){

	document.getElementById("menuitems").classList.toggle("showmenu");

}

function loadFunctions(){

	//Start Function - Word Typing and Deleting Effects//
	
	const words = ["Programmer", "Web Developer", "Human"];
	let i = 0;
	let timer;

	function typingEffect() {

		let word = words[i].split("");

		var loopTyping = function() {

			if (word.length > 0) {

				document.getElementById('word').innerHTML += word.shift();

			} else {

				deletingEffect();
				return false;

			};

			timer = setTimeout(loopTyping, 200);

		};

		loopTyping();

	};

	function deletingEffect() {

		let word = words[i].split("");

		var loopDeleting = function() {

			if (word.length > 0) {

				word.pop();
				document.getElementById('word').innerHTML = word.join("");

			} else {

				if (words.length > (i + 1)) {

					i++;

				} else {

					i = 0;

				};

				typingEffect();
				return false;

			};

			timer = setTimeout(loopDeleting, 50);

		};

		loopDeleting();

	};

	typingEffect();

	//End Function - Word Typing and Deleting Effects//

	//Start Function - Hide Hamburger Menu//
	
	window.onscroll = function() {onScroll()};

	window.onclick = function(event){

		if(!event.target.matches("#menuimg")){

			var dropdowns = document.getElementsByClassName("menucontent");
			var i;

			for(i = 0; i < dropdowns.length; i++){

				var openDropdown = dropdowns[i];

				if(openDropdown.classList.contains("showmenu")){

					openDropdown.classList.remove("showmenu");

				}

			}

		}
				
	}
	
	//End Function - Hide Hamburger Menu//

	//Start Function - Hide Navigation Menu When Scroll Up//

	var prevScrollpos = window.pageYOffset;

	window.onscroll = function(){

		var currentScrollPos = window.pageYOffset;

		if(prevScrollpos > currentScrollPos){

			document.getElementById("navigation").style.top = "0";

		}else{

			document.getElementById("navigation").style.top = "-90px";

		}

		prevScrollpos = currentScrollPos;

	}

	//End Function - Hide Navigation Menu When Scroll Up//

}

//Start Function - Scroll Reveal Effects//

function reveal(){
	
	var reveals = document.querySelectorAll(".reveal");
  
	for(var i = 0; i < reveals.length; i++){

	  	var windowHeight = window.innerHeight;
	  	var elementTop = reveals[i].getBoundingClientRect().top;
	  	var elementVisible = 50;
  
		if(elementTop < windowHeight - elementVisible){

			reveals[i].classList.add("active");

	  	}else{

			reveals[i].classList.remove("active");

		}

	}

}
  
window.addEventListener("scroll", reveal);

//End Function - Scroll Reveal Effects//