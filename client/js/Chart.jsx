import React, {Component} from "react";
import RegionFilter from './RegionFilter';
import SubmitButton from './SubmitButton';

export default class Chart extends Component {

    // override Component class functions



    constructor(props){
        super(props);

        this.state = {
            error: null,
            isLoaded: false,
            salesRegion: "Global Sales",
            data: [],
            dataTable: null,
            filterValues: [''],
            updateData: false,
        };
        google.charts.load('current', {packages: ['corechart']});

        this.handleRegionChange = this.handleRegionChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }

    componentDidMount(){
        google.charts.setOnLoadCallback(this.drawChart.bind(this));
        this.fetchData();

    }

    handleRegionChange(region){
        console.log("changing region to "+region);
        this.state.filterValues[0] = region;

        let data = this.state.dataTable;
        let vals = this.state.filterValues;

        this.setState({
            dataTable: data,
            filterValues: vals,
            salesRegion: region,
            updateData: false,
        });
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
                    error: error,
                    initialLoad:true,
                });
            }
        );
    }

    handleSubmit(){

        fetch("/filterData", {
            method: 'POST',
            body: JSON.stringify({'filters':this.state.filterValues}),
        })
        .then( response => response.json() )
        .then(
            (response) => {
                this.setState({
                    isLoaded: true,
                    data: response.filteredData,
                    updateData:true,
                });
            },

            (error) => {
                this.setState({
                    isLoaded: true,
                    error: error,
                });
            },
        );

    }



    render(){
        if (this.state.error){
            return <div>Error: {this.state.error.message}</div>;
        }
        else if(!this.state.isLoaded){
            return <div>Loading....</div>
        }
        else{

        }
        return (
            <div>
                <div id="chart"></div>
                <RegionFilter handleChange={this.handleRegionChange}/>
                <SubmitButton handleSubmit={this.handleSubmit}/>
            </div>
        );
    }
    componentDidUpdate(){
        console.log(this.state.salesRegion);
        if (this.state.updateData){
            this.drawChart();
        }
    }
    // non Component functions
    drawChart(){
      // Define the chart to be drawn.
      let data = new google.visualization.DataTable();
      data.addColumn('number', 'Score');
      data.addColumn('number', this.state.salesRegion);
      data.addRows(this.state.data);

      let options = {
          title: "Video Games' IGN Reviews vs. "+this.state.salesRegion,
          hAxis: {title:"IGN Review Score"},
          vAxis: {title:this.state.salesRegion+" (in millions)"},
          legend: 'none',
          trendlines: {0:{}},
      };
      // this.setState({dataTable:data});
      // Instantiate and draw the chart.
      let chart = new google.visualization.ScatterChart(document.getElementById('chart'));
      chart.draw(data, options);
    }
}