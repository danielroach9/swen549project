import React, {Component} from 'react';
import Filter from './Filter';


const REGION_OPTIONS = ["","Global Sales", "Japan Sales", "North America Sales", "European Sales"];

export default class RegionFilter extends Component {

    constructor(props){
        super(props);
        this.state = {
            value: REGION_OPTIONS[0],
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e){
        e.preventDefault();
        this.setState({
            value: e.target.value,
        });
        this.props.handleChange(this.state.value);
    }

    createOptionsList(){
        return REGION_OPTIONS.map( ( option, idx ) => {
            return <option key={idx}> {option} </option>
        });
    }

    render(){
        let optTags = this.createOptionsList();
        return <Filter options={optTags} label={"Region Sales"} handleChange={this.handleChange}/>;
    }
}