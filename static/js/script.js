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
        let parentDiv = document.createElement('div');
        for (let key in groupedData.data[i]) {
            let div = document.createElement('div');
            let name = document.createElement('p');
            let email = document.createElement('p');
            name.innerHTML = groupedData.data[i][key]['Name'];
            email.innerHTML = groupedData.data[i][key]['Email'];
            div.appendChild(name);
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

