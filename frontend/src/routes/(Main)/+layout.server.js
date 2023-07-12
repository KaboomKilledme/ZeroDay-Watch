import { PRIVATE_API_URL } from "$env/static/private";
import { redirect } from '@sveltejs/kit';

export async function load({ cookies, }) {
    const authToken = cookies.get('authCookie');
    const isValidToken = await checkToken(authToken);

    console.log(isValidToken);

    if(!isValidToken){
        throw redirect(308, '/login');
    }

    return {
        isAuth: isValidToken
    }
    
}

async function checkToken(authToken){

    const response = await fetch(`${PRIVATE_API_URL}/api/token`, {
        headers: {
            'Authorization':`Bearer ${authToken}`,
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
        }
    })

    if(response.ok){
        return true;
    }
    return false
}