Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure the CLERK_SECRET_KEY [environment variable](https://clerk.com/docs/deployments/clerk-environment-variables#clerk-publishable-and-secret-keys) is set, ie:

```bash
export CLERK_SECRET_KEY=my_secret_key
```

Start the server:

```bash
python3 manage.py runserver
```

From a Clerk frontend, use the `useSession` hook to retrieve the getToken() function:

```
const session = useSession();
const getToken = session?.session?.getToken
```

Then, request the python server with:

```
if (getToken) {
    await fetch("http://localhost:8000/clerk_jwt", {
        headers: {
            "Authorization": `Bearer ${await getToken()}`
        }
    })
}
```
