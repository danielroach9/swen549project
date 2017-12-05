import React, {Component} from 'react';
import Filter from './Filter';

let SCORES = ["All",0,1,2,3,4,5,6,7,8,9,10];
export default class ScoreFilter extends Component {

    constructor(props){
        super(props);
        this.state = {
            value: SCORES[0],
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e){
        this.setState({
           value: e.target.value,
        });

        this.props.handleChange( 2, e.target.value );
    }

    createOptionTags(){
        return SCORES.map( (option,idx) => {
            return <option key={idx} value={option}> {option} </option>
        });

    }

    render(){
        let optTags = this.createOptionTags();
        return <Filter options={optTags} label={"Score"} refVal={"score"} value={SCORES[0]} handleChange={this.handleChange}/>
    }
}