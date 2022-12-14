let sidebar = document.querySelector("#sidebar");
let sidebarCont = document.querySelector("#sidebar-container");
let sidebarToggle = document.querySelector("#sidebar-toggle");
let sidebarToggleImg = document.querySelector("#sidebar-toggle img");
let searchBox = document.querySelector("#sidebar-search");
let searchInput = document.querySelector("#sidebar-search-input");
let searchBtn = document.querySelector("#sidebar-search-btn");
let sidebarItemsCont = document.querySelector("#sidebar-items-container");
let sidebarItems = document.querySelector("#sidebar-items");
let sidebarItemsArray = document.querySelector("#sidebar-items li.sidebar-item");
let sidebarItemIconsArray = document.querySelectorAll("#sidebar-items li.sidebar-item i.fa");
let sidebarItemNamesArray = document.querySelectorAll("#sidebar-items li.sidebar-item span.item-name");
let workspace = document.querySelector("#workspace");

let sidebarExpanded = true;



sidebarToggle.addEventListener("click", function(){
    if(sidebarExpanded){
        sidebar.classList.remove("expanded");
        sidebar.classList.add("collapsed");
        workspace.classList.remove("collapsed");
        workspace.classList.add("expanded");
    }else{
        sidebar.classList.remove("collapsed");
        sidebar.classList.add("expanded");
        workspace.classList.remove("expanded");
        workspace.classList.add("collapsed");
    }
    sidebarExpanded = !(sidebarExpanded);
});

sidebarToggle.addEventListener("mouseover", function(){
    sidebarToggleImg.classList.add("filter-blue");
})

sidebarToggle.addEventListener("mouseout", function(){
    sidebarToggleImg.classList.remove("filter-blue");
})