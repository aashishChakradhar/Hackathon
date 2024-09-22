if(document.getElementById('RadarChart')){
    const ctx = document.getElementById('RadarChart').getContext('2d');

    const spans = document.querySelectorAll('.legend-list li span');

    let spanlist = [];

    for(let i=0; i<spans.length; i++){
        spanlist.push(spans[i].innerHTML)
    }
    
    const data = {
    labels: ['Coding', 'Leadership', 'Communication Skill', 'Presentation designing'],
    datasets: [{
        label: 'Student Skill Levels',
        data: spanlist,
        fill: true,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgb(54, 162, 235)',
        pointBackgroundColor: 'rgb(54, 162, 235)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(54, 162, 235)',
    }]
    };

    const config = {
    type: 'radar',
    data: data,
    borderJoinStyle: 'round',
    options: {
        responsive: false,
        maintainAspectRatio: false,
        elements: {
            line: {
                borderWidth: 3
            }
        },
        scales: {
            r: {
                angleLines: {
                    display: true, // Show the angle lines
                    color: 'rgba(0, 0, 0, 0.1)', // Color of the lines
                    lineWidth: 1 // Thickness of the lines
                },
                grid: {
                    circular: true, // Make grid lines circular instead of straight
                    color: 'rgba(0, 0, 0, 0.1)', // Color of the grid lines
                    lineWidth: 1 // Thickness of the grid lines
                },
                ticks: {
                    beginAtZero: true
                },
                pointLabels: {
                    font: {
                        size: 16, // Adjust the font size
                        weight: 'bold'
                    },
                    color: '#000', // Label color
                    padding: 20, // Add padding to move the labels outward
                }
            }
        }
    }
    };

    const radarChart = new Chart(ctx, config);
}