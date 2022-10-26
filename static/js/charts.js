const pieOptions = ({ title, series, labels }) => {
    return {
        series: series,
        chart: {
            width: 500,
            type: 'pie',
        },
        labels: labels,
        title: {
            text: title,
            align: 'center',
            margin: 16,
            floating: false,
            style: {
                fontSize: '14px',
                fontWeight: 'bold',
                color: '#fff'
            },
        },
        dataLabels: {
            enabled: true,
            textAnchor: 'start',
            style: {
                colors: ['#fff'],
                fontSize: 12,
                fontWeight: 400
            },
            offsetX: 0,
            dropShadow: {
                enabled: false
            },
        },
        legend: {
            position: 'bottom'
        },
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 360,
                },
                legend: {
                    show: false,
                }
            }
        }, {
            breakpoint: 425,
            options: {
                chart: {
                    width: 320,
                },
                legend: {
                    show: false,
                }
            }
        }, {
            breakpoint: 375,
            options: {
                chart: {
                    width: 250,
                },
                legend: {
                    show: false,
                }
            }
        }]
    }
};

const barOption = ({ title, series, labels }) => {
    return {
        series: series,
        chart: {
            type: 'bar',
            width: 500,
            height: 500
        },
        plotOptions: {
            bar: {
                barHeight: '100%',
                distributed: true,
                horizontal: true,
                dataLabels: {
                    position: 'bottom'
                },
            }
        },
        dataLabels: {
            enabled: true,
            textAnchor: 'start',
            style: {
                colors: ['#fff'],
                fontSize: 9,
                fontWeight: 400
            },
            formatter: function (val, opt) {
                return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val
            },
            offsetX: 0,
            dropShadow: {
                enabled: false
            }
        },
        xaxis: {
            categories: labels,
        },
        yaxis: {
            labels: {
                show: false
            }
        },
        title: {
            text: title,
            align: 'center',
        },
        tooltip: {
            theme: 'light',
            x: {
                show: false
            },
            y: {
                title: {
                    formatter: function () {
                        return ''
                    }
                }
            }
        },
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 360,
                },
                legend: {
                    show: false,
                }
            }
        }, {
            breakpoint: 425,
            options: {
                chart: {
                    width: 320,
                },
                legend: {
                    show: false,
                }
            }
        }, {
            breakpoint: 375,
            options: {
                chart: {
                    width: 250,
                },
                legend: {
                    show: false,
                }
            }
        }]
    }
};

const getOption = ({ type, ...data }) => {
    switch (type) {
        case 'pie':
            return pieOptions(data);
        case 'bar':
            return barOption(data);
        default:
            return "Invalid Chart option";
    }
}

const charts = document.querySelector('#charts');
for (let key in data) {
    const option = getOption(data[key])
    const newChild = document.createElement('div');
    newChild.className = "p-6 rounded-md shadow-sm backdrop-blur-sm bg-indigo-800 text-center"
    const chartDiv = document.createElement('div');
    newChild.append(chartDiv)
    charts.insertAdjacentElement('beforeend', newChild);
    (new ApexCharts(chartDiv, option)).render();
}