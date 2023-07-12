<script>
    import { PUBLIC_API_URL } from "$env/static/public";
    import Notification from "$lib/Main/Notification/+page.svelte";

    export let title;
    export let inputs;
    export let btnText;

    let inputValues = [null, null, null]

    function handleInput(event){
        if( event.target.id === "password" || 
            event.target.id === "checkPassword"
        ){
            event.target.type = "password"
        }
    }

    function handleSubmit(event){
        const username = inputValues[0];
        const password = inputValues[1];
        const checkPassword = inputValues[2];
        
        event.preventDefault();
        
        if(title === "login"){
            login(username, password)
        } else if (title === "register"){
            register(username, password, checkPassword)
        }

        inputValues = [null, null, null];

    }

    function register(username, password, checkPassword){
    
        if(password === checkPassword){
            console.log('Same password')
            authenticate(username, password)
        } else {       
            console.log('Different password')
            displayError('Passwords do not match');
        }
        
    }

    function login(username, password){
        authenticate(username, password)
    }

    async function authenticate(username, password){
        const response = await fetch(`${PUBLIC_API_URL}/api/${title}`, {
            method: "POST",
            headers: {
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
                displaySuccess('You have logged in');
                console.log(data);

            }else{
                displayError(data.message);
            }

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


<div class="AuthFormContainer">
    <form class="AuthForm" id="AuthForm" >
        <h1 class="AuthForm__title">{title}</h1>
        <div class="AuthFields">
            {#each inputs as input}
                <input class="AuthFields__input" id="{input.name}" 
                placeholder="{input.placeholder}" bind:value={inputValues[input.id-1]} 
                on:input={handleInput}
                >
            {/each}
        </div>
        <button class="AuthForm__submit" form="AuthForm" on:click={handleSubmit}>
            {btnText}
        </button> 
    </form>
</div>



<style lang="scss">
.AuthFormContainer{
    display: flex;
    display: -ms-flexbox;
    display: -webkit-flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    height: 100vh;
    width:100%;

    .AuthForm{
        width: 22rem;
        background: black;
        
        padding-bottom: 4rem;
        padding-left: 2rem;
        padding-right: 2rem;

        display: flex;
        display: -ms-flexbox;
        display: -webkit-flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        clip-path: polygon(
            0 2rem,
            2rem 0,
            100% 0,
            100% calc(100% - 2rem),
            calc(100% - 2rem) 100%,
            0 100%
        );

        @media screen and (max-width: 480px){
            background:none;
        }

        @media screen and (max-width: 320px){
            width: 98vw;
        }

        .AuthForm__title{
            background: $linearGradient1;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem;
            font-family:  'Zekton';
            font-weight: bold;
            letter-spacing: .3rem;
            margin-bottom: 1rem;
            text-transform: uppercase;
        }

        .AuthFields{
    
            width: 100%;
            display: flex;
            display: -ms-flexbox;
            display: -webkit-flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            
            .AuthFields__input{
                color: white;
                height: 2.8rem;
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

                @media screen and (max-width: 480px){
                    background: black;
                    opacity: 1;
                }
            }

        }
        .AuthForm__submit{
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
    }

}


</style>