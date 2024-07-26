import React from 'react'
import { Container } from 'react-bootstrap'
import Navbar from './components/Navbar'
import Footer from './components/Footer'


export default function App() {
  return (
    <>
    <div>
      <Navbar />
      <Container>
        <h1>Welcome to Django Rest Series using react-redux</h1>
      </Container>
      <Footer />
    </div>
    </>
  )
}
