import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import $ from 'jquery';


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
        $(ReactDOM.findDOMNode(this.refs[this.props.refVal])).material_select();
        $(ReactDOM.findDOMNode(this.refs[this.props.refVal])).change(this.change);
    }

    render(){
        return (
            <div className="input-field col s3 offset-s1">
                <select className="select" ref={this.props.refVal} value={this.state.value} onChange={this.change.bind(this)}>
                    {this.props.options}
                </select>
                <label>{this.props.label}</label>
            </div>
        );
    }
}