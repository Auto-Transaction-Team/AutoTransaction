import React, { Component } from 'react';
import {BrowserRouter, Route, Switch} from "react-router-dom";
import { LinkContainer } from 'react-router-bootstrap'
import { Navbar, Nav } from 'react-bootstrap'
import { Container } from 'react-bootstrap'
import Main from '../components/main';
import Ticker from '../components/ticker';
import Rate from '../components/rate';
import Transaction from '../components/transaction';

class Header extends Component {
  render() {
    return (
      <BrowserRouter>
          <Navbar bg='dark' variant='dark'>
            <Nav className='mr-auto'>
              <LinkContainer to='/'>
                <Nav.Link>HOME</Nav.Link>
              </LinkContainer>
              <LinkContainer to='/ticker'>
                <Nav.Link>TICKER</Nav.Link>
              </LinkContainer>
              <LinkContainer to='/rate'>
                <Nav.Link>RATE</Nav.Link>
              </LinkContainer>
              <LinkContainer to='/transaction'>
                <Nav.Link>TRANSACTION</Nav.Link>
              </LinkContainer>
            </Nav>
          </Navbar>
          <Container>
          <Switch>
              <Route exact={true} path='/' component={Main}/>
              <Route exact={true} path='/ticker' component={Ticker}/>
              <Route exact={true} path='/rate' component={Rate}/>
              <Route exact={true} path='/transaction' component={Transaction}/>
          </Switch>
          </Container>
      </BrowserRouter>
    );
  }
}
export default Header;