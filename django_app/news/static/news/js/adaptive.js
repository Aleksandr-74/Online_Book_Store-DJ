window.addEventListener('DOMContentLoaded', function(){

    `use strict`;

    let el = document.querySelectorAll(".categ-col");
    let ul = document.querySelectorAll(".categ-list");
    el.forEach(function(item, i, el){
        let width = document.documentElement.scrollWidth;
        item.addEventListener('mouseover', function(){
             if(this && document.documentElement.scrollWidth <= 799){
                ul[i].classList.add("categ-list_on");
             };
        });

        item.addEventListener('mouseout', function(){
             if(this && document.documentElement.scrollWidth <= 799){
                ul[i].classList.remove("categ-list_on");
             };
        });
     });
});



