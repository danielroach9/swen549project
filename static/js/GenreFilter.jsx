import React, {Component} from 'react';
import Filter from './Filter';

export default class GenreFilter extends Component {

    constructor(props){
        super(props);
        this.state = {
            value: this.props.genres[0],
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(e){
        this.setState({
           value: e.target.value,
        });

        this.props.handleChange( 1, e.target.value );
    }

    createOptionTags(){
        let options = [<option key={0} value="All" selected>All</option>];
        options.push(this.props.genres.map( (option,idx) => {
            return <option key={idx+1} value={option}> {option} </option>
        }));

        return options;
    }

    render(){
        let optTags = this.createOptionTags();
        let initialVal = optTags[0].innerHTML
        return <Filter options={optTags} label={"Genre"} refVal={"genre"} value={initialVal} handleChange={this.handleChange}/>
    }
}