// Run in JS console on the Career Center career fair event page's website
// For some reason this has a small bug with the duplicate consecutive Sandia entries; I just fix that manually
var companies = {};
companies.nameArr = document.getElementsByClassName('lst-cl_name');
companies.websiteArr = document.getElementsByClassName('lst-cl_website');
for (var i = 0; i < companies.nameArr.length; i++) {
	var name = companies.nameArr[i].firstChild.textContent;
	var link = companies.websiteArr[i].firstChild.href;
	console.log(name, link);
}

