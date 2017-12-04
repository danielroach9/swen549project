import React, {Component} from 'react';
import $ from "jquery"
export default class Filter extends Component {

    constructor(props){
        super(props);
        this.state = {value: this.props.value};
        this.change = this.change.bind(this);
    }
    change(e){
        this.setState({value: e.target.value});
        this.props.handleChange(e);
    }

    componentDidMount(){
        $(".select").change(this.change);
    }

    render(){
        console.log(this.props.value);
        return (

            <div className="input-field col s4">
                <select className="select" value={this.state.value} onChange={this.change.bind(this)}>
                    {this.props.options}
                </select>
                <label>{this.props.label}</label>
            </div>
        );
    }
}