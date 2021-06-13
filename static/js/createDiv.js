function createDiv(type,kwargs = {className:'',innerText:'',innerHTML:''}){
    let divCustom = document.createElement(type);
    divCustom.innerText = (kwargs.innerText === '') ? "" : kwargs.innerText;        
    divCustom.className = (kwargs.className === '') ? "" : kwargs.className;
    return divCustom;
  
}