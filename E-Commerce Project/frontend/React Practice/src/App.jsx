import React from 'react';
import { useReducer } from 'react';
import Counter from './Counter';

const initialstate = 0;
const reducer = (state, action) => {
  
}

function App(){
  useReducer(reducer, initialstate)
  return(
    <div>
      <Counter />
    </div>
  )
}

export default App;