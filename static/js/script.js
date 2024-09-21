async function saveJsonFile(data) {
  const jsonData = JSON.stringify(data, null, 2);

  try {
      // Prompt user to choose where to save the file
      const fileHandle = await window.showSaveFilePicker({
          suggestedName: 'data.json',
          types: [{
              description: 'JSON file',
              accept: { 'application/json': ['.json'] }
          }]
      });

      // Create a writable stream
      const writableStream = await fileHandle.createWritable();

      // Write the JSON data to the file
      await writableStream.write(jsonData);

      // Close the file stream to save changes
      await writableStream.close();

      console.log("File saved successfully!");
  } catch (err) {
      console.error("Error saving the file:", err);
  }
}

if (document.getElementById('teamDivider')) {
  document.getElementById('teamDivider').addEventListener('click', () => {
      async function processResponse() {
          async function get_response() {
              const api = 'http://127.0.0.1:8001/predict';
              const response = await fetch(api, {
                  method: 'POST',
                  headers: {
                      'Content-Type': 'application/json'
                  }
              }
              )

              if (!response.ok) {
                  throw new Error(`HTTP error! status: ${response.status}`);
              }
              const data = await response.json();
              return { data };
          }

          groupedData = await get_response();

          saveJsonFile(groupedData.data);

          for (let i = 0; i < Object.keys(groupedData.data).length; i++) {

              let gparentDiv = document.createElement('div');
              gparentDiv.classList.add('item-group');
              let parentDiv = document.createElement('div');
              parentDiv.classList.add('group-box');

              for (let key in groupedData.data[i]) {
                  const div = document.createElement('div');
                  let name = document.createElement('p');
                  let email = document.createElement('p');
                  let skill = document.createElement('p');

                  div.classList.add('groupitems');

                  name.innerHTML = groupedData.data[i][key]['Name'];
                  email.innerHTML = groupedData.data[i][key]['Email'];
                  coding = groupedData.data[i][key]['Coding'];
                  Leadership = groupedData.data[i][key]['Leadership'];
                  communication = groupedData.data[i][key]['Communication Skill'];
                  presentation = groupedData.data[i][key]['Presentation designing'];

                  skills = { 'Coding': coding, 'Leadership': Leadership, 'Communication': communication, 'Presentation': presentation }
                  const topTwoSpecialities = Object.entries(skills).sort(([, a], [, b]) => b - a).slice(0, 2).map(([key]) => key);

                  topTwoSpecialities.forEach((e) => {
                      const specialityElement = document.createElement('span');
                      specialityElement.textContent = e;
                      skill.appendChild(specialityElement);
                  })

                  div.appendChild(name);
                  div.appendChild(email);
                  div.appendChild(skill);

                  parentDiv.appendChild(div);
              }
              gparentDiv.appendChild(parentDiv);
              document.getElementById('itemdisplay').appendChild(gparentDiv);
          }

      }
      processResponse();
  })

}