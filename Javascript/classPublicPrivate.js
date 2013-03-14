// Make the grade value private with the getGPA stll showing the result

// INITIAL STATE
function StudentReport() {
    this.grade1 = 4;
    this.grade2 = 2;
    this.grade3 = 1;
    this.getGPA = function() {
        return (grade1 + grade2 + grade3) / 3;
    };
}

var myStudentReport = new StudentReport();

for(var x in myStudentReport) {
    if(typeof myStudentReport[x] !== "function") {
        console.log("Muahaha! "+myStudentReport[x]);
    }
}

console.log("Your overall GPA is "+myStudentReport.getGPA());



//  ANSWER - MAde the variable private and 
//		removed this frm the addition in the method
function StudentReport() {
    var grade1 = 4;
    var grade2 = 2;
    var grade3 = 1;
    this.getGPA = function() {
        return (grade1 + grade2 + grade3) / 3;
    };
}

var myStudentReport = new StudentReport();

for(var x in myStudentReport) {
    if(typeof myStudentReport[x] !== "function") {
        console.log("Muahaha! "+myStudentReport[x]);
    }
}

console.log("Your overall GPA is "+myStudentReport.getGPA());