import React, {Component} from "react";
import RegionFilter from './RegionFilter';
import GenreFilter from './GenreFilter';
import ScoreFilter from './ScoreFilter'
import SubmitButton from './SubmitButton';
import Spinner from './Spinner';

import $ from "jquery";
export default class Chart extends Component {

    // override Component class functions

    constructor(props){
        super(props);

        this.state = {
            error: null,
            isLoaded: false,
            salesRegion: "Global Sales",
            data: [],
            genres: [],
            dataTable: null,
            filterValues: ['Global Sales','All','All'],
            updateData: false,
        };
        google.charts.load('current', {packages: ['corechart']});

        this.handleRegionChange = this.handleRegionChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.drawChart = this.drawChart.bind(this);

    }

    componentDidMount(){
        this.fetchData();

    }

    handleRegionChange(idx,region){
        console.log("index is " +idx);
        this.state.filterValues[idx] = region;

        let data = this.state.dataTable;
        let vals = this.state.filterValues;
        if( idx === 0){
            this.setState({
                dataTable: data,
                filterValues: vals,
                salesRegion: region,
                updateData: false,
            });
        }
        else {
            this.setState({
                dataTable: data,
                filterValues: vals,
                updateData: false,
            });
        }

    }


    fetchData(){
        console.log("fetching");

        $.ajax({
            url: "/globalData",
            success: (result) => {
                result = JSON.parse(result);

                this.setState({
                    isLoaded:true,
                    data: result.scoreSales,
                    genres: result.genres,
                    updateData: false,
                });
                console.log("done");
            },
            error: (error) => {
                this.setState({
                    isLoaded: true,
                    error: error,
                });
            },

        });

    }

    handleSubmit(){

        fetch("/filterData", {
            method: 'POST',
            body: JSON.stringify({'filters':this.state.filterValues}),
        })
        .then( response => response.json() )
        .then(
            (response) => {
                console.log(response);
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
            return <Spinner/>;
        }
        else {

            return (
                <div className="container">
                    <div className="row">
                        <div id="chart" style={{height:"550px",width:"950px"}}></div>
                    </div>
                    <div className="row">
                        <RegionFilter handleChange={this.handleRegionChange}/>
                        <GenreFilter genres={this.state.genres} handleChange={this.handleRegionChange}/>
                        <ScoreFilter handleChange={this.handleRegionChange}/>
                    </div>
                    <div className="row">
                        <SubmitButton handleSubmit={this.handleSubmit}/>
                    </div>

                </div>
            );
        }
    }

    componentDidUpdate(){
        if (this.state.updateData){
            console.log("updated");
            this.drawChart();
        }
        else{
            google.charts.setOnLoadCallback(this.drawChart);
        }

    }

    // non Component functions
    drawChart(){
      // Define the chart to be drawn.
      let data = new google.visualization.DataTable();

      let options = {
          title: "Video Games' IGN Reviews vs. "+this.state.salesRegion,
          hAxis: {title:"IGN Review Score", minValue:0, maxValue:10},
          vAxis: {title:this.state.salesRegion+" (in millions)"},
          legend: 'none',
          trendlines: {0:{}},
      };

      data.addColumn('number', 'Score');
      data.addColumn('number', this.state.salesRegion);
      if (this.state.data.length > 0){

          data.addRows(this.state.data);
      }
      else{
          console.log("here");
          data.addRows([[0,0]]);
          options.series = {
              0: {
                  color: 'transparent'
              }
          };
      }




      // Instantiate and draw the chart.
      let chart = new google.visualization.ScatterChart(document.getElementById('chart'));
      chart.draw(data, options);
    }
}