import { useState } from "react"

export default function Login() {

    const [login, setLogin] = useState<boolean>(true)
    const [error, setError] = useState<string>()

    const [username, setUsername] = useState<string>("")
    const [password, setPassword] = useState<string>("")

    console.log(username)
    console.log(password)


    const HandleSubmit = (event:any) => {
        event?.preventDefault()
        console.log('Submitting')

        switch (login) {
            case true:
                // Submit login
                break;
            case false:
                // Submit register
                break;

            default:
                setError(() => `${login} failed`)
                break;
        }

    }

    const LoginBox = () => (
        <form onSubmit={HandleSubmit}>
            <label>Username:
                <input
                    name="usernameInput"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
            </label>
            <label>Password:
                <input
                    type="password"
                    name="usernameInput"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </label>
            <button type="submit">
                {login ? 'login' : 'register'}
            </button>
            <div onClick={() => setLogin((prevLogin) => !prevLogin)}>
                {login ? 'register' : 'login'}
            </div>
        </form>
    )
    const ShowError = () => (
        <div>{error}</div>
    )

    return (
        <div>
            <section>
                Welcome to the Password manager
            </section>
            <section>
                {LoginBox()}
            </section>
            <section>
                {error && ShowError()}
            </section>
        </div>
    )
}