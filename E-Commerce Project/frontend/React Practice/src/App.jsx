// Example of a React application which renders a list of user items and allows us 
// add and remove items with callback handlers. We are using React's useState Hook 
// to make the list stateful
// function being saved // values being saved 

import React, { useCallback } from 'react';
import { v4 as uuidv4 } from 'uuid';

const App = () => {
  const [users, setUsers] = React.useState([
    { id: 'a', name: 'Robin' },
    { id: 'b', name: 'Dennis' },
  ]);

  const [text, setText] = React.useState('');

  const handleText = (event) => {
    setText(event.target.value);
  };

  const handleAddUser = () => {
    setUsers((prevUsers) => prevUsers.concat({ id: uuidv4(), name: text }));
  };

  // Memoize handleRemove to prevent re-creation on each render
  const handleRemove = useCallback(
    (id) => setUsers((prevUsers) => prevUsers.filter((user) => user.id !== id)),
    [users]
  );

  return (
    <div>
      <input type="text" value={text} onChange={handleText} />
      <button type="button" onClick={handleAddUser}>
        Add User
      </button>
      {/* Memoized List component */}
      <List list={users} onRemove={handleRemove} />
    </div>
  );
};

// Wrap List in React.memo to prevent re-render if props don't change
const List = React.memo(({ list, onRemove }) => {
  return (
    <ul>
      {list.map((item) => (
        <ListItem key={item.id} item={item} onRemove={onRemove} />
      ))}
    </ul>
  );
});

// Wrap ListItem in React.memo to prevent re-render if props don't change
const ListItem = React.memo(({ item, onRemove }) => {
  return (
    <li>
      {item.name}
      <button type="button" onClick={() => onRemove(item.id)}>
        Remove
      </button>
    </li>
  );
});

export default App;
