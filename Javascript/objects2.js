var friends = {};
friends.bill = {
  firstName: "Bill",
  lastName: "Gates",
  number: "(206) 555-5555",
  address: ['One Microsoft Way','Redmond','WA','98052']
};
friends.steve = {
  firstName: "Steve",
  lastName: "Jobs",
  number: "(408) 555-5555",
  address: ['1 Infinite Loop','Cupertino','CA','95014']
};

var search = function(name) {
	for (var f in friends) {
		if(f["name"] === name) {
			console.log(f["number"]);
			return f;
		}
	}
}

var list = function(aList) {
	for(var f in aList) {
		console.log f["name"];
	}	
}