$(function () {
    $('#container').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Top 10 States with Highest Inbound And Outbound Load '
        },
        subtitle: {
            text: ''
        },
        xAxis: {
            categories: topstates,
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Truck Loads (X10000)',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' X10000'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 100,
            floating: true,
            borderWidth: 1,
            backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            shadow: true
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Inbound',
            data: topinbound
        }, {
            name: 'Outbound',
            data: topoutbound
        }]
    });
});
