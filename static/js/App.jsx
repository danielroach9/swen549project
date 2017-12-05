import React, {Component} from "react";
import Chart from "./Chart";
import Navbar from "./Navbar";


export default class App extends Component {
    constructor(props){
        super(props);
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