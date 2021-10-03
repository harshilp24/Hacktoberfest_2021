import { useState, useEffect } from 'react';

import Select from 'react-select';
import axios from 'axios';
import { currencyCodes } from './currencyLabel';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faExchangeAlt, faCommentsDollar } from '@fortawesome/free-solid-svg-icons'
import 'dotenv/config';

import './App.css';


export default function App() {
  const [base, setBase] = useState(currencyCodes[145]); //USD
  const [pair, setPair] = useState(currencyCodes[43]); // EUR
  const [baseAmount, setBaseAmount] = useState(1);
  const [conversion, setConversion] = useState('');
  const [width, setInnerWidth] = useState(window.innerWidth)

  useEffect(() => {
    const url = `https://v6.exchangerate-api.com/v6/${process.env.REACT_APP_API_KEY}/pair/${base.value}/${pair.value}/${baseAmount}`;
    axios.get(url).then(res => {
      setConversion(res.data.conversion_result);
    }).catch(() => {
      // no error handling yet
      alert('Request Failed. Make sure your API credentials are valid.');
    })
  }, [baseAmount, base, pair]);

  const handleReverse = () => {
    const newBase = pair;
    const newPair = base;
    setBase(newBase);
    setPair(newPair);
  }
  window.addEventListener('resize', () => {
    setInnerWidth(window.innerWidth);
  })

  return (
    <div className="container">
      <header id="header">
        <h1>
          Currency Converter
          <FontAwesomeIcon
            icon={faCommentsDollar}
            style={{marginLeft: '20px'}}
          />
        </h1>
      </header>

      <main id="main">

        <div id="base">
          <h2 className="label">From</h2>
          <input
            id="baseAmount"
            placeholder="Enter an amount"
            type="number"
            value={baseAmount}
            onChange={e => setBaseAmount(e.target.value)}
          />
          <Select
            className="selection"
            options={currencyCodes}
            value={base}
            onChange={setBase}
          />
        </div>

        <div id="btn-container">
          <button className="btn" onClick={handleReverse}>
            <FontAwesomeIcon
              icon={faExchangeAlt}
              transform={{rotate: width > 720 ? 0 : 90}}
            />
          </button>
        </div>

        <div id="pair">
          <h2 className="label">To</h2>
          <p className="amount">{conversion}</p>
          <Select
            className="selection"
            options={currencyCodes}
            value={pair}
            onChange={setPair}
          />
        </div>

      </main>
    </div>
  );
}
