function chercher(object){

    if(object.value != ""){
        elems = document.querySelectorAll("#pokemon_list .affichage:not([id*='" + object.value + "'])");
        elemsV = document.querySelectorAll("#pokemon_list .affichage[id*='" + object.value + "']");

        hide(elems);
        show(elemsV);
    }
    else{
        elems = document.querySelectorAll("#pokemon_list .affichage");

        show(elems);
    }
}

function hide(elements){
    elements.forEach(element => {
        element.classList.remove('flex')
        element.hidden = true;
    });
}

function show(elements){
    elements.forEach(element => {
        element.classList.add('flex')
        element.hidden = false;
    });  
}