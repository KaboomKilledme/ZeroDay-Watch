import { PRIVATE_API_URL } from "$env/static/private";

export async function load({ cookies }) {
    
    const authToken = cookies.get('authCookie');

    const sources = await getBookmarks(authToken);

    return {
        sources: sources,
        authToken: authToken,
    }
}

async function getBookmarks(authToken){
    const response = await fetch(`${PRIVATE_API_URL}/api/bookmarks?title=`, {
        method: 'GET',
        headers: {
            'Authorization':`Bearer ${authToken}`,
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
        }
    });

    const data = await response.json();
    return data;
}
