import React, {Component} from 'react';


export default class Button extends Component {

    constructor(props){
        super(props);
    }



    render(){
        return <button onClick={this.props.handleSubmit}>{this.props.buttonText}</button>
    }
}