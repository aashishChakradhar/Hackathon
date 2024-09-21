async function processResponse() {
    async function get_response() {
        const api = 'http://127.0.0.1:8001/predict';
        const response = await fetch(api,{
                method : 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            }
        )

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log(data)
        return {data};   
    }

    groupedData = await get_response();

    for(let i=0; i<Object.keys(groupedData.data).length; i++){
        // console.log(`group ${i} : ${groupedData.data[i]}`)

        let parentDiv = document.createElement('div');
        parentDiv.classList.add('col-md-3');

        // for(let k=0; k<Object.keys(groupedData.data[i]).length; k++){
        //     console.log(`${i}, ${k}`)
        // }
        for (let key in groupedData.data[i]) {
            console.log(`${i} , ${key}`);
            let div = document.createElement('div');
            div.classList.add('groupitems')
            let name = document.createElement('p');
            let skill = document.createElement('p');
            let email = document.createElement('p');
            name.innerHTML = groupedData.data[i][key]['Name'];
            skill.innerHTML = groupedData.data[i][key]['skills'];
            email.innerHTML = groupedData.data[i][key]['Email'];
            div.appendChild(name);
            div.appendChild(skill);
            div.appendChild(email);
            // div.innerHTML = groupedData.data[i][key]['Email'];
            parentDiv.appendChild(div);
            console.log(`Key: ${key}, Value:`, groupedData.data[i][key]);
        }
        document.getElementById('itemdisplay').appendChild(parentDiv);
        // console.log(groupedData.data[i]);
    }

    // groupedData.data.forEach((element) => {
    //     console.log(element);
    // });
}
processResponse();

