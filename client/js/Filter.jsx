import React, {Component} from 'react';

export default class Filter extends Component {

    constructor(props){
        super(props);
        this.state = {value:''};
    }


    render(){
        const {label, options } = this.props;
        return (<div>
            <label>{label}</label>
            <select value={this.props.value} onChange={this.props.handleChange}>
                {options}
            </select>
        </div>);
    }
}