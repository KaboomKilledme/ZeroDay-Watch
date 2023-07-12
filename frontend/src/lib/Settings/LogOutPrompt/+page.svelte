<script>
    import Notification from "$lib/Main/Notification/+page.svelte";
    import { PUBLIC_API_URL } from "$env/static/public";
    import { createEventDispatcher } from "svelte";
    import { goto } from "$app/navigation";


    export let authToken;

    const dispatch = createEventDispatcher();



    async function logout(){

        const response = await fetch(`${PUBLIC_API_URL}/api/logout`, {
        method: 'POST',
        headers: {
            'Authorization':`Bearer ${authToken}`,
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
        }
        });   
        const data = await response.json();

        if(response.ok){
            displaySuccess('You have logged out')
            document.cookie ='authCookie=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
            goto('/login');

        } else {
            displayError('Something Went Wrong')
        }
    }

    function closeBtn(){
        dispatch('close', {
            id: null
        })
    }

    function displayError(message){
        displayNotification('error', message);
    }

    function displaySuccess(message){
        displayNotification('success', message);
    }

    function displayNotification(type, message){
        const Notifications = document.querySelector(`.MainContainer`);
        new Notification({
            target: Notifications,
            props: {
                type:type,
                text: message
            }
        })
    }

</script>

<div class="LogOutPromptBorder">
    <div class="LogOutPrompt">
        <p class="LogOutPrompt__text">
            Are you sure you want to log out?
        </p>

        <div class="LogOutPrompBtns">
            <button class="PromptBtn" on:click={logout}>
                <i class="accept fa-solid fa-check"></i>
            </button>

            <button class="PromptBtn" on:click={closeBtn}>
                <i class="decline fa-solid fa-xmark"></i>
            </button>
        </div>
    </div>
</div>


<style lang="scss">
    
    .LogOutPromptBorder{
        opacity: 0;
        animation-name: fadeIn;
        animation-duration: .5s;
        opacity: 1;

        margin: auto;
        width: 18rem;
        min-height: 13rem;
        position: fixed;
        background: $linearGradient1;
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        align-items: center;
        justify-content: center;
        padding: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
        border-radius: 1rem;
        
        @media screen and (max-width: 370px){
            width: 70%;        
        }

        .LogOutPrompt{
            background: black;
            width: 95%;
            height: 90%;
            position:absolute;
            border-radius: 1rem;
            display: flex;
            display: -ms-flexbox;
            display: -webkit-flex;
            flex-direction: column;
            
            justify-content: center;
            align-items: center;
            
            
            .LogOutPrompt__text{
                height: 50%;
                display: flex;
                display: -ms-flexbox;
                display: -webkit-flex;
                flex-direction: row;
                padding: 0 .2rem 0.2rem;
                justify-content: center;
                align-items: center;
                color: white;
                text-align: center;
                font-size: 1.5rem;
                font-family: $primaryFont;
            }

            .LogOutPrompBtns{
                margin: auto;
                display: flex;
                display: -ms-flexbox;
                display: -webkit-flex;
                flex-direction: row;
                justify-content: space-between;
                width: 30%;
                                
                .PromptBtn{
                    background:none;
                    border: none;
                    font-size: 2rem;
                                
                    .accept{
                        color: rgb(24, 231, 24);
                        &:hover{
                            color: white;
                        }
                    }

                    .decline{
                        color: red;
                        &:hover{
                            color: white;
                        }
                    }
                }
          
            }
        }
    }

</style>