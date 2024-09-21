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
        return {data};   
    }

    groupedData = await get_response();

    for(let i=0; i<Object.keys(groupedData.data).length; i++){
        let parentDiv = document.createElement('div');
        parentDiv.classList.add('col-md-3');

        for (let key in groupedData.data[i]) {
            let div = document.createElement('div');
            div.classList.add('groupitems')
            let name = document.createElement('p');
            let email = document.createElement('p');
            let skill = document.createElement('p');
            name.innerHTML = groupedData.data[i][key]['Name'];
            email.innerHTML = groupedData.data[i][key]['Email'];

            coding = groupedData.data[i][key]['Coding'];
            Leadership = groupedData.data[i][key]['Leadership'];
            communication = groupedData.data[i][key]['Communication Skill'];
            presentation = groupedData.data[i][key]['Presentation designing'];

            skills = {'Coding': coding, 'Leadership': Leadership, 'Communication' : communication, 'Presentation': presentation}
            const topTwoSpecialities = Object.entries(skills).sort(([, a], [, b]) => b - a).slice(0, 2).map(([key]) => key); 
            div.appendChild(name);
            div.appendChild(email);

            topTwoSpecialities.forEach((e)=>{
                const specialityElement = document.createElement('span');
                specialityElement.textContent = e;
                skill.appendChild(specialityElement);
            })
            parentDiv.appendChild(div);
        }
        document.getElementById('itemdisplay').appendChild(parentDiv);
    }
}
processResponse();

