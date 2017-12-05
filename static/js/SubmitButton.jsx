import React, {Component} from 'react';
import Button from './Button';

export default class SubmitButton extends Component {

    constructor(props){
        super(props);
    }

    render(){
        return <Button className="col s4 offset-s5" handleSubmit={this.props.handleSubmit} buttonText={"Submit"}/>
    }
}
