      let winkelmandItems = [];
      let winkelmandQuantities = [];
      let winkelmandPrices = [];
      let winkelmandSubTotals = [];
      let winkelmandRows = [];

      async function laadData() 
      {
        // start (asynchroon?) process om data op te halen uit db
        const response = await fetch('http://localhost:5000/producten');
        const result_dat = await response.json();
        
        // .then(response => response.json()) // Zet json als tekst om naar een object
        // .then(data => { //gebruik het resultaat van net als "data"

          let productenHtml = ""; //start van de stringbuild
          result_dat.forEach(product => { // voor elk item uit data noem dit product.
          productenHtml += `<tr>
                              <td>${product.naam}</td>
                              <td>${product.categorie}</td>
                              <td>${product.prijs}</td>
                              <td><button type="button" class="btn btn-secondary buyItem" data-bs-toggle="offcanvas"
                data-bs-target="#offcanvas">Voeg toe aan winkelmandje</button></td>
                              <td>
                                  <img class="img-fluid" src="${product.afbeelding_url}">
                              </td>
                            </tr>`
          // vul in het bovenstaande de string aan volgens een vast schema,
          // met kolomnamen "naam/categorie/prijs/afbeeldinurl"
          // <td>Toevoegen aan winkelmand.</td>
          });
          // product-pagina tabel
          document.getElementById('productCatalog').innerHTML = productenHtml;
          // pas in het document de innerhtml van element met id productcata... aan
          // met het resultaat van de gebouwde string.
      }
      
      function nieuwWinkelmandje(tabelRow, cart){
        // sidebar-winkelmandje 2e DIV
        document.getElementById("shopping-cart").innerHTML = "";
        let cartRow =   `<table id="shopping-cart-contents">
                        <tr>
                          <th>
                            Product
                          </th>
                          <th>
                            Aantal
                          </th>
                          <th>
                            SubTotaal
                          </th>
                        </tr>
                        <tr id="mandBucket1">
                          <td>
                            ${tabelRow.children[0].innerHTML}
                          </td>
                          <td>
                            1
                          </td>
                          <td>
                            ${tabelRow.children[2].innerHTML}
                          </td>
                        </tr>
                        </table>`
                        // <td>
                        //     <button><img src="wegermee.png" width="20" height="20">
                        //   </td>
          cart.innerHTML = cartRow;
          winkelmandItems.push(tabelRow.children[0].innerHTML);
          winkelmandQuantities.push(1);
          winkelmandPrices.push(tabelRow.children[2].innerHTML);
          winkelmandSubTotals.push(parseFloat(tabelRow.children[2].innerHTML));
          winkelmandRows.push("mandBucket1");

          // let totalPrice = document.createElement("div");
          // totalPrice.innerHTML = parseFloat(tabelRow.children[2].innerHTML);
          let totalPrice = document.getElementById("totaalVanMandje");
          // totalPrice.innerHTML += "Doei";
          totalPrice.innerHTML += arithmaticSubTotal(winkelmandSubTotals);
          // totalPrice.id = "sub-totaal";
          // sidebar-winkelmandje aanmaken 3e DIV
          // document.getElementById("offcanvas").appendChild(totalPrice);
          // console.log(totalPrice);

          // Als ik het bovenstaande ontleen, zie ik het volgende:
          //  - Een HTML-string die de tabel maakt.                       (1)
          //  - Een array die bijhoudt waarvan er minstens 1 item in zit  (2)
          //  - Een array die per item bijhoudt wat het subtotaal is      (3)
          //  - Een array die de id's van de entries bijhoudt             (4)
          //  - HET totaal van alle subtotalen --> valt te berekenen.     
          //  - dit geeft vier local storage items.

                              // Als ik bij het binnenhengelen in de laadDatacall ook het ID onthoud
                              // kan dit een stuk compacter
          // Bij het aanmaken van een nieuw winkelmandje, wordt de localstorage opnieuw gedefinieerd.
          localStorage.setItem("Producten",winkelmandItems);
          localStorage.setItem("Aantallen",winkelmandQuantities);
          localStorage.setItem("Prijzen",winkelmandPrices);

      }

      function arithmaticSubTotal(mandItems){
        let currentSubTotal = 0;
        for(let item = 0; item < mandItems.length; item++){
          currentSubTotal += mandItems[item];
        }
        return(parseFloat(currentSubTotal).toFixed(2));
      }

      function verhoogMandItem(tabelRij,mandjeItemNr){
        // tabelRij is hier een id-handle voor de volledige rij van de side-bar winkelmandje tabel
        const aantal = parseFloat(document.getElementById(tabelRij).cells[1].firstChild.nodeValue);
        const subsubtotaal = parseFloat(document.getElementById(tabelRij).cells[2].firstChild.nodeValue);
        const newsubtotaal = subsubtotaal/aantal;
        document.getElementById(tabelRij).cells[1].firstChild.nodeValue = aantal +1;
        document.getElementById(tabelRij).cells[2].firstChild.nodeValue = (newsubtotaal*(aantal+1)).toFixed(2);
        winkelmandSubTotals[mandjeItemNr] = parseFloat((newsubtotaal*(aantal+1)).toFixed(2));

        document.getElementById("totaalVanMandje").innerHTML = arithmaticSubTotal(winkelmandSubTotals);

        // Aanpassen van localStorage zodat er voor dit product één extra is.
        let hoeveelheden = JSON.parse("["+localStorage.getItem("Aantallen")+"]");
        let hoeveelheid = parseFloat(hoeveelheden[mandjeItemNr]);
        hoeveelheden[mandjeItemNr] = hoeveelheid+1;
        localStorage.setItem("Aantallen",hoeveelheden);
      }

      function voegItemToe(){
        let productAanwezig = false;
        const tabelRow = this.parentNode.parentElement;
        const cart = document.getElementById("shopping-cart");
        // Dit vervangt een eventueel leeg winkelmandje.
        // Met toekomstige functionaliteit kan dan een winkelmandje geleegd worden.
        // En dan moet deze weer worden "teruggezet" naar de tekst "Uw Winkelmandje is nog leeg."
        if(cart.innerHTML=="Uw Winkelmandje is nog leeg."){// als deze dus leeg is, maak een nieuwe aan.
          nieuwWinkelmandje(tabelRow, cart)
        }else{
          let productNaam = tabelRow.children[0].innerHTML;
          // ga elke waarde af in het huidige winkelmandje en kijk of het productnaam
          // er al in zit, zo ja, verhoog de quantity met 1, verhoog de prijs met product.prijs.
          for(let mandjeItemNr = 0; mandjeItemNr < winkelmandItems.length; mandjeItemNr++){
            if(productNaam == winkelmandItems[mandjeItemNr]){
              verhoogMandItem(winkelmandRows[mandjeItemNr],mandjeItemNr);
              productAanwezig = true;
              break;
            }
          }
        if(productAanwezig == false){
          // Productnamen
          winkelmandItems.push(tabelRow.children[0].innerHTML);
          localStorage.setItem("Producten",winkelmandItems);
          console.log(localStorage.getItem("Producten"));
          winkelmandSubTotals.push(parseFloat(tabelRow.children[2].innerHTML));
          // Product aantallen
          winkelmandQuantities.push(1);
          localStorage.setItem("Aantallen",winkelmandQuantities);
          // Product prijzen
          winkelmandPrices.push(tabelRow.children[2].innerHTML);
          localStorage.setItem("Prijzen",winkelmandPrices);
          // Product tabelrij
          winkelmandRows.push("mandBucket"+winkelmandItems.length);

          // if tabelRow.children[0] in keys van tabel verhoog aantal met 1
          // en verhoog subtotaal van producten met prijs.
          let shoppingCart = document.getElementById("shopping-cart-contents").firstElementChild;
          let newRow = document.createElement("tr");
          newRow.id = "mandBucket"+winkelmandItems.length;
          let prodName = document.createElement("td");
          let prodQuantity = document.createElement("td");
          let prodSubTotal = document.createElement("td");
          prodName.innerHTML = tabelRow.children[0].innerHTML;
          prodQuantity.innerHTML = 1;
          prodSubTotal.innerHTML = tabelRow.children[2].innerHTML;

          newRow.appendChild(prodName);
          newRow.appendChild(prodQuantity);
          newRow.appendChild(prodSubTotal);
          shoppingCart.appendChild(newRow);
          document.getElementById("totaalVanMandje").innerHTML = arithmaticSubTotal(winkelmandSubTotals);
        }
        // console.log(winkelmandSubTotals)
        // cart.innerHTML += tabelRow.children[0].innerHTML;
      }
    }

      function buttonsListenen(){
        // await laadData();
        const buttonCollection = document.getElementsByClassName("buyItem"); // zouden er dus 10 moeten zijn.
        // console.log(buttonCollection);
        for (let buttonnr = 0; buttonnr < buttonCollection.length; buttonnr++){
          buttonCollection[buttonnr].addEventListener("click",voegItemToe);
        }
      }


      function verversWinkelmandje(){
        let winkelmandItems = localStorage.getItem("Producten");
        winkelmandItems = winkelmandItems.split(",");

        let winkelmandAantallen = localStorage.getItem("Aantallen");
        winkelmandAantallen = winkelmandAantallen.split(",");

        let winkelmandPrijzen = localStorage.getItem("Prijzen");
        winkelmandPrijzen = winkelmandPrijzen.split(",");
        


        console.log(winkelmandItems);
        console.log(winkelmandAantallen);
        console.log(winkelmandPrijzen);
        
        let productenHtml = ""; //start van de stringbuild
        document.getElementById("shopping-cart").innerHTML = "";

        
        result_dat.forEach(product => { // voor elk item uit data noem dit product.
        productenHtml += `<tr>
                            <td>${product.naam}</td>
                            <td>${product.categorie}</td>
                            <td>${product.prijs}</td>
                            <td><button type="button" class="btn btn-secondary buyItem" data-bs-toggle="offcanvas"
              data-bs-target="#offcanvas">Voeg toe aan winkelmandje</button></td>
                            <td>
                                <img class="img-fluid" src="${product.afbeelding_url}">
                            </td>
                          </tr>`
        // vul in het bovenstaande de string aan volgens een vast schema,
        // met kolomnamen "naam/categorie/prijs/afbeeldinurl"
        // <td>Toevoegen aan winkelmand.</td>
        });

        let cartRow =   `<table id="shopping-cart-contents">
                        <tr>
                          <th>
                            Product
                          </th>
                          <th>
                            Aantal
                          </th>
                          <th>
                            SubTotaal
                          </th>
                        </tr>
                        <tr id="mandBucket1">
                          <td>
                            ${tabelRow.children[0].innerHTML}
                          </td>
                          <td>
                            1
                          </td>
                          <td>
                            ${tabelRow.children[2].innerHTML}
                          </td>
                        </tr>
                        </table>`
                        // <td>
                        //     <button><img src="wegermee.png" width="20" height="20">
                        //   </td>
          cart.innerHTML = cartRow;
          winkelmandItems.push(tabelRow.children[0].innerHTML);
          winkelmandQuantities.push(1);
          winkelmandPrices.push(tabelRow.children[2].innerHTML);
          winkelmandSubTotals.push(parseFloat(tabelRow.children[2].innerHTML));
          winkelmandRows.push("mandBucket1");

          // let totalPrice = document.createElement("div");
          // totalPrice.innerHTML = parseFloat(tabelRow.children[2].innerHTML);
          let totalPrice = document.getElementById("totaalVanMandje");
          // totalPrice.innerHTML += "Doei";
          totalPrice.innerHTML += arithmaticSubTotal(winkelmandSubTotals);
          // totalPrice.id = "sub-totaal";
          // sidebar-winkelmandje aanmaken 3e DIV
          // document.getElementById("offcanvas").appendChild(totalPrice);
          // console.log(totalPrice);

          // Als ik het bovenstaande ontleen, zie ik het volgende:
          //  - Een HTML-string die de tabel maakt.                       (1)
          //  - Een array die bijhoudt waarvan er minstens 1 item in zit  (2)
          //  - Een array die per item bijhoudt wat het subtotaal is      (3)
          //  - Een array die de id's van de entries bijhoudt             (4)
          //  - HET totaal van alle subtotalen --> valt te berekenen.     
          //  - dit geeft vier local storage items.

                              // Als ik bij het binnenhengelen in de laadDatacall ook het ID onthoud
                              // kan dit een stuk compacter
          // Bij het aanmaken van een nieuw winkelmandje, wordt de localstorage opnieuw gedefinieerd.
          localStorage.setItem("Producten",winkelmandItems);
          localStorage.setItem("Aantallen",winkelmandQuantities);
          localStorage.setItem("Prijzen",winkelmandPrices);

      }

      laadData().then(buttonsListenen);
      // Na het inladen van de tabel met producten en het toewijzen van functionaliteit aan de knoppen.
      // wordt gecontroleerd of er nog gegevens in de localstorage staan.
      // Zo ja, dan wordt het winkelmandje hersteld.
      if(localStorage.getItem("Producten")==null){
        document.getElementById("shopping-cart").innerHTML = "Uw winkelmandje is nog leeg.";
      }else{
        // verversWinkelmandje();
      }
// Nadat de tabel met de producten is geladen, zal gecontroleerd moeten worden óf en welke waardes er in de localstorage zitten van het winkelmandje.
// Stel dat daar niets in zit, zet de waarde van de div op "Uw Winkelmandje is nog leeg.".
      

