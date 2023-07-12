import { PRIVATE_API_URL } from "$env/static/private";

export async function load({ url }) {
    const mainParams = ['krebs', 'thn', 'cisa', 'secweek'];
    let sources = false;

    let param = url.search.replace('?','');
    param = param.replace('=', '')
    
    const isValidParam = mainParams.includes(param);

    if(isValidParam){
        sources = await getSources(param);
    }

    return {
        sources: sources
    }
}

async function getSources(source){
    const response = await fetch(`${PRIVATE_API_URL}/api/sources?source=${source}`, {
        headers: {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
        }
    });

    const data = await response.json();
    return data;
}
