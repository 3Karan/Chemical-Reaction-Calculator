let screen = document.getElementById("screen");
buttons = document.querySelectorAll("button");
let screenValue = "";
screen.value = ""

let footer = document.createElement("div");
footer.innerHTML = "<p>For comments and feedback, contact us by email: dnapen [at] guptalab.org <br/><br/> ChemicalCALC (copyright © 2021 <a href='https://www.guptalab.org/mankg/public_html/'>Manish K. Gupta</a>) has been developed by <a href='https://www.linkedin.com/in/tulsi-shah-a5250b1a4'>Tulsi Shah</a>, <a href='https://www.linkedin.com/in/janvi-patel-aa3a5a1a5/'>Janvi Patel</a>, <a href='https://www.linkedin.com/in/skand-vala-95a0b6189'>Skand Vala</a>, <a href='https://www.linkedin.com/in/khushalishah7/'>Khushali Shah</a>, <a href='https://www.linkedin.com/in/nishtha-chaudhary-92573319b/'>Nishtha Chaudhary</a>, <a href='https://www.linkedin.com/in/ritka-lakdawala-a0272a21a/'>Ritika Lakdawala</a>.<br/><br/> Dhirubhai Ambani Institute of Information and Communication Technology <br/> Room 2209 Faculty Block 2, Near Indroda Circle, Gandhinagar, Gujarat INDIA 382 007 <br/> Phone: 91-79-30510549, Fax: 91-79-30520010. Assistant (Deepa Poduval) Phone: 91-79-30510552. <br/> Any selling or distribution of the program or its parts, original or modified, is prohibited without a written permission from Manish K. Gupta. Last updated on December 11, 2021.</p>";  
footer.setAttribute('class','footer');
document.body.appendChild(footer);

for (item of buttons) {

    item.addEventListener('click', (e) => {
        buttontxt = e.target.innerText;
        

        if (buttontxt == 'X') {
            buttontxt = '*';
            screenValue += buttontxt;
            screen.value = screenValue;
        }
        else if (buttontxt == 'C') {
            screenValue = ""
            screen.value = screenValue;
            removeElementsByClass("styled-table");
            removeElementsByClass("styled-table-reactions");
            removeElementsByClass("downloadbtn")

        }
        else if (buttontxt == '=') {

            screen.value = eval(screenValue);
            ChemicalCALC();
        }
            
        else if(buttontxt=='1' || buttontxt=='2' || buttontxt=='3'  || buttontxt=='4' || buttontxt=='5' || buttontxt=='6' || buttontxt=='7' || buttontxt=='8' || buttontxt=='9' || buttontxt=='0' || buttontxt=='/' || buttontxt=='+' || buttontxt=='-' || buttontxt=='(' || buttontxt==')') {
            screenValue += buttontxt;
            screen.value = screenValue;
        }
        else
        {
            if(screenValue.length!=0)
            {

                screenValue = screenValue.substring(0, screenValue.length - 1);
                screen.value = screenValue;
                removeElementsByClass("styled-table");
                removeElementsByClass("styled-table-reactions");
                removeElementsByClass("downloadbtn")

            }
        }

    })
}





const ChemicalCALC = async () => {

    var myBody = {
        'exp': screenValue,
    }
  //const response = await fetch('https://chemicalcalcapp.herokuapp.com/chemicalCALCapp',{
     console.log("Tulsi")                           
    const response = await fetch("/chemicalCALC",{
        method: 'POST',
        body: JSON.stringify(myBody), // string or object
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }

    });
    const myJson = await response.json(); //extract JSON from the http response
    console.log(myJson);
    display(myJson['data']);
    
    // do something with myJson
}

function removeElementsByClass(className){
    const elements = document.getElementsByClassName(className);
    while(elements.length > 0){
        elements[0].parentNode.removeChild(elements[0]);
    }
}
//console.log("Tulsi")
function display(data) {
   
    console.log(data)
    
    for (let i = 0; i < data[0].length; i++) {
        var table_reactions = document.createElement("TABLE");
        var table = document.createElement("TABLE");
        table.classList.add("styled-table");
        table_reactions.classList.add("styled-table-reactions");
        
        let rowRea = document.createElement('tr')
        var colRea = document.createElement("th");
        let textRea = document.createTextNode(data[0][i]);
        colRea.appendChild(textRea);
        rowRea.appendChild(colRea);

        let headerRea= document.createElement('thead');
        headerRea.appendChild(rowRea);

        table_reactions.appendChild(headerRea);

        //div.innerHTML = data[0][i];

        for (let j = 0; j < data[1][i].length; j++) {

            let rowRea = document.createElement('tr')
            var colRea = document.createElement("td");
            let textRea = document.createTextNode(data[1][i][j]);
            colRea.appendChild(textRea);
            rowRea.appendChild(colRea);

            table_reactions.appendChild(rowRea);
        }

        let table_header = [];
        table_header.push("Reaction");
        table_header.push("Number Of Iterations");

        for(let k = 0;k<data[3][i].length;k++)
        {
            table_header.push(data[3][i][k]);
        }



        
        let row = document.createElement('tr')
        let header = document.createElement('thead');
        for (let k = 0; k <table_header.length; k++) {
            var col = document.createElement("th");
            let text = document.createTextNode(table_header[k]);
            col.appendChild(text);
            row.appendChild(col);
        }
        header.appendChild(row);
        table.appendChild(header);
        

        for (let j = 0; j < data[2][i].length; j++) {
            let row = document.createElement('tr');
            for (let k = 0; k < data[2][i][j].length; k++) {
                var col = document.createElement("td");
                let text = document.createTextNode(data[2][i][j][k]);
                col.appendChild(text);
                row.appendChild(col);
            }

            table.appendChild(row);



        }

        document.body.appendChild(table_reactions);
        document.body.appendChild(table);


    }

    let btn = document.createElement("button");
    btn.innerHTML = "Download (XML)";
    btn.setAttribute('class','downloadbtn');
    
    btn.onclick = function(){window.location.href="/download"};
    document.body.appendChild(btn);

    removeElementsByClass("footer");
    document.body.appendChild(footer);
}

