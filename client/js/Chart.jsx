import React, {Component} from "react";

export default class Chart extends Component {

    // override Component class functions

    constructor(props){
        super(props);
        google.charts.load('current', {packages: ['corechart']});

    }

    componentDidMount(){
        google.charts.setOnLoadCallback(this.drawChart.bind(this));

    }


    render(){
        return <div id="pieChart"></div>;
    }

    // non Component functions
    drawChart() {
      // Define the chart to be drawn.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Element');
      data.addColumn('number', 'Percentage');
      data.addRows([
        ['Nitrogen', 0.78],
        ['Oxygen', 0.21],
        ['Other', 0.01]
      ]);

      // Instantiate and draw the chart.
      let chart = new google.visualization.PieChart(document.getElementById('pieChart'));
      chart.draw(data, null);
    }
}