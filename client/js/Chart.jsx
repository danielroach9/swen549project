import React, {Component} from "react";

export default class Chart extends Component {

    // override Component class functions

    constructor(props){
        super(props);
        this.state = {
          error: null,
          isLoaded: false,
          data: [],
        };
        google.charts.load('current', {packages: ['corechart']});


    }

    componentDidMount(){
        google.charts.setOnLoadCallback(this.drawChart.bind(this));
        this.fetchData();

    }

    fetchData(){
        fetch("/globalData")
            .then(result => result.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded:true,
                        data: result.scoreSales,
                    });
                },

                (error) => {
                    this.setState({
                        isLoaded: true,
                        error: error
                    });
                }
            )
    }


    render(){
        if (this.state.error){
            return <div>Error: {error.message}</div>;
        }
        else if(!this.state.isLoaded){
            return <div>Loading....</div>
        }
        else{

        }
        return <div id="chart"></div>;
    }

    // non Component functions
    drawChart() {
      // Define the chart to be drawn.
      let data = new google.visualization.DataTable();
      data.addColumn('number', 'Score');
      data.addColumn('number', 'Global Sales');
      data.addRows(this.state.data);

      let options = {
          title: "IGN Reviews vs. Global Video Game Sales",
          hAxis: {title:"IGN Review Score"},
          vAxis: {title:"Global Sales (in millions)"},
          legend: 'none',
          trendlines: {0:{}},
      };

      // Instantiate and draw the chart.
      let chart = new google.visualization.ScatterChart(document.getElementById('chart'));
      chart.draw(data, options);
    }
}