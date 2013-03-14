// Constructors are a way to make objects with the keyword new. 
// The most basic constructor is the Object constructor, 
// which will make an object with no methods or properties.

// For more complicated objects we can make our own constructors 
// and put in whatever properties and methods we want. 



// Define a new method on line 8, calcPerimeter, 
// which calculates and returns the perimeter for a Rectangle in terms 
// of length and width. 

function Rectangle(length, width) {
  this.length = length;
  this.width = width;
  this.calcArea = function() {
      return this.length * this.width;
  };
  // put our perimeter function here!
  this.calcPerimeter = function() {
  	 return 2 * this.length + 2 * this.width;
  }
}

var rex = new Rectangle(7,3);
var area = rex.calcArea();
var perimeter = rex.calcPerimeter();