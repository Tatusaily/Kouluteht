'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
const target = document.getElementById("target");
students.forEach(student =>{
  const newelement = document.createElement("option");
  newelement.value = student.id;
  newelement.innerHTML = student.name;
  target.appendChild(newelement);
});