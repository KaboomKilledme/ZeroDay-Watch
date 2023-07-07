<script>
    export let title = "Login";
    export let inputs = [
        {name:'username', placeholder:'Create Username', type:'text'},
        {name:'password', placeholder:'Create Password', type:'password'},
        {name:'checkPassword', placeholder:'Confirm Password', type:'password'},
    ];
    export let btnText;
</script>


<div class="AuthFormContainer">
    <form class="AuthForm" action="">
        <h1 class="AuthForm__title">{title}</h1>
        <div class="AuthFields">
            {#each inputs as input}
                <input class="AuthFields__input" id="{input.name}"
                placeholder="{input.placeholder}" type="{input.type}" >
            {/each}
        </div>
        <input class="AuthForm__submit" type="submit" value="{btnText}" name="" id="">
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