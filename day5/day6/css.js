var selectedRow = null;
function onFormSubmit() {
var formData = readFormData();
if(isValid()){
    if (selectedRow == null) {
    insertNewRecord(formData);
    alert("Your details are saved Sucessfully........");
  }
}
}

function FacultyInformationForm() {
  var formData = {};
  formData["Faculty Name"] = document.getElementById("Faculty Name").value;
  formData["Training Attended"] = document.getElementById("Training Attended").value;
  formData["Overall Rating"] = document.getElementById("Overall Rating").value;
   formData["Topics Covered"] = document.getElementById("Topics Covered").value;
  return formData;
}
function resetForm() {
  document.getElementById("Faculty Name").value = "";
  document.getElementById("Training Attended").value = "";
  document.getElementById("Overall Rating").value = "";
  selectedRow = null;
}
function insertNewRecord(data) {
  var table = document
    .getElementById("Faculty")
    .getElementsByTagName("tbody")[0];
  var newRow = table.insertRow(table.length);
  cell1 = newRow.insertCell(0);
  cell1.innerHTML = data.FacultyName;
  cell2 = newRow.insertCell(1);
  cell2.innerHTML = data.TrainingAttended;
  cell3 = newRow.insertCell(2);
  cell3.innerHTML = data.OverallRating;
  cell4 =newRow.insertCell(3)
  cell4.innerHTML = `<a onClick="onEdit(this)">Update</a><a onClick="onDelete(this)">Delete</a>`;
}
function onEdit(td)
{if(confirm("Are you upadate student details")){
selectedRow=td.parentElement.parentElement;  
document.getElementById("FacultyName").value=selectedRow.cells[0].innerHTML;
document.getElementById("Training Attended").value=selectedRow.cells[1].innerHTML;
document.getElementById("Overall Rating").value=selectedRow.cells[2].innerHTML;
}
}
function isValid(){
var a=document.getElementById("FacultyName").value;
if(a==""|| a==null ){return false;}
 var  b = document.getElementById("Training Attended").value;
if(b==""|| b==null ){return false;}
 var c= document.getElementById("Overall Rating").value;
if(c==""|| c==null ){return false;}
else
{return true;}

}