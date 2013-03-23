var nyc = {
    fullName: "New York City",
    mayor: "Michael Bloomberg",
    population: 8000000,
    boroughs: 5
};

// write your for-in loop here
for (var p in nyc)
{
	console.log(p);
}


// ******************************

var nyc = {
    fullName: "New York City",
    mayor: "Michael Bloomberg",
    population: 8000000,
    boroughs: 5
};

// write a for-in loop to print the value of nyc's properties
for(var pp in nyc)
{
	console.log(nyc[pp]);
}