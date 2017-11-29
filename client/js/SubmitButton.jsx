import React, {Component} from 'react';
import Button from './Button';

export default class SubmitButton extends Component {

    constructor(props){
        super(props);
    }

    render(){
        return <Button handleSubmit={this.props.handleSubmit} buttonText={"Submit"}/>
    }
}
