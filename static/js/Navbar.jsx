import React, {Component} from "react";

export default class Navbar extends Component {
    render(){
        return (
            <div>
                <nav>
                    <div className="nav-wrapper">
                      <a onClick={(e) => {e.preventDefault(); javascript:void(0);}} className="brand-logo center">Score Check</a>
                    </div>
                </nav>
            </div>
        );
    }
}