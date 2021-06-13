let descriptionCard = (product) => {
    let accordion = createDiv('div',{className:'accordion',innerText:'',innerHTML:''});
    accordion.innerHTML = `
    <div class="accordion" id="accordionExample">
                          <div class="card">
                            <div class="card-header" id="heading-${product.id}">
                              <h2 class="mb-0 text-center">
                                <button class="btn btn-link btn-block" type="button" data-toggle="collapse" data-target="#collapse-${product.id}" aria-expanded="true" aria-controls="collapse-${product.id}">
                                  see more
                                </button>
                              </h2>
                            </div>
                        
                            <div id="collapse-${product.id}" class="collapse" aria-labelledby="heading-${product.id}" data-parent="#accordionExample">
                              <div class="card-body p-3">                                    
                                  ${product.description}
                                  <br></br>
                                  <form id="addCart" value="${product.id}" >
                                      <label for="quantity">Quantity:</label>
                                      <div class="input-group mb-3">
                                          <input type="number" id="quantity" name="quantity" min="1" class="form-control" placeholder="1" value='1' aria-label="Recipient's username" aria-describedby="basic-addon2">
                                          <div class="input-group-append">
                                            <button class="btn btn-primary" type="submit">Add to cart</button>
                                          </div>
                                      </div>
                                  </form>
                              </div>
                            </div>
                          </div>
                        </div>  
    `;
    accordion.setAttribute('id',"accordionExample");
    let card = createDiv('div',{className:'card',innerText:'',innerHTML:''});
    let cardHeader = createDiv('div',{className:'card-header',innerText:'',innerHTML:''});
    let h2 = createDiv('div',{className:'mb-0 text-center',innerText:'',innerHTML:''});
    let buttonCustom = createDiv('div',{className:'btn btn-link btn-block',innerText:'see more',innerHTML:''});
    let collapseDiv = createDiv('div',{className:'collapse',innerText:'',innerHTML:''});
    let cardBody = createDiv('div',{className:'card-body p-3',innerText:'',innerHTML:''});
    let form = createDiv('div',{className:'card',innerText:'',innerHTML:''});
    let label = createDiv('div',{className:'card',innerText:'Quantity:',innerHTML:''});
    let inputGroup= createDiv('div',{className:'input-group mb-3',innerText:'',innerHTML:''});
    let inputQty = createDiv('div',{className:'form-control',innerText:'',innerHTML:''});
    let inputButtonGroup = createDiv('div',{className:'input-group-append',innerText:'',innerHTML:''});
    let inputButton = createDiv('div',{className:'btn btn-primary',innerText:'',innerHTML:''});
    return accordion;
  }
