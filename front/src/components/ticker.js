import React, { Component } from 'react';
import axios from 'axios';

const TICKERURL = 'http://localhost:8080/ticker/';

class Ticker extends Component {
  constructor(props) {
    super(props);
    this.state = {
      getList: []
    };

    this.display = this.display.bind(this)
  }

  componentDidMount(){
    this.display()
  }

  display() {
    try {
          axios
            .get(TICKERURL)
            .then((result) => {
              this.setState({getList: result.data})
            })
          } catch (error) {
            console.log("error!!");
          }
  }

  render() {
    let list = []
    for (let [key, value] of Object.entries(this.state.getList)) {
      list.push(key + ' : ' + value + '\n');
    }
    return (
      <div>
        <h1>Ticker</h1>
        <div style={{whiteSpace: 'pre-line'}}>{list}</div>
      </div>
    );
  }
}
export default Ticker;