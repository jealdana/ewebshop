function filterProd(order_by={value:'name'}){
      
    let productSearchFilter = document.getElementById('productSearchFilter');
    let productSearchInput = document.getElementById('productSearchInput');
    

    let productsList = document.getElementById('productsList');
    
    fetch(`/product/?${productSearchFilter.getAttribute('value')}=${productSearchInput.value}&order_by=${order_by.value}`)
      .then(response => response.json())
      .then(data => {
        let allProductsMockupList = data.results;
    
        let productsList = document.getElementById('productsList');
        productsList.innerHTML = '';
        
        allProductsMockupList.forEach( product => 
            { 
              let colDiv = createDiv('div',{className:'col',innerText:'',innerHTML:''});
              colDiv.appendChild( createProductCard(product) );
              productsList.appendChild(colDiv);
            }
          );
      });

    
  }

  
function allProd(){
    let productSearchFilter = document.getElementById('productSearchFilter');
    let productSearchInput = document.getElementById('productSearchInput');
    productSearchFilter.setAttribute('value','name');
    productSearchInput.value = '';

    filterProd({value:document.getElementById('sortItems').getAttribute('value')});
}
