import React, {Component} from "react";

export default class Chart extends Component {

    // override Component class functions

    constructor(props){
        super(props);
    }


    render(){
        return <div id="mainChart"></div>;
    }

    // non Component functions
    drawChart(){
        let data = google.visualization.arrayToDataTable([
          ['Age', 'Weight'],
          [ 8,      12],
          [ 4,      5.5],
          [ 11,     14],
          [ 4,      5],
          [ 3,      3.5],
          [ 6.5,    7]
        ]);

        let options = {
          title: 'Age vs. Weight comparison',
          hAxis: {title: 'Age', minValue: 0, maxValue: 15},
          vAxis: {title: 'Weight', minValue: 0, maxValue: 15},
          legend: 'none'
        };

        let chart = new google.visualization.ScatterChart(document.getElementById('mainChart'));

        chart.draw(options, data);
    }
}