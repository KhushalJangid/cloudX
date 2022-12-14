function setProgressValue(progressContainerElement, percentage){
    //get the fill element:
    let fillElement;
    for(let i = 0; i < progressContainerElement.childNodes.length; i++){
        if(progressContainerElement.childNodes[i].tagName == "DIV"){
            fillElement = progressContainerElement.childNodes[i];
        }
        // if(progressContainerElement.childNodes[i].classList.contains("progress-line")){
        // }
    }
    //apply the styles:
    fillElement.style.width = percentage + "%";

    //to change the number below the bar:
    let siblings = progressContainerElement.parentElement.childNodes;
    let spanElement;
    for(let i = 0; i < siblings.length; i++){
        if(siblings[i].tagName == "SPAN"){
            if(siblings[i].classList.contains("progress-percentage")){
                for(let j = 0; j < siblings[i].childNodes.length; j++){
                    if(siblings[i].childNodes[j].tagName == "SPAN"){
                        spanElement = siblings[i].childNodes[j];
                    }
                }
            }
        }
    }

    spanElement.innerText = percentage;
}