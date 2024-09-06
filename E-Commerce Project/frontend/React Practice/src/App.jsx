import React from 'react';
import { useReducer } from 'react';

const initialstate = 0;
const reducer = (state, action) => {
  
}

function App(){
  useReducer(reducer, initialstate)
  return(
    <div>
      <button>Increment</button>
      <button>Decrement</button>
    </div>
  )
}

export default App;