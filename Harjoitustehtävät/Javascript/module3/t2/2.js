const lista = document.getElementById("target")
const tasklist = ["First item", "Second item", "Third item"]
tasklist.forEach(task => {
    const newline = document.createElement("li");
    newline.textContent = task;
    lista.appendChild(newline);
});

lista.children[1].className="my-item";