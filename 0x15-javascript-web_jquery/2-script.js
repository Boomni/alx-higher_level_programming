const header = document.querySelector("header");
const red_header = document.querySelector("div#red_header");

red_header.addEventListener("click", updateHeader);

function updateHeader () {
	header.style.color = "#FF0000";
}
