import React, {Component} from 'react';


export default class Button extends Component {

    constructor(props){
        super(props);
    }



    render(){
        return <a className="waves-effect waves-light btn col s3 offset-s5" onClick={this.props.handleSubmit}>{this.props.buttonText}</a>;
    }
}