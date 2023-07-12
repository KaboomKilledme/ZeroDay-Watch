<script>
    import { PUBLIC_API_URL } from "$env/static/public";
    import { createEventDispatcher } from "svelte";
    import Notification from "$lib/Main/Notification/+page.svelte";

    const dispatch = createEventDispatcher()

    export let authToken;

    let inputValues = [null, null, null];

    let inputs = [
        {id:1, name:'username', placeholder:'Update Username'},
        {id:2, name:'password', placeholder:'Update Password'},
        {id:3, name:'checkPassword', placeholder:'Confirm Password'}
    ]

    function handleSubmit(event){
        const username = inputValues[0];
        const password = inputValues[1];
        const checkPassword = inputValues[2];
        
        event.preventDefault();

        if(password !== checkPassword){
            displayError('Passwords Do Not Match');
        } else {
            updateDetails(username, password);
        }

        closeForm();

        inputValues = [null, null, null];

    }

    async function updateDetails(username, password){
            const response = await fetch(`${PUBLIC_API_URL}/api/users`, {
            method: "POST",
            headers: {
                'Authorization':`Bearer ${authToken}`,
                "Accept": "application/vnd.api+json",
                "Content-Type": "application/vnd.api+json",
            },
            body: JSON.stringify({
                    name: username,
                    password: password,
                }),
            });
            
            const data = await response.json();
            
            if(response.ok){
                displaySuccess('Account Details have been updated');
            
            }else{
                displayError(data.message);
            }
        }
        

    function handleInput(event){
        if( event.target.id === "password" || 
            event.target.id === "checkPassword"
        ){
            event.target.type = "password"
        }
    }

    function closeForm(){
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

<div class="UpdateFormBorder">
    <form class="UpdateForm" id="UpdateForm">
        <h1 class="UpdateForm__title">Change Details</h1>
        <div class="UpdateFormFields">
            {#each inputs as input}
                <input
                class="UpdateFormFields__input" 
                id={input.name} placeholder={input.placeholder} 
                bind:value={inputValues[input.id-1]}
                on:input={handleInput} >
            {/each}
        </div>

        <button form="UpdateForm" on:click={handleSubmit}
        class="UpdateForm__btn" >update</button>

    </form>
</div>

<style lang="scss">
    .UpdateFormBorder{
        opacity: 0;
        animation-name: fadeIn;
        animation-duration: .5s;
        
        opacity: 1;
        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;

        width: 20rem;

        position: absolute;
        
        align-items: center;
        justify-content: center;
        padding: .5rem;
        margin:auto;
        background: none; 
        border-radius: 1rem;
        transition: 1s;


        .UpdateForm{
            font-family: 'Zekton';
            background: black;
            width: 100%;
            height: 80%;
            border-radius: 1rem;
            padding-bottom: 3rem;
            display: flex;
            display: -ms-flexbox;
            display: -webkit-flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            color: white;

        
            .UpdateForm__title{
                font-family: $primaryFont;
            }

            .UpdateForm__btn{
                width: 80%;
                height: 3rem;
                background: $linearGradient1;
                border: none;
                font-size: 1.25rem;
                font-family: $primaryFont;
                letter-spacing: .3rem;
                text-transform: uppercase;
                &:hover{
                    background: rgb(37, 37, 37);
                    color: white;
                }
            }

            .UpdateFormFields{
    
                width: 100%;
                display: flex;
                display: -ms-flexbox;
                display: -webkit-flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;

                .UpdateFormFields__input{
                    color: white;
                    height: 2.5rem;
                    background: $backgroundColour;
                    width: 80%;
                    border: none;
                    outline: none;
                    margin-bottom: 2rem;
                    text-indent: 1rem ;
                    font-size: 1.2rem;
                    opacity: .8;

                    &::placeholder{
                        font-family: $primaryFont;
                    }

              
                }   
    
            }
        }

    }
</style>