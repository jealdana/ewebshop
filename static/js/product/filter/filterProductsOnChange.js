$(document).ready(function(){
    $('#productSearchFilter').on('change', function() {
      let productsList = document.getElementById('productSearchFilter')
      if ( this.value == 'name')
      {
        productsList.setAttribute('value','name');
      }
      else
      {
        productsList.setAttribute('value','code');
      }
    });

    $('#sortItems').on('change', function() {
      let productsList = document.getElementById('productSearchFilter');
      if ( this.value == 'name')
      {
        filterProd({value:'name'});
        document.getElementById('sortItems').setAttribute('value','name');
        
      }
      else
      {
        filterProd({value:'price'});
        document.getElementById('sortItems').setAttribute('value','price');
      }
      
    });
});