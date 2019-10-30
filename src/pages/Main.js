import React from 'react';
import { Container, Segment } from 'semantic-ui-react';
import Header from '../components/shared/Header';

const Main = ({ children }) => (
  <Header>
    <Segment vertical>
      <Container>
        {children}
      </Container>
    </Segment>
  </Header>
);

export default Main;
