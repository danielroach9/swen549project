import React, {Component} from 'react';
import Filter from './Filter';


const REGION_OPTIONS = ["Global Sales", "Japan Sales", "North America Sales", "European Sales","Other"];

export default class RegionFilter extends Component {

    constructor(props){
        super(props);
        this.state = {
            value: REGION_OPTIONS[0],
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e){
        this.setState({
            value: e.target.value,
        });

        this.props.handleChange( 0, e.target.value );
    }

    createOptionsList(){
        return REGION_OPTIONS.map( ( option, idx ) => {
            return <option key={idx} value={option}> {option} </option>
        });
    }

    render(){
        let optTags = this.createOptionsList();
        return <Filter options={optTags} label={"Region Sales"} refVal={"region"} value={this.state.value} handleChange={this.handleChange}/>;
    }
}