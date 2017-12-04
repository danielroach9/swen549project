import React, {Component} from "react";
import Chart from "./Chart";
import Navbar from "./Navbar";
import $ from "jquery";

export default class App extends Component {
    constructor(props){
        super(props);
        $(document).ready(function() {
            $('select').material_select();
        });
    }



    render(){

        return(
            <div>
                <Navbar/>
                <Chart/>
            </div>
            )
        ;
    }
}