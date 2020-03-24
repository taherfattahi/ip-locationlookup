import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {

    state = {
        contacts: []
    };

    componentDidMount() {
        fetch('http://url:8000/api/?format=json')
            .then(res => res.json())
            .then((data) => {
                this.setState({contacts: data})
            })
            .catch(console.log)
    }

    render() {
        return (
            <div>
                {Object.keys(this.state.contacts).map((key) =>
                    <td>{key !== "time_zone" && key !== "currency" ? this.state.contacts[key]: ""}</td>)}
            </div>
        )
    }

}

export default App;
