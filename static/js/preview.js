function createThumbnail(){
    file = document.getElementById("file").files[0];
    console.log(file.type);
    frame = document.getElementsByClassName("pdf-frame");
    if(frame.length == 0){
        container = document.createElement("div");
        container.classList.add("pdf-frame");
        container.classList.add("mv-1");
        document.getElementById("preview-container").appendChild(container);
    } else {
        container = frame[0];
        container.innerHTML = '';
    }
    if(file.type == "application/pdf"){
        tag = document.createElement("embed");
        tag.classList.add("pdf");
        tag.type = file.type;
        if (file) {
                const reader = new FileReader();
                reader.onload = function () {
                    const result = reader.result;
                    tag.src = result;
                }
                reader.readAsDataURL(file);
            }
        container.appendChild(tag);
    } else{
        tag = document.createElement("img");
        tag.classList.add("pdf");
        if (file) {
                const reader = new FileReader();
                reader.onload = function () {
                    const result = reader.result;
                    tag.src = result;
                }
                reader.readAsDataURL(file);
            }
        container.appendChild(tag);
    }
    return 0;
}