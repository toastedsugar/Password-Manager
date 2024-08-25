import { useState } from "react"

import Auth from "./components/Auth"

export default function App() {
    const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false)

    return (
        <div>
            This is the frontend!!
        </div>
    )
}