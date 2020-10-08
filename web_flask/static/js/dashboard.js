/* globals Chart:false, feather:false */

(function () {
    'use strict'

    feather.replace()

    // Graphs
    var ctx = document.getElementById('myChart')
    // eslint-disable-next-line no-unused-vars
    ontario_data = JSON.parse(ctx.dataset.status),
        dates = [],
        confirmed = [],
        resolved = [],
        deceased = [],

        ontario_data.forEach(function (daily) {
            dates.push(daily['date']);
            confirmed.push(daily['confirmed']['total'])
            resolved.push(daily['resolved'])
            deceased.push(daily['deceased'])

        })
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                data: confirmed,
                lineTension: 0,
                backgroundColor: 'transparent',
                borderColor: '#dc3545',
                borderWidth: 4,
                pointBackgroundColor: '#dc3545'
            },
            {
                data: resolved,
                lineTension: 0,
                backgroundColor: 'transparent',
                borderColor: '#28a745',
                borderWidth: 4,
                pointBackgroundColor: '#28a745'
            },
            {
                data: deceased,
                lineTension: 0,
                backgroundColor: 'transparent',
                borderColor: '#34340',
                borderWidth: 4,
                pointBackgroundColor: '#343a40'
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: false
                    }
                }]
            },
            legend: {
                display: false
            }
        }
    })
}())
