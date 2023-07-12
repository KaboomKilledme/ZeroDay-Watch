<script>
    
    import Notification from "$lib/Main/Notification/+page.svelte";
    import { PUBLIC_API_URL } from "$env/static/public";
    import { createEventDispatcher } from "svelte";
    import { goto } from "$app/navigation";


    export let authToken;

    const dispatch = createEventDispatcher();

    async function deleteAccount(){

        const response = await fetch(`${PUBLIC_API_URL}/api/users/delete`, {
        method: 'POST',
        headers: {
            'Authorization':`Bearer ${authToken}`,
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
        }
        });   

        const data = await response.json();

        if(response.ok){
            displaySuccess('You have deleted your account')
            document.cookie ='authCookie=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
            goto('/register');

        } else {
            displayError(data.message)
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

<div class="DeleteAccountPromptBorder">
    <div class="DeleteAccountPrompt">
        <p class="DeleteAccountPrompt__text">
            Are you sure you want to delete this account permanently?
        </p>

        <div class="DeleteAccountPrompBtns">
            <button class="PromptBtn" on:click={deleteAccount}>
                <i class="accept fa-solid fa-check"></i>
            </button>

            <button class="PromptBtn" on:click={closeBtn}>
                <i class="decline fa-solid fa-xmark"></i>
            </button>
        </div>
    </div>
</div>


<style lang="scss">
    
    .DeleteAccountPromptBorder{
        opacity: 0;
        animation-name: fadeIn;
        animation-duration: .5s;
        opacity: 1;

        margin: auto;
        width: 18rem;
        min-height: 13rem;
        position: fixed;
        background: -webkit-linear-gradient(50deg, red, purple);
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

        .DeleteAccountPrompt{
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
            
            
            .DeleteAccountPrompt__text{
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

            .DeleteAccountPrompBtns{
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