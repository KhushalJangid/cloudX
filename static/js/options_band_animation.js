let band = document.querySelector("#options-band");
let buttons = document.querySelectorAll("#options-band td button");
let imgs = document.querySelectorAll("#options-band td button img");


for(let i = 0; i < buttons.length; i++){
    buttons[i].addEventListener("mouseover", function(){
        imgs[i].classList.add("btn-hovered");
    });

    buttons[i].addEventListener("mouseout", function(){
        imgs[i].classList.remove("btn-hovered");
    });
}