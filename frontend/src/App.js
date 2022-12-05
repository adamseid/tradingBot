import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'



import Home from './components/home/Home'
import Tracker from './components/Tracker'

const App = () => {
  return (
    <Router>
        <Routes>
          <Route exact path="/" element={<Home/>}/>
          <Route exact path='/tracker' element={<Tracker/>}/>
        </Routes>
    </Router>
  );
}

export default App;