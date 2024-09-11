import { useState } from 'react'

import Home from './components/Home'
import Login from './components/Login'

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false)

  return (
    <>
      {isLoggedIn ? <Home /> : <Login />}
    </>
  )
}

export default App
