$(document).ready(function() {
  $("#prodCreate").submit(function(event) {
    event.preventDefault();
    $.ajax({ data: $(this).serialize(), 
            type: $(this).attr('method'), 
            url: $(this).attr('action'), 
            success: function(response) {
                 console.log(response);
                 if(response['success']) {
                    // Notify the manager that the item was created
                    alert('Product successfully created!');
                    // Refresh the products listed
                    allProd();
                 } 
                 if(response['error']) {
                     $("#feedbackmessage").html("<div class='alert alert-danger'>" +
                     response['error']['comment'] +"</div>");
                 } 
            },
            error: function (request, status, error) {
                 console.log(request.responseText);
            }
   });
  });
  
});

let createProductCard = (product) => {

    let card = createDiv('div',{className:'card',innerText:'',innerHTML:''});

    let cardImg = createDiv('img',{className:'card-img-top',innerText:'',innerHTML:''});
      cardImg.setAttribute("src", product.photo_url);
      cardImg.setAttribute("style", "height: 20em;");

    let cardBody = createDiv('div',{className:'card-body',innerText:'',innerHTML:''});
    
    let title = createDiv('h5',{innerText:product.name,className:'card-title'});
    let code = createDiv('p',{innerText:`Code ${product.code}`,className:'card-text'});
    let price = createDiv('p',{innerText:`USD $ ${product.price}`,className:'card-text'});

    let footer = createDiv('div',{className:'card-footer',innerText:'',innerHTML:''});
    let lastPurchase = createDiv('small',{innerText:`Last purchase made ${Math.floor(Math.random() * 100)} mins ago`,className:'text-muted'});

    
    
    footer.appendChild(lastPurchase);
    cardBody.appendChild(title);
    cardBody.appendChild(code);
    cardBody.appendChild(price);
    cardBody.appendChild(descriptionCard(product));      

    card.appendChild(cardImg);
    card.appendChild(cardBody);
    card.appendChild(footer);
    return card;

  }
