
export async function load({ cookies, }) {
    const authToken = cookies.get('authCookie');

    return {
        authToken: authToken
    }
    
}