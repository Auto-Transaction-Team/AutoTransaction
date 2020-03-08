import React, { Component } from 'react';
import axios from 'axios';

const RATEURL = 'http://localhost:8000/transaction/';

class Transaction extends Component {
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
            .get(RATEURL)
            .then((result) => {
              this.setState({getList: result.data})
            })
          } catch (error) {
            console.log("error!!");
          }
  }

  render() {
    let list = []
    // for (let [key, value] of Object.entries(this.state.getList)) {
    //   console.log(key)
    //   list.push(value[0] + ' : ' + value[1].rate + '\n');
    // }
    return (
      <div>
        <h1>Transaction</h1>
        <div style={{whiteSpace: 'pre-line'}}>{list}</div>
      </div>
    );
  }
}
export default Transaction;