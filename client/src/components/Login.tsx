import { useState } from "react"

import axios from "axios"

export default function Login() {

    const [login, setLogin] = useState<boolean>(true)
    const [error, setError] = useState<string>()

    const [formData, setFormData] = useState({
        username: '',
        password: ''
    });

    console.log(formData)

    const HandleChange = (e: any) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const HandleLogin = (e:any) => {
        e.preventDefault(); // Prevent the default form submission
        axios.post('http://localhost:8080/auth/login', formData, {
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => {
            console.log('Success:', response.data);
        })
        .catch(error => {
            console.error('Error:', error);
            setError(error)
        });
    };

    const HandleRegister = (e:any) => {
        e.preventDefault(); // Prevent the default form submission
        axios.post('http://localhost:8080/auth/register', formData, {
            headers: {
                'Content-Type': 'application/json',
            }
        })
        .then(response => {
            console.log('Success:', response.data);
        })
        .catch(error => {
            console.error('Error:', error);
            setError(error)
        });
    };

    const LoginForm = () => (
        <form onSubmit={login ? HandleLogin : HandleRegister}>
            <label>Username:
                <input
                    name="username"
                    value={formData.username}
                    onChange={HandleChange}
                />
            </label>
            <label>Password:
                <input
                    type="password"
                    name="password"
                    value={formData.password}
                    onChange={HandleChange}
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
                {LoginForm()}
            </section>
            <section>
                {error && ShowError()}
            </section>
        </div>
    )
}