import React, {Component} from 'react';

export default class Spinner extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return (
            <div className="row">
                <div className="col s6 offset-s6">
                    <div className="preloader-wrapper big active">
                        <div className="spinner-layer spinner-blue-only">
                            <div className="circle-clipper left">
                                <div className="circle">
                                </div>
                            </div>
                            <div className="gap-patch">
                                <div className="circle">
                                </div>
                            </div>
                            <div className="circle-clipper right">
                                <div className="circle">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}