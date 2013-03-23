// the original Animal class and sayName method
function Animal(name, numLegs) {
    this.name = name;
    this.numLegs = numLegs;
}
Animal.prototype.sayName = function() {
    console.log("Hi my name is "+this.name);
};

// define a Penguin class
function Penguin(name) {
	this.name = name;
	this.numLegs = 2;
	this.sayName = function() {
		console.log("Hi my name is "+this.name);
	};
}

// set its prototype to be a new instance of Animal
Penguin.prototype = new Animal();


//////////////////////

function Penguin(name) {
    this.name = name;
    this.numLegs = 2;
}

// create your Emperor class here and make it inherit from Penguin
function Emperor(name) {
	this.name = name;
}
Emperor.prototype = new Penguin();

// create an "emperor" object and print the number of legs it has
var emperor = new Emperor("Steo");
console.log(emperor.numLegs);


//////////////////////////////

// original classes
function Animal(name, numLegs) {
    this.name = name;
    this.numLegs = numLegs;
    this.isAlive = true;
}
function Penguin(name) {
    this.name = name;
    this.numLegs = 2;
}
function Emperor(name) {
    this.name = name;
    this.saying = "Waddle waddle";
}

// set up the prototype chain
Penguin.prototype = new Animal();
Emperor.prototype = new Penguin();

var myEmperor = new Emperor("Jules");

console.log(myEmperor.saying); // should print "Waddle waddle"
console.log(myEmperor.numLegs); // should print 2
console.log(myEmperor.isAlive); // should print true