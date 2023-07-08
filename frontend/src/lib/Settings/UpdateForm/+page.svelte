<script>
    import { createEventDispatcher } from "svelte";
    const dispatch = createEventDispatcher()

    let inputs = [
        {id:'username', placeholder:'Update Username', type:'text'},
        {id:'password', placeholder:'Update Password', type:'password'},
        {id:'confirmPassword', placeholder:'Confirm Password', type:'password'}

    ]

    function closeForm(){
        dispatch('close', {
            id: null
        })
    }
</script>

<div class="UpdateFormBorder">
    <form class="UpdateForm">
        <h1 class="UpdateForm__title">Change Details</h1>
        <div class="UpdateFormFields">
            {#each inputs as input}
                <input
                class="UpdateFormFields__input" 
                id={input.id} placeholder={input.placeholder} type={input.type} >
            {/each}

        </div>

        <input on:click={() => {closeForm()}}
        class="UpdateForm__btn"
        type="submit" value="update">
    </form>
</div>

<style lang="scss">
    .UpdateFormBorder{

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