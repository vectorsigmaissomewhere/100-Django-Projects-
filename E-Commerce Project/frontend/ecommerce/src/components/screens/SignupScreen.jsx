import React, {useState, useEffect} from 'react';
import {Container, Row, Col, Button, Form, Card} from 'react-bootstrap';
import {Link, useNavigate, useLocation} from 'react-router-dom';
import {useDispatch, useSelector} from "react-redux";
import Loader from '../Loader';
import Message from '../Message';
import InputGroup from "react-bootstrap/InputGroup";


function SignupScreen() {
  return (
    <>
    <Container className='mt-3 '>
      <Row>
        <Col md={4}>4</Col>
        <Col md={4}>
        <Card>
          <Card.Header as="h3" className='text-center bg-black text-light'>
            Signup
          </Card.Header>
          <Card.Body>
            <Form>
            <Form.Group className="mb-3" controlId="fname">
            <Form.Label><span><i className='fa fa-user'></i></span>First Name</Form.Label>
            <Form.Control type="text" placeholder="Enter your First Name" value="" required/>
            </Form.Group>
            <Form.Group className="mb-3" controlId="lname">
            <Form.Label><span><i className='fa fa-user'></i></span>Last Name</Form.Label>
            <Form.Control type="text" placeholder="Enter your Last Name" value="" required/>
            </Form.Group>
            <Form.Group className="mb-3" controlId="email">
            <Form.Label><span><i className='fa-regular fa-envelope'></i></span>Email</Form.Label>
            <Form.Control type="email" placeholder="Enter your Email" value="" required/>
            </Form.Group>
             
            <Form.Group className="mb-3" controlId="pass1">
            <Form.Label><span><i className=''></i></span>Password</Form.Label>
            <InputGroup className="mb-3">
            <InputGroup.Checkbox />
            {" "}
            <Form.Control 
            placeholder='Enter Password'
            required
            type='password'
            id='pass1'
            />
            </InputGroup>
            </Form.Group>
            <small>Password must include atleast [1-9][a-z][A-z][_$@*!..] & 5 Characters</small>
            <Form.Group className="mb-3" controlId="pass2">
            <Form.Label><span><i className=''></i></span>Confirm Password</Form.Label>
            <InputGroup className="mb-3">
            <InputGroup.Checkbox />
            {" "}
            <Form.Control 
            placeholder='Confirm Password'
            required
            type='password'
            id='pass2'
            />
            </InputGroup>
            </Form.Group>
            <br />
            <div className='d-grid gap-2'>
              <Button className='btn btn-md btn-success' type='submit'>Sign up</Button>
            </div>
            </Form>
          </Card.Body>
        </Card>
        </Col>
        <Col md={4}>12</Col>
      </Row>
    </Container>
    </>
  )
}

export default SignupScreen