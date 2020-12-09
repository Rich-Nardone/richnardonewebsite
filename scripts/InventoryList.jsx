// Displayes inventory list. Inventory list is retrieved from database
import React, { useState, useEffect } from 'react';
import { Socket } from './Socket';
import { fnt, brc } from './OptionMenu';

const div = {
  position: 'relative',
  width: 205,
  height: 200,
  background: 'orange',
  border: brc,
  boxShadow: '2px 5px black',
  borderRadius: 10,
  top: 100,

};
const p = {
  padding: 'auto',
  margin: 10,
  position: 'relative',
  border: brc,
  fontWeight: 'bold',
  textAlign: 'center',
  fontSize: fnt,

};
const ul = {
  height: 151,
  textAlign: 'left',
  overflow: 'scroll',
  fontStyle: 'italic',
  padding: 0,
  fontSize: fnt,

};

export function InventoryList() {
  const [inventory, setInventory] = useState([]);

  function retrievePlayerInventory() {
    useEffect(() => {
      Socket.emit('get inventory');
      Socket.on('user inventory', (data) => {
        setInventory(data);
      });
    }, []);
  }
  const displayInventory = inventory.map((item, index) => (
    // eslint-disable-next-line react/no-array-index-key
    <li key={index}>
      {' '}
      {item}
      {' '}
    </li>
  ));

  retrievePlayerInventory();

  return (
    <div style={div}>
      <p style={p}> INVENTORY </p>
      <ul style={ul}>
        {' '}
        {displayInventory}
        {' '}
      </ul>
    </div>
  );
}

export default InventoryList;
