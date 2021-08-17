$(document).on('submit','#addCart', function(e){
    e.preventDefault();

    let qty = $(this).find('input[type=number]').val();
    let prodID = $(this).attr("value");

    fetch(`/product/${prodID}/`).then(response => response.json())
      .then(data => {
        // Create list item for the cart list
        let li = createDiv('li', {innerText:``, className:'list-group-item d-flex justify-content-between lh-condensed'});
        let div = createDiv('div', {innerText:``, className:'my-0'});
        let h6 = createDiv('h6', {innerText:`${data.name} - $ ${data.price} X ${qty}`, className:'my-0'});
        let span = createDiv('span', {innerText:`$ ${data.price * parseInt(qty) }`, className:'text-muted'});

        div.appendChild(h6);
        li.appendChild(div);
        li.appendChild(span);
        document.getElementById('cartList').appendChild(li);

        // Recalculate Total cost in the cart
        let total = document.getElementById('total');
        let new_cost = data.price * parseInt(qty);
        let newTotal = parseFloat(total.getAttribute('value')) + new_cost;
        total.setAttribute('value',newTotal) ;
        total.innerText = newTotal;

        // Update the cart value
        let cartBadge = document.getElementById('cartBadge');
        let newcartBadge = parseFloat(cartBadge.getAttribute('value')) + parseInt(qty);
        cartBadge.setAttribute('value',newcartBadge) ;
        cartBadge.innerText = newcartBadge;

      });
    
  });